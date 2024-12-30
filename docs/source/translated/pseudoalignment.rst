Pseudoalignment of RNA seq data against a protein reference
=======================================

.. note:: **Reference:**
   Luebbert L, Sullivan DK, Carilli M, Eldjárn Hjörleifsson K, Viloria Winnett A, Chari T, Pachter L.  
   `Efficient and accurate detection of viral sequences at single-cell resolution reveals putative novel viruses perturbing host gene expression. <https://doi.org/10.1101/2023.12.11.571168>`_  
   *bioRxiv* 2023.12.11.571168  
   https://doi.org/10.1101/2023.12.11.571168

kallisto can perform translated pseudoalignment of nucleotide sequences against an amino acid reference while retaining single-cell (for single-cell RNA sequencing data) or sample (for bulk RNA seq data) resolution. Generally, to perform translated alignment, **simply add the ``--aa`` flag to the ``kb ref`` and ``kb count`` commands**.

The workflow can be executed in three lines of code, and computational requirements do not exceed those of a standard laptop. Building on kallisto’s versatility, the workflow is compatible with all state-of-the-art single-cell and bulk RNA sequencing methods, including but not limited to 10x Genomics, Drop-Seq, SMART-Seq, SPLiT-Seq (including Parse Biosciences), and spatial methods such as Visium.

The translated alignment workflows can be used to **align RNA sequencing data to any protein reference.** However, we first described its use in combination with the `PalmDB viral protein database <https://github.com/ababaian/palmdb>`_ for the detection of viral sequences in RNA sequencing data:

1. Install `kb-python` (optional: install `gget <https://github.com/pachterlab/gget>`_ to fetch the host genome and transcriptome):

.. code-block:: bash

   pip install kb-python gget

2. Download optimized PalmDB viral protein reference files:

.. code-block:: bash

   wget https://raw.githubusercontent.com/pachterlab/LSCHWCP_2023/main/PalmDB/palmdb_rdrp_seqs.fa
   wget https://raw.githubusercontent.com/pachterlab/LSCHWCP_2023/main/PalmDB/palmdb_clustered_t2g.txt

3. Create reference index (optional masking of the host, here human, genome using the D-list):

.. code-block:: bash

   # Single-thread runtime: 1.5 h; Max RAM: 4.4 GB; Size of generated index: 593 MB
   # Without D-list: Single-thread runtime: 3.5 min; Max RAM: 3.9 GB; Size of generated index: 592 MB
   kb ref \
       --aa \
       --d-list $(gget ref --ftp -w dna homo_sapiens) \
       -i index.idx \
       --workflow custom \
       palmdb_rdrp_seqs.fa

4. Align sequencing reads:

.. code-block:: bash

   # Single-thread runtime: 1.5 min / 1 million sequences; Max RAM: 2.1 GB
   kb count \
       --aa \
       -i index.idx \
       -g palmdb_clustered_t2g.txt \
       --parity single \
       -x default \
       $USER_DATA.fastq.gz


.. image:: ../../figures/translated_alignment_overview.png
   :width: 800px
   :alt: Overview of translated alignment workflow

`Tutorials <https://kallisto.readthedocs.io/en/latest/translated/tutorials.html>`_
^^^^^^^^^^
