SPLIT-Seq preprocessing
=======================

Here, we demonstrate how to preprocess SPLiT-seq (Parse Biosciences) single-cell RNA-seq data using kb-python.  
The preprocessing steps are similar to those used for 10x data, but with two key differences:

1. The technology string ``-x`` must be customized to extract multiple barcode segments rather than a single barcode.
2. Two **on-lists** are required:  
   - one for barcode error correction  
   - one for converting random-oligo barcodes into poly-T barcodes

Let's say we have two SPLiT-seq data files: ``R1.fastq.gz`` and ``R2.fastq.gz`` from a human sample.

We first download the human index as before:


.. code-block:: shell

   kb ref -d human -i index.idx -g t2g.txt

Next, we download the two on-lists:

.. code-block:: shell

   wget https://raw.githubusercontent.com/pachterlab/kb_docs/refs/heads/main/docs/barcodes/splitseqv2_barcodes.txt -O onlist.txt
   wget https://raw.githubusercontent.com/pachterlab/kb_docs/refs/heads/main/docs/barcodes/splitseqv2_replace.txt -O replace.txt


.. note::

   The above on-lists are for SPliT-seq version 2. For version 3, see `splitseqv3_barcodes.txt <https://raw.githubusercontent.com/pachterlab/kb_docs/refs/heads/main/docs/barcodes/splitseqv3_barcodes.txt>`_ and `splitseqv3_replace.txt <https://raw.githubusercontent.com/pachterlab/kb_docs/refs/heads/main/docs/barcodes/splitseqv3_replace.txt>`_.



Next, we use ``kb count`` to pseudoalign the reads.

.. code-block:: shell

   kb count --h5ad --strand=forward -w onlist.txt -r replace.txt -g t2g.txt -x SPLIT-SEQ -i c57bl6j.idx -t 24 R1.fastq.gz R2.fastq.gz


.. note::

   Here we use `-x SPLIT-SEQ` which applies to SPLiT-seq versions 1 and 2. We can design a custom technology string for newer versions of SPLiT-seq. For example, SPLiT-seq version 3 would be ``-x "1,10,18,1,30,38,1,50,58:1,0,10:0,0,0"`` (8-bp barcodes separated by 12-bp linkers). See the :ref:`technologies and the -x string <technologies-section>` section for more details.


The count matrices with collapsed random-oligo and polyT barcodes will be stored in ``counts_unfiltered_modified``. The count matrices produced from the original unmodified barcodes are also outputted in a separate directory.

Next, we load in the AnnData object that is generated in the `counts_unfiltered_modified` directory for downstream analysis:

.. code-block:: python

   adata = anndata.read_h5ad('counts_unfiltered_modified/adata.h5ad')



.. note::

   See the other single-cell tutorials for the downstream processing steps.



