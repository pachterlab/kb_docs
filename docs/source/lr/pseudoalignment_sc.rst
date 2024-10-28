Pseudoalignment of single-cell long read RNA seq data
=======================================
.. note:: **Reference:**
   Loving, R, Sullivan, DK, Reese, F, Rebboah, E, Sakr, J, Rezaie, N, Liang, HY, Filimban, G, Kawauchi, S, Oakes, C, Trout, D, Williams, BA, MacGregor, G, Wold, BJ, Mortazavi, A, Pachter, L 
   `Long-read sequencing transcriptome quantification with lr-kallisto. <https://doi.org/10.1101/2024.07.19.604364>`_  
   bioRxiv 2024.07.19.604364
   https://doi.org/10.1101/2024.07.19.604364

kallisto can perform long-read pseudoalignment of nucleotide sequences against a large *k*-mer reference while retaining single-cell (for single-cell RNA sequencing data) or sample (for bulk RNA seq data) resolution. To perform long-read pseudoalignment, first add ``-k 63`` to ``kb ref`` and, second, add the ``--long`` flag to the ``kb count`` commands.

Long-read pseudoalignment is performed by the longer k-mer length improving the quality of mapping k-mers in the higher sequencing error rates (relative to short read sequencing), making it more probable that the read originates from the transcript compatibility class it maps to. As k increases, the number of distinct k-mers also increases, but the number of contigs decreases. This implies that the number of transcripts in a transcript compatibility class decreases on average with increasing length of k. Overall, the complexity of the T-DBG decreases (Supplementary Fig. 5), increasing the probability of the read originating from the transcript compatibility class it is mapping to. Furthermore, this also increases the probability of the intersection of equivalence classes being nonempty, which increases the overall mapping rate.

The workflow can be executed in three lines of code, and computational requirements do not exceed those of a standard laptop. Building on kallisto’s versatility, the workflow is compatible with all state-of-the-art single-cell and bulk RNA sequencing methods, including but not limited to SMART-Seq [add citation]_ and SPLiT-Seq [add citation]_ (including Parse Biosciences) and performance is state-of-the-art on both PacBio and Oxford Nanopore Technologies long-read data.

.. note:: For long-read single-cell data to be processed with lr-kallisto some preprocessing steps are required. Here we present the use of seqspec and splitcode to facilitate an automated processing of LR-SPLiT-Seq [add citation]_. seqspec is used to create a configuration file for splitcode to extract barcodes, umis, and the biological sequences from the reads. seqspec requires as input a machine readable specification file for the sample protocol that is in the seqspec format. splitcode can then be called on the reads with the configuration file created by seqspec to extract from the reads the barcodes, umis, and biological sequences. The output of splitcode can be piped directly into lr-kallisto or output to files that are processed with lr-kallisto.  

The long-read pseudoalignment workflows can be used to align RNA sequencing data to any transcriptome reference:

1. Install `kb-python` (optional: install `gget <https://github.com/pachterlab/gget>`_ to fetch the host genome and transcriptome) as well as seqspec and splitcode:

.. code-block:: bash

   pip install kb-python gget git+https://github.com/pachterlab/seqspec 
   git clone https://github.com/pachterlab/splitcode
   cd splitcode
   mkdir build
   cd build
   cmake ..
   make
   make install

2. Create splitcode config file using seqspec:

.. code-block:: bash 
  
  seqspec index -m rna -s file -t splitcode spec.yaml > seqspec-config.txt

3. Use splitcode to extract barcodes, umis, and biological sequences:

.. code-block:: bash 

  splitcode -c seqspec-config.txt $sample_data.fastq.gz -o $sample_data_modified.fastq.gz -t 32

4. Importantly, the extracted sequences may need reorienting for the sample to be processed appropriately; we give an example of this in the case of ONT single-nuclei samples in the tutorials. 

5. Create reference index (using the D-list of human genome):

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
       -x '0,0,0:1,0,0:2,0,0' \
       $sample_barcode.fastq.gz $sample_umi.fastq.gz $sample_bioseq.fastq.gz
