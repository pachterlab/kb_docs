SPLIT-Seq preprocessing
=======================

Here, we demonstrate how to preprocess SPLiT-seq single-cell RNA-seq data (Parse Biosciences). The main difference between the preprocessing steps of 10x and SPLiT-seq is that 1) The technology string (-x) needs to be modified to extract the multiple barcodes that are linked together, 2) Two "on lists" need to be provided: one for barcode error correction and the other to "replace" the random oligomer barcodes with the polyT barcodes (since SPLiT-seq uses two sets of barcoded primers, therefore two different barcodes may belong to thesame cell).

Let's say we have our SPLiT-seq data files: ``R1.fastq.gz`` and ``R2.fastq.gz``, and let's say they are from a human sample.

We first download the human index as before.


.. code-block:: shell

   kb ref -d human -i index.idx -g t2g.txt

Next, we download the two "on lists":

.. code-block:: shell

   wget
   wget 


Next, we use ``kb count`` to pseudoalign the reads.

.. code-block:: shell

   kb count --h5ad --strand=forward -w onlist.txt -r replace.txt -g t2g.txt -x SPLIT-SEQ -i c57bl6j.idx -t 24 -o out_dir/ R1.fastq.gz R2.fastq.gz


.. note::

   Here we use `-x SPLiT-SEQ` which applies to SPLiT-seq versions 1 and 2. We can design a custom technology string for newer versions of SPLiT-seq; for example, SPLiT-seq version 3 would be ``-x "1,10,18,1,30,38,1,50,58:1,0,10:0,0,0"`` (8-bp barcodes separated by 12-bp linkers). See the technology (-x) string section for more details.



The count matrices will be located in ``out_dir/counts_unfiltered_modified`` (note: this directory contains the count matrices generated from the "modified" barcodes wherein the random oligomer barcodes were replaced by polyT barcodes -- this is what we want to use; however, the count matrices produced from the original unmodified barcodes are also outputted in a separate directory).

Next, we load in the AnnData object that is generated in that directory:

.. code-block:: python

   adata = anndata.read_h5ad('counts_unfiltered_modified/adata.h5ad')



.. note::

   See the other single-cell tutorials for the downstream processing steps.



