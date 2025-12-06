Long read pseudoaligment
=======================================
.. note:: **Reference:**
   Loving, R, Sullivan, DK, Reese, F, Rebboah, E, Sakr, J, Rezaie, N, Liang, HY, Filimban, G, Kawauchi, S, Oakes, C, Trout, D, Williams, BA, MacGregor, G, Wold, BJ, Mortazavi, A, Pachter, L 
   `Long-read sequencing transcriptome quantification with lr-kallisto. <https://doi.org/10.1101/2024.07.19.604364>`_  
   bioRxiv 2024.07.19.604364
   https://doi.org/10.1101/2024.07.19.604364

kallisto can perform long-read pseudoalignment of nucleotide sequences against a large *k*-mer reference while retaining single-cell (for single-cell RNA sequencing data) or sample (for bulk RNA seq data) resolution. To perform long-read pseudoalignment, first add ``-k 63`` to ``kb ref`` and, second, add the ``--long`` flag to the ``kb count`` commands.

Long-read pseudoalignment with **lr-kallisto**, which performs alignment using an extended k-mer length (> 31 bases), improves transcript-to-gene mapping quality. As k-mer length increases, the number of transcripts in a compatibility class decreases on average, raising the probability that reads map to the correct compatibility class. Additionally, longer k-mers increase the likelihood that equivalence class intersections will be nonempty, which improves the overall mapping rate.

The workflow can be executed in three lines of code, and computational requirements do not exceed those of a standard laptop. Building on kallisto’s versatility, the workflow is compatible with all state-of-the-art single-cell and bulk RNA sequencing methods, including but not limited to SMART-Seq and SPLiT-Seq (including Parse Biosciences) and performance is state-of-the-art on both PacBio and Oxford Nanopore Technologies long-read data.

.. _lr-bulk-rna-seq:

Long read pseudoalignment of bulk RNA-seq data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The long-read pseudoalignment workflows can be used to align RNA sequencing data to any transcriptome reference:

1. Install `kb-python` (optional: install `gget <https://github.com/pachterlab/gget>`_ to fetch the host genome and transcriptome):

.. code-block:: bash

   pip install kb-python gget

2. Create reference index (using the D-list of human genome):

.. code-block:: bash

   kb ref \
       -k 63 \
       --d-list $(gget ref --ftp -w dna homo_sapiens) \
       --workflow standard \
       -i index.idx \
       -g t2g.txt \
       -f1 fasta.fa \
       $(gget ref --ftp -w dna,gtf homo_sapiens)

3. Align and quantify sequencing reads:

.. code-block:: bash

   kb count \
       --long \
       -i index.idx \
       -g t2g.txt \
       --parity single \
       --tcc \
       --matrix-to-directories \
       -x bulk \
       $USER_DATA.fastq.gz

.. _lr-sc-rna-seq:

Long read pseudoalignment of single-cell RNA-seq data
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Processing long-read single-cell data with kallisto requires several preprocessing steps.  
In this workflow, **seqspec** and **splitcode** are used together to automate barcode and sequence extraction for **LR-SPLiT-seq**.

First, seqspec is used to generate a machine-readable configuration file describing the structure of the sequencing reads, including the locations of barcodes, UMIs, and the biological sequence.  
This configuration file is then supplied to splitcode, which extracts these components directly from the raw reads.

The output from splitcode may be streamed directly into kallisto or saved to disk for later processing.

The long-read pseudoalignment workflows can be used to align RNA sequencing data to any transcriptome reference:

1. Create splitcode config file using seqspec:

.. code-block:: bash 
  
  seqspec index -m rna -s file -t splitcode spec.yaml > seqspec-config.txt

2. Use splitcode to extract barcodes, umis, and biological sequences:

.. code-block:: bash 

  splitcode -c seqspec-config.txt $sample_data.fastq.gz -o $sample_data_modified.fastq.gz -t 32

3. Importantly, the extracted sequences may need reorienting for the sample to be processed appropriately; we give an example of this in the case of ONT single-nuclei samples in the tutorials. 

4. Create reference index (using the D-list of human genome):

.. code-block:: bash

   kb ref \
       -k 63 \
       --d-list $(gget ref --ftp -w dna homo_sapiens) \
       --workflow standard \
       -i index.idx \
       -g t2g.txt \
       -f1 fasta.fa \
       $(gget ref --ftp -w dna,gtf homo_sapiens)

5. Align and quantify sequencing reads:

.. code-block:: bash

   kb count \
       --long \
       -i index.idx \
       -g t2g.txt \
       --parity single \
       --tcc \
       --matrix-to-directories \
       -x '0,0,0:1,0,0:2,0,0' \
       $sample_barcode.fastq.gz $sample_umi.fastq.gz $sample_bioseq.fastq.gz
