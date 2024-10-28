Pseudoalignment of bulk long read RNA seq data
=======================================
.. note:: **Reference:**
   Loving, R, Sullivan, DK, Reese, F, Rebboah, E, Sakr, J, Rezaie, N, Liang, HY, Filimban, G, Kawauchi, S, Oakes, C, Trout, D, Williams, BA, MacGregor, G, Wold, BJ, Mortazavi, A, Pachter, L 
   `Long-read sequencing transcriptome quantification with lr-kallisto. <https://doi.org/10.1101/2024.07.19.604364>`_  
   bioRxiv 2024.07.19.604364
   https://doi.org/10.1101/2024.07.19.604364

kallisto can perform long-read pseudoalignment of nucleotide sequences against a large *k*-mer reference while retaining single-cell (for single-cell RNA sequencing data) or sample (for bulk RNA seq data) resolution. To perform long-read pseudoalignment, first add ``-k 63`` to ``kb ref`` and, second, add the ``--long`` flag to the ``kb count`` commands.

Long-read pseudoalignment is performed by the longer k-mer length improving the quality of mapping k-mers in the higher sequencing error rates (relative to short read sequencing), making it more probable that the read originates from the transcript compatibility class it maps to. As k increases, the number of distinct k-mers also increases, but the number of contigs decreases. This implies that the number of transcripts in a transcript compatibility class decreases on average with increasing length of k. Overall, the complexity of the T-DBG decreases (Supplementary Fig. 5), increasing the probability of the read originating from the transcript compatibility class it is mapping to. Furthermore, this also increases the probability of the intersection of equivalence classes being nonempty, which increases the overall mapping rate.

The workflow can be executed in three lines of code, and computational requirements do not exceed those of a standard laptop. Building on kallisto’s versatility, the workflow is compatible with all state-of-the-art single-cell and bulk RNA sequencing methods, including but not limited to SMART-Seq [4]_ and SPLiT-Seq [5]_ (including Parse Biosciences) and performance is state-of-the-art on both PacBio and Oxford Nanopore Technologies long-read data.

The long-read pseudoalignment workflows can be used to align RNA sequencing data to any transcriptome reference:

1. Install `kb-python` (optional: install `gget <https://github.com/pachterlab/gget>`_ to fetch the host genome and transcriptome):

.. code-block:: bash

   pip install kb-python gget

2. Create reference index (using the D-list of human genome):

.. code-block:: bash

   kb ref \
       -k 63 \
       --d-list $(gget ref --ftp -w dna homo_sapiens) \
       -i index.idx --workflow standard \
       -g t2g.txt -f1 fasta.fa \
       $(gget ref --ftp -w dna,gtf homo_sapiens)

3. Align and quantify sequencing reads:

.. code-block:: bash

   kb count \
       --long \
       -i index.idx -g homo_t2g.txt \
       --parity single \
       --tcc --matrix-to-directories 
       -x bulk \
       $USER_DATA.fastq.gz
