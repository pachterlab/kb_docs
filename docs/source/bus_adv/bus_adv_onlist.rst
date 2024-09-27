Barcodes "on list" format
=========================

On list
=======

In bustools, one supplies a list of barcodes (in the form of a text file) to ``bustools correct`` (or to the ``-w`` option in ``kb count``) for technologies that support matching barcodes within reads error-tolerantly to an external list (called an **on list**) of barcodes. The "on list" used in this *barcode error correction* process can simply be formatted as follows (example of the first ten barcodes from 10x Genomics 5′ v2 chemistry):

.. code-block:: text

  AAACCTGAGAAACCAT
  AAACCTGAGAAACCGC
  AAACCTGAGAAACCTA
  AAACCTGAGAAACGAG
  AAACCTGAGAAACGCC
  AAACCTGAGAAAGTGG
  AAACCTGAGAACAACT
  AAACCTGAGAACAATC
  AAACCTGAGAACTCGG
  AAACCTGAGAACTGTA

However, let's say you have something like SPLiT-seq where there are three barcodes separated by linker regions. When running ``kb count``, one typically only extracts the barcodes (not the linker regions); see the :ref:`technologies section<technologies-section>` for details. One can use an "on list" that enables correcting each of the three barcodes separately. For example, if one extracted three 8-bp barcodes (final barcode is therefore 24 bp's), one can make an "on list" of three columns (where each column is separated by one or more spaces) to correct each 8-bp portion individually. (Note that you can have a different number of barcodes in each column by simply using ``-`` after a certain column has no more rows remaining). See an example below where we error correct the first 8-bp barcode against a list of 4 sequences, the second 8-bp barcode against the same list of 4 sequences, and the third 8-bp barcode against a different list of 8-bp sequences.

.. code-block:: text

  GACAGTGC GACAGTGC GCCTTTCA
  GAGTTAGC GAGTTAGC ATTCTAGG
  GATGAATC GATGAATC CCTTACAT
  GCCAAGAC GCCAAGAC ACATTTGG
  -        -        CATCATCC
  -        -        CTGCTTTG
  -        -        CTAAGGGA


.. note::

  The preceding example was an excerpt of the *on list* from a SPLiT-seq assay (version 2 of the assay; note that different iterations of the technology may have different barcodes). The full *on list* that SPLiT-seq assay can be found at: :ref:`splitseqv2_barcodes.txt<bus_adv/splitseqv2_barcodes.txt>`.


Replacement list
=================


One can specify a *barcode replacement* list (in the form of a text file) via the ``-r`` option in ``bustools count`` or ``kb count``. This will replace existing barcodes with other barcodes of your choosing. This is useful for processing assays such as SPLiT-seq wherein two different barcodes can represent the same cell.


.. tip::

  When using ``-r`` to specify a replacement list in ``kb count``, *two* count matrices will be produced: One with the original barcodes (stored in the output file ``counts_unfiltered``) and one with the replacement barcodes (stored in the output file ``counts_unfiltered_modified``.


A simple example of the replacement list file is the following, where a barcode of a certain length is replaced with another barcode of the same length.

.. code-block:: text

  ATTCGAT ATTCGAT
  TTCCGAC TTCCGAG
  CTTCCTG AGAAACC
  GAAGCTG AGGGGCC

There are more advanced ways to do replacement. For example, if one does the following:

.. code-block:: text

  CATCATCC *CATTCCTA
  CTGCTTTG *CTTCATCA
  CTAAGGGA *CCTATATC

This will tell bustools to convert the nucleotides at the end of the barcode sequence. As an example, the barcode sequence AACAACCATGAAGAGA\ **CATCATCC** will be converted into AACAACCATGAAGAGA\ **CATTCCTA**. (If one wanted to convert the nucleotides at the beginning of the barcode sequence one would put the ``*`` at the end rather than at the beginning of the replacement barcodes in the second column).

.. note::

  See the full replacement list of the SPLiT-seq assay (version 2) here: :ref:`splitseqv2_replace.txt<bus_adv/splitseqv2_replace.txt>`, which converts the random hexamer barcodes (first column of the file) into their oligo-dT counterparts (second column).
