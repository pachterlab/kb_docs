Pseudoalignment of bulk RNA seq data
=======================================

.. toctree::
   :maxdepth: 1

   alignment_types/standard
   alignment_types/matrices

.. note::

   **To align bulk RNA-seq data against a protein or amino acid reference, see:** 
   `Translated Pseudoalignment </../translated/pseudoalignment>`_


Quantification
--------------


To quantify bulk RNA-seq reads, run `kb count` with the `-x BULK` option.

Say, we are mapping paired-end reads to an index stored in the the file `human_index.idx` (and the transcript-to-gene mapping file produced by `kb ref` is `human_t2g.txt`). Let's say our reads came from a knockdown experiment and we have three control samples (C_1, C_2, C_3) and three knockdown samples (KD_1, KD_2, KD_3). We can run the following (note that the order in which the input read files are supplied determines the sample identities after read quantification):


.. code-block:: text

   kb count -x BULK -i human_index.idx -g human_t2g.txt \
   --parity=paired --tcc --matrix-to-directories -o output_dir \
   C_1_R1.fastq.gz C_1_R2.fastq.gz \
   C_2_R1.fastq.gz C_2_R2.fastq.gz \
   C_3_R1.fastq.gz C_3_R2.fastq.gz \
   KD_1_R1.fastq.gz KD_1_R2.fastq.gz \
   KD_2_R1.fastq.gz KD_2_R2.fastq.gz \
   KD_3_R1.fastq.gz KD_3_R2.fastq.gz


Other options that might be relevant are setting the `--strand` option to either forward or reverse if you have stranded RNA-seq reads, and also setting `--bootstraps` if performing differential expression analysis.

The quantification output will be stored in `output_dir/quant_unfiltered/`, which contains the directories abundance_1, abundance_2, abundance_3, abundance_4, abundance_5, abundance_6 corresponding for our six samples (in the order they were provided). For example `output_dir/quant_unfiltered/abundance_1/abundance.tsv` will contain the transcript abundances for the C_1 control sample.



Differential transcript expression
----------------------------------


See the tutorial for a full example of using kallisto with edgeR for differential transcript expression.


Differential gene expression
----------------------------

For differential gene expression, one can use sleuth or one can import the kallisto results into tximport and then use a program such as DESeq2. 

https://pachterlab.github.io/sleuth_walkthroughs/trapnell/analysis.html

https://bioconductor.org/packages/devel/bioc/vignettes/tximport/inst/doc/tximport.html#kallisto

