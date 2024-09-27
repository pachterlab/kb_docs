Barcodes "on list" format
=========================

In bustools, one supplies a list of barcodes to ``bustools correct`` for technologies that support matching barcodes within reads error-tolerantly to an external list (called an **on list**) of barcodes. The "on list" used in this *barcode error correction* process can simply be formatted as follows (example of the first 10 barcodes from 10X genomics 5′ v2 chemistry):

737K-august-2016.txt:

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

However, let's say you have something like SPLiT-seq where there are three barcodes separated by linker regions. When running ``kb count``, one typically only extracts the barcodes (not the linker regions); see  the :ref:`technologies section<sc/technologies>`_ for details. One can use an "on list" that enables correcting each of the three barcodes separately. For example, if one extracted three 8-bp barcodes (final barcode is therefore 24 bp's), one can make an "on list" of three columns (where each column is separated by one or more spaces) to correct each 8-bp portion individually. (Note that you can have a different number of barcodes in each column by simply using ``-`` after a certain column has no more rows remaining). See an example below where we error correct the first 8-bp barcode against a list of 4 sequences, the second 8-bp barcode against the same list of 4 sequences, and the third 8-bp barcode against a different list of 8-bp sequences.

.. code-block:: text

  GACAGTGC GACAGTGC GCCTTTCA
  GAGTTAGC GAGTTAGC ATTCTAGG
  GATGAATC GATGAATC CCTTACAT
  GCCAAGAC GCCAAGAC ACATTTGG
  -        -        CATCATCC
  -        -        CTGCTTTG
  -        -        CTAAGGGA

..code-block: note

  The preceding example was an excerpt of the *on list* from a SPLiT-seq assay (version 2 of the assay; note that different iterations of the technology may have different barcodes). The full *on list* that SPLiT-seq assay can be found at: :ref:`technologies section<bus_adv/splitseqv2_barcodes.txt>`_.
