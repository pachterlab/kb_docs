.. _advanced-barcodes-onlist:

Barcodes on-list format
=========================

on-list
-------

In bustools, barcode error correction is performed by supplying a list of valid barcodes to ``bustools correct`` (or via the ``-w`` option in ``kb count``).  
For supported technologies, this list—referred to as an *on-list*—allows barcodes observed in reads to be matched to known barcodes with error tolerance.

The on-list is a plain text file containing one barcode per line.  
An example (first ten barcodes from the 10x Genomics 5′ v2 chemistry) is shown below:

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

.. note::

  The allowable "error tolerance" for matching barcodes to the on-list is one substitution error. However, if you would like to turn off error tolerance (i.e. only permit perfect barcode matches), you can use the ``--nocorrect`` option in ``bustools correct`` (or the ``--exact-barcodes`` option in ``kb count``).


For technologies like SPLiT-seq, barcodes may be split into multiple segments separated by linker sequences.  
When running ``kb count``, the linker regions are typically discarded so that only the barcode segments are extracted (see the :ref:`technologies and the -x string <technologies-section>` section for more details).

In this case, barcode correction can be applied to each segment independently using a multi-column on-list.  
For example, if three 8-bp barcodes are extracted (forming a combined 24-bp barcode), the on-list may contain three columns—one for each segment—with columns separated by one or more spaces.  
Each column is corrected separately, allowing mismatches to be resolved within each barcode fragment.

If one column has fewer barcodes than the others, remaining rows may be filled with ``-`` to indicate missing entries.

Below is an example in which the first two 8-bp barcodes are corrected using the same set of sequences, while the third is corrected using a different list:

.. code-block:: text

  GACAGTGC GACAGTGC GCCTTTCA
  GAGTTAGC GAGTTAGC ATTCTAGG
  GATGAATC GATGAATC CCTTACAT
  GCCAAGAC GCCAAGAC ACATTTGG
  -        -        CATCATCC
  -        -        CTGCTTTG
  -        -        CTAAGGGA


.. note::

  The preceding example was an excerpt from the on-list of the version 2 SPLiT-seq assay. The full on-list for this assay can be found at: :download:`splitseqv2_barcodes.txt<splitseqv2_barcodes.txt>`. For version 3, download: :download:`splitseqv3_barcodes.txt<splitseqv3_barcodes.txt>`.

.. _advanced-barcodes-replacement:

replacement list
----------------

One can specify a *barcode replacement* list (in the form of a text file) via the ``-r`` option in ``bustools count`` or ``kb count``. This will replace existing barcodes with other barcodes of your choosing. This is useful for processing assays such as SPLiT-seq wherein two different barcodes can represent the same cell.


.. tip::

  When using ``-r`` to specify a replacement list in ``kb count``, *two* count matrices will be produced: One with the original barcodes (stored in the output file ``counts_unfiltered``) and one with the replacement barcodes (stored in the output file ``counts_unfiltered_modified``.


A simple example of the replacement list file is the following, where a barcode of a certain length is replaced with another barcode of the same length:

.. code-block:: text

  ATTCGAT ATTCGAT
  TTCCGAC TTCCGAG
  CTTCCTG AGAAACC
  GAAGCTG AGGGGCC

There are more advanced ways to do replacement. For example, if you do the following:

.. code-block:: text

  CATCATCC *CATTCCTA
  CTGCTTTG *CTTCATCA
  CTAAGGGA *CCTATATC

this will tell bustools to convert the nucleotides at the end of the barcode sequence. As an example, the barcode sequence AACAACCATGAAGAGA\ **CATCATCC** will be converted into AACAACCATGAAGAGA\ **CATTCCTA**. (If you wanted to convert the nucleotides at the beginning of the barcode sequence, you would put the ``*`` at the end rather than at the beginning of the replacement barcodes in the second column).

.. note::

  See the full replacement list for the SPLiT-seq assay version 2 here: :download:`splitseqv2_replace.txt<splitseqv2_replace.txt>`, which converts the random hexamer barcodes (first column of the file) into their oligo-dT counterparts (second column). For version 3, download: :download:`splitseqv3_replace.txt<splitseqv3_replace.txt>`.
