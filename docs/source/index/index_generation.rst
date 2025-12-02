.. _index-generation:

Generate a reference index
=====================

To pseudoalign RNA-seq reads with kallisto, a reference index must first be built from a set of 
*target sequences*. In most standard analyses, 
these target sequences are transcript annotations, where each target corresponds to a single transcript.

kb-python provides an interface for constructing kallisto indices via the ``kb ref`` command. 
The type of index generated is determined by the ``--workflow`` argument:

- ``--workflow=standard`` *(default)* — builds an index for bulk or single-cell RNA-seq quantification  
- ``--workflow=nac`` — builds an index suitable for single-nucleus RNA-seq or for analyses distinguishing nascent and mature RNA
- ``--workflow=kite`` — builds an index for feature barcoding experiments (e.g. CRISPR screens or antibody tags)
- ``--workflow=custom`` — builds an index directly from a set of target sequences

By selecting the appropriate workflow, users can generate reference indices tailored to their assay and downstream analytical goals.

.. _downloading-a-premade-index:

Downloading a premade index
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oftentimes, it is easy to simply download an index that has already been made.

To download a mouse index for bulk and single-cell RNA-seq (i.e. the **standard** workflow), run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt

The files **index.idx** and **t2g.txt** will then be created.

To download a mouse index for single-nucleus RNA-seq or for analyses that require quantification of nascent and mature RNA (i.e. the **nac** workflow), run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt -c1 cdna.txt -c2 nascent.txt --workflow=nac


The files **index.idx**, **t2g.txt**, **cdna.txt**, and **nascent.txt** will then be created.

kb-python supports downloading pre-made indices for the following species:

- human
- mouse
- dog 
- monkey
- zebrafish
 
The up to date list of pre-created indices (and how they were generated) is available `here <https://github.com/pachterlab/kallisto-transcriptome-indices>`_.  

.. _making-an-index:

Making an index
^^^^^^^^^^^^^^^

To create an index via ``kb ref``, a user typically needs to specify a *genome* FASTA reference file and a GTF annotation file. These files are necessary to extract the transcript sequences (i.e. a transcriptome) that will be used to create the index. These files can be obtained from `ENSEMBL <https://useast.ensembl.org/index.html>`_ or `GENCODE <https://www.gencodegenes.org/>`_.  We recommend using the primary assembly FASTA file (in ENSEMBL, the file name for the primary assembly ends in *.dna.primary_assembly.fa.gz*). Examples for the human ENSEMBL FASTA and GTF files are the following:

* https://ftp.ensembl.org/pub/release-108/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
* https://ftp.ensembl.org/pub/release-108/gtf/homo_sapiens/Homo_sapiens.GRCh38.108.gtf.gz

.. note::
   You can specify the number of threads to ``kb ref`` via the ``-t`` option (increasing the number of threads improves processing speed, assuming that the number of CPU cores requested is available on the system). For example, to specify 12 threads, you can specify ``-t 12``. By default, 8 threads are used.

.. note::
   You can use `gget ref <https://pachterlab.github.io/gget/en/ref.html>`_ to fetch the download links for the Ensembl reference files for any species (you can also specify a specific Ensembl release):

   .. code-block:: text

      pip install gget
      gget ref -w dna,gtf homo_sapiens



The standard index type (for bulk and single-cell RNA-seq quantification)
--------------------------------------------------

Here, we'll build an index (using the *standard* workflow) for bulk and single-cell RNA-seq.

Only the FASTA file and GTF file (which we named **genome.fasta** and **genome.gtf** here) need to be supplied by the user; the other files are output files generated as part of the indexing process and may be necessary for the subsequent mapping and quantification step.

.. code-block:: text

   kb ref \
      -i index.idx \
      -g t2g.txt \
      -f1 cdna.fasta \
      genome.fasta genome.gtf

You can also use `gget ref <https://pachterlab.github.io/gget/en/ref.html>`_ to pass the Ensembl download links to ``kb ref`` directly, in which case the user only needs to supply the species name:

.. code-block:: text

   kb ref \
      -i index.idx \
      -g t2g.txt \
      -f1 cdna.fasta \
      $(gget ref --ftp -w dna,gtf homo_sapiens)

Running ``kb ref --workflow=standard`` will generate three files:

- **index.idx:**  
  Contains the kallisto index used for pseudoalignment and quantification.

- **t2g.txt:**  
  A transcript-to-gene mapping file, linking each transcript in the index to its corresponding gene.

- **cdna.fasta:**  
  A FASTA file containing the transcript sequences extracted from the input genome FASTA and GTF.  
  This file is *not required* in downstream steps, but is useful to keep as a reference.

The nac index type (for single-nucleus RNA-seq or nascent/mature RNA quantification)
----------------------------------------------------------------------------------


Here, we'll build an index (using the *nac* workflow) for single-nucleus RNA-seq or nascent/mature RNA quantification.

Only the FASTA file and GTF file (which we named **genome.fasta** and **genome.gtf** here) need to be supplied by the user; the other files are output files generated as part of the indexing process and may be necessary for the subsequent mapping and quantification step.

