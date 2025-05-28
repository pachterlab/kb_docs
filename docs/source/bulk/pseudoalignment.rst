Pseudoalignment of bulk RNA seq data
=======================================


.. note::

   **To align bulk RNA-seq data against a protein or amino acid reference, see:** 
   `Translated Pseudoalignment </../translated/pseudoalignment>`_


Quantification
--------------


To quantify bulk RNA-seq reads, run ``kb count`` with the ``-x BULK`` option.

Say, we are mapping paired-end reads to an index stored in the the file `human_index.idx` (and the transcript-to-gene mapping file produced by ``kb ref`` is `human_t2g.txt`). Let's say our reads came from a knockdown experiment and we have three control samples (C_1, C_2, C_3) and three knockdown samples (KD_1, KD_2, KD_3). We can run the following (note that the order in which the input read files are supplied determines the sample identities after read quantification):


.. code-block:: text

   kb count -x BULK -i human_index.idx -g human_t2g.txt \
   --parity=paired --tcc --matrix-to-directories -o output_dir \
   C_1_R1.fastq.gz C_1_R2.fastq.gz \
   C_2_R1.fastq.gz C_2_R2.fastq.gz \
   C_3_R1.fastq.gz C_3_R2.fastq.gz \
   KD_1_R1.fastq.gz KD_1_R2.fastq.gz \
   KD_2_R1.fastq.gz KD_2_R2.fastq.gz \
   KD_3_R1.fastq.gz KD_3_R2.fastq.gz


Other options that might be relevant are setting the ``--strand`` option to either forward or reverse if you have stranded RNA-seq reads, and also setting ``--bootstraps`` if performing differential expression analysis.

The quantification output will be stored in `output_dir/quant_unfiltered/`, which contains the directories abundance_1, abundance_2, abundance_3, abundance_4, abundance_5, abundance_6 corresponding for our six samples (in the order they were provided). For example `output_dir/quant_unfiltered/abundance_1/abundance.tsv` will contain the transcript abundances for the C_1 control sample.



Differential transcript expression
----------------------------------


See the tutorial for a full example of using kallisto with edgeR for differential transcript expression.


Differential gene expression
----------------------------

For differential gene expression, one can use sleuth (which can also perform different transcript expression) or one can import the kallisto results into tximport and then use a program such as DESeq2. 


For `tximport <https://bioconductor.org/packages/devel/bioc/vignettes/tximport/inst/doc/tximport.html#kallisto>`_, we can do:

.. code-block:: R

   # Install tximport
   if (!require("BiocManager", quietly = TRUE))
       install.packages("BiocManager")
   BiocManager::install("tximport")

   # Include tximport
   require(tximport)

   # Load transcript-to-gene mapping
   t2g <- read.delim("human_t2g.txt", header = FALSE, sep = "\t")
   t2g <- t2g[, 1:2]

   # Prepare file paths and sample info
   base_dir <- "output_dir/quant_unfiltered"
   dirs <- list.dirs(base_dir, full.names = FALSE, recursive = FALSE)
   abundance_dirs <- dirs[grepl("^abundance_\\d+$", dirs)]
   files <- file.path(base_dir, abundance_dirs, "abundance.h5")
   names(files) <- paste0("sample", 1:length(files))

   # Run tximport
   txi.kallisto <- tximport(files, type = "kallisto", txOut = TRUE)

   # Summarize to gene-level
   txi.kallisto.sum <- summarizeToGene(txi.kallisto, t2g)


Here is a sleuth tutorial (https://pachterlab.github.io/sleuth_walkthroughs/trapnell/analysis.html); the first few steps are to create a sleuth object which we can do as follows:

.. code-block:: R

    # Install sleuth and rdhf5
   if (!require("BiocManager", quietly = TRUE))
       install.packages("BiocManager")
   BiocManager::install("rhdf5")
   install.packages("devtools")
   devtools::install_github('pachterlab/sleuth')

   # Include sleuth
   require(sleuth)

   # Load transcript-to-gene mapping
   t2g <- read.delim("human_t2g.txt", header = FALSE, sep = "\t")
   t2g <- t2g[, 1:2]
   colnames(t2g) <- c("target_id", "gene_id")

   # Prepare file paths and sample info
   base_dir <- "output_dir/quant_unfiltered"
   dirs <- list.dirs(base_dir, full.names = FALSE, recursive = FALSE)
   abundance_dirs <- dirs[grepl("^abundance_\\d+$", dirs)]
   files <- file.path(base_dir, abundance_dirs)
   samples <- paste0("sample", 1:length(files))
   conditions <- c("control", "control", "control", "knockdown", "knockdown", "knockdown")
   s2c <- data.frame(sample=samples, condition=conditions, path=files, stringsAsFactors=FALSE)

   # Prepare a sleuth orject
   so <- sleuth_prep(s2c, target_mapping = t2g)


