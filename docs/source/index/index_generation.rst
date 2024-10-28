Generate a reference index
=====================

To process RNA-seq reads, one must first use kallisto to build an **index** from a set of sequences, referred to as targets, representing the set of sequences that the sequencing reads can be mapped to. In a standard analysis, these targets are usually transcript sequences (i.e., each individual target corresponds to one transcript). 

**kb-python** enables the construction of kallisto indices through the ``kb ref`` command (Fig. 1). Different types of kallisto indices can be built by specifying the ``--workflow`` argument in kb ref, which selects the type of index to be constructed. The default is ``--workflow=standard``, which creates an index suitable for bulk and single-cell RNA-seq quantification. Specifying ``--workflow=nac`` should be used for quantifying single-nucleus RNA-seq or nascent/mature RNA species.

Downloading a premade index
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oftentimes, it is easy to simply download an index that has already been made.

To download a mouse index for bulk and single-cell RNA-seq (i.e. the **standard** workflow), one can run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt

The files **index.idx** and **t2g.txt** will then be created.

To download a mouse index for single-nucleus RNA-seq or for analyses that require quantification of nascent and mature RNA (i.e. the **nac** workflow), one can run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt -c1 cdna.txt -c2 nascent.txt --workflow=nac


The files **index.idx**, **t2g.txt**, **cdna.txt**, and **nascent.txt** will then be created.

One can replace *mouse* with *human* (or another species). A comprehensive list of pre-created indices (and how they were generated) is available `here <https://github.com/pachterlab/kallisto-transcriptome-indices>`_.  




Making an index
^^^^^^^^^^^^^^^

To create an index via ``kb ref``, a user typically needs to specify a FASTA reference file and a GTF annotation file. These files can be obtained from `ENSEMBL <https://useast.ensembl.org/index.html>`_ or `GENCODE <https://www.gencodegenes.org/>`_.  We recommend using the primary assembly FASTA file (in ENSEMBL, the file name for the primary assembly ends in *.dna.primary_assembly.fa.gz*). Examples for the mouse ENSEMBL FASTA and GTF files are the following:

* https://ftp.ensembl.org/pub/release-108/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
* https://ftp.ensembl.org/pub/release-108/gtf/homo_sapiens/Homo_sapiens.GRCh38.108.gtf.gz

Note: One can specify the number of threads to ``kb ref`` via the ``-t`` option (increasing the number of threads improves processing speed, assuming that the number of CPU cores requested is available on the system). For example, to specify 12 threads, one can specify ``-t 12``. By default, 8 threads are used.


The standard index type (bulk and single-cell RNA-seq)
--------------------------------------------------

Here, we'll build an index (using the *standard* workflow) for bulk and single-cell RNA-seq.

Only the FASTA file and GTF file (which we named **genome.fasta** and **genome.gtf** here) need to be supplied by the user; the other files are output files generated as part of the indexing process and may be necessary for the subsequent mapping and quantification step.

.. code-block:: text

   kb ref -i index.idx -g t2g.txt -f1 cdna.fasta genome.fasta genome.gtf


The files **index.idx**, **t2g.txt**, **cdna.fasta** will then be created. The index.idx file contains the kallisto index while the t2g.txt file is a text file containing a mapping between transcripts and genes. The cdna.fasta file is not used in subsequent steps (but is useful for reference); it simply contains the individual transcript sequences that comprise the transcriptome that are extracted from the genome FASTA and GTF and indexed by kallisto.


The nac index type (single-nucleus RNA-seq or nascent/mature RNA quantification)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here, we'll build an index (using the *standard* workflow) for single-nucleus RNA-seq or nascent/mature RNA quantification.

Only the FASTA file and GTF file (which we named **genome.fasta** and **genome.gtf** here) need to be supplied by the user; the other files are output files generated as part of the indexing process and may be necessary for the subsequent mapping and quantification step.

.. code-block:: text

   kb ref --workflow=nac -i index.idx -g t2g.txt -c1 cdna.txt -c2 nascent.txt \
   -f1 cdna.fasta -f2 nascent.fasta genome.fasta genome.gtf


The files **index.idx**, **t2g.txt**, **cdna.txt**, **nascent.txt**, **cdna.fasta**, and **nascent.fasta** will then be created. The index.idx file contains the kallisto index while the t2g.txt file is a text file containing a mapping between transcripts and genes. The cdna.txt file contains the identifiers of the "mature" (i.e. cDNA) sequences while the nascent.txt file contains the identifiers of the "nascent" sequences.  The cdna.fasta and nascent.fasta files are not used in subsequent steps (but are useful for reference); they contain the sequences that comprise the "mature" transcriptome and the "nascent" transcriptome that are extracted from the genome FASTA and GTF and indexed by kallisto. The "mature" transcriptome is simply the transcript sequences while the "nascent" transcriptome are the full length gene sequences (i.e. all exons and all introns that make up the gene). 