.. code-block:: text

   kb ref --workflow=nac -i index.idx -g t2g.txt -c1 cdna.txt -c2 nascent.txt \
   -f1 cdna.fasta -f2 nascent.fasta genome.fasta genome.gtf


Running ``kb ref --workflow=nac`` will generate six files:

- **index.idx:**  
  The kallisto index used for pseudoalignment and quantification.

- **t2g.txt:**  
  A transcript–gene mapping file linking each transcript in the index to its corresponding gene.

- **cdna.txt:**  
  Contains identifiers for *mature* (cDNA) transcript sequences.

- **nascent.txt:**  
  Contains identifiers for *nascent* transcript sequences.

- **cdna.fasta:**  
  A FASTA file containing sequences that make up the mature transcriptome  
  (i.e. spliced transcript sequences).

- **nascent.fasta:**  
  A FASTA file containing sequences for the nascent transcriptome  
  (i.e. full gene sequences including all exons and introns).

Both ``cdna.fasta`` and ``nascent.fasta`` are not required for downstream processing,  
but may be useful to retain for reference.

Advanced
^^^^^^^^


kallisto
--------

As ``kb ref`` invokes the ``kallisto index`` command, the kallisto commands associated with each ``kb ref`` call can be viewed by specifying ``--dry-run`` to kb ref or by specifying ``--verbose`` when building an index with kb ref. For more details, see the :ref:`kallisto index` section of the kallisto manual.

Selecting GTF entries
---------------------

You can use the ``--include-attribute`` or ``--exclude-attribute`` to include or exclude certain entries from the GTF file. For example, to only include protein-coding genes and lncRNAs/lincRNAs when making an index:

.. code-block:: text

   kb ref -i index.idx -g t2g.txt -f1 cdna.fasta \
   --include-attribute gene_biotype:protein_coding \
   --include-attribute gene_biotype:lncRNA \
   --include-attribute gene_biotype:lincRNA \
   genome.fasta genome.gtf

Note that the ``--include-attribute`` and ``--exclude-attribute`` options take in a **KEY:VALUE** pair.
In the above example, the key is **gene_biotype** and the values are **protein_coding**, **lncRNA**, and **lincRNA**.
The indexes will then only include transcripts whose gene_biotype attribute in the GTF file matches one of the specified values.

The D-list
----------

The D-list provides a mechanism for *background filtering* during index construction.  
It ensures that reads originating from outside the indexed target sequences are removed rather than incorrectly assigned to a target.

If ``--d-list`` is not specified, ``kb ref`` defaults to the input genome FASTA  
(equivalent to ``--d-list=genome.fasta``). This prevents reads derived from unindexed
regions of the genome from being assigned to transcript targets.  
Users may provide a custom D-list using ``--d-list <file>`` or disable background filtering entirely by setting ``--d-list=None``.

By default, only **distinguishing flanking k-mers** (DFKs) are filtered.  
DFKs are k-mers that occur immediately upstream or downstream of a transcript boundary.  
Reads aligning to DFKs are likely to extend beyond the transcript itself, and therefore represent signal originating from outside the intended target space.

To filter *all* k-mers from a sequence rather than only the flanking ones, provide the sequence in the D-list FASTA file **without a header**.  
In this case, the entire sequence is treated as background and all of its k-mers are excluded.  
If a header is present, only DFKs will be filtered.


.. code-block:: text

   >
   ACGCGACATAGCAGACTAGACATTATTTACGTATTATGATAGTAGAT


A custom index
--------------

In addition to the ``standard`` and ``nac`` workflows, kb-python also supports a 
``custom`` workflow via ``--workflow=custom``. This option allows you to build a 
kallisto index directly from a set of provided target sequences, rather than 
extracting them from a reference FASTA and GTF annotation. This is useful when 
working with non-standard references, custom transcriptomes, or other sequence 
collections.

Example (with target sequences stored in ``custom.fasta``):

.. code-block:: text

   kb ref --workflow=custom -i index.idx custom.fasta

You can also index k-mers associated with sets of disjoint sequences. This is useful for mapping against genetic polymorphisms (where there exist multiple variants for each transcript). This is possible by specifying ``--distinguish`` in ``--workflow=custom``. 

.. code-block:: text

   kb ref --workflow=custom -i index.idx --distinguish custom.fasta

For the ``--distinguish`` option, the custom.fasta should be organized such that the target names in the input FASTA file are numbers (specifically, zero-indexed numerical identifiers).  An example custom.fasta file (with 3 targets) would look like:

.. code-block:: text

   >0
   ACTCTATCATCATCTACTACTACTCGCAGCGACGACATCAGCTTTTTT
   >1
   GCGCGCCGCCGACGACACGCAGAGAAGAAAGCGCGACGAC
   >2
   TTATGTGTCGTGTAGTCGTAGTGTGTCGTGCCGCCGCGCGCAAA
   >2
   ATATACGATCATCAGCGACAGACTACTTCAGAAGACTATCA
   >0
   GTCGATCGGTGTCACATGCGCAAGCGTCAGCGACACGACTTCGG


