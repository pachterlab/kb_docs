Technologies and the -x string
===============================

This section will cover how to tell the ``kb count`` within **kb-python** how to process sequencing data depending on the technology that produced the data. As different sequencing assays have different read structures, strandedness, parity, and barcodes, one must provide the specifications for the technology which produced the sequencing reads.


-x string
^^^^^^^^^

A **technology string** for a particular type of assay can be supplied via the ``-x`` option. The technology string can be specified in one of two ways:

* Several assays are predefined within the software (the list is viewable by calling ``kb --list``) so one can name one of those directly (e.g. one can specify ``-x 10xv3``).

* One can format their own **custom** technology string specifying the read locations of the barcodes, UMIs, and the biological sequence that is to be mapped (see below).


.. admonition:: Custom technology string

  The **custom** technology string (supplied to ``-x``) contains the format ``barcode:UMI:DNA``, representing the locational information of the barcode, UMI, and the DNA (where DNA is the biological read to be mapped):

  .. code-block:: text

    -x a,b,c:d,e,f:g,h,i

  * **a**: barcode file number, **b**: barcode start position, **c**: barcode end position
  * **d**: UMI file number, **e**: UMI start position, **f**: UMI end position
  * **g**: DNA file number, **h**: DNA start position, **i**: DNA end position

  .. important::
    File numbers and positions are zero-indexed. If no specific end position exists (i.e. the end position is the very end of the read), the end position should be set to **0**. If cell barcodes and/or UMIs are not supported by the technology, the barcode and/or UMI field can be set to ``-1,0,0``.

  An example for **10xv3** (10x Genomics, version 3 chemistry):

  .. code-block:: text

    -x 0,0,16:0,16,28:1,0,0

  Sequences can be stitched together by specifying multiple locations; for example, a SPLiT-seq assay, which contains three separate unlinked barcodes, each of length 8, and a UMI of length 10 in the second file and the DNA in the first file would look as follows:

  .. code-block:: text

    -x 1,10,18,1,48,56,1,78,86:1,0,10:0,0,0

  .. tip::
    For multiple locations: If the paired-end read mapping option is enabled, exactly two DNA locations should be specified (for the first and second read in the pair).

  If a technology does not fit into this format (e.g. due to barcodes or UMIs of variable lengths and positions), preprocessing of the FASTQ file should be performed beforehand to reformat the reads into a structure that can be handled by this format.

* Finally, ``seqspec`` can generate custom technology strings based on the assay specifications provided to it. Please see the section, :ref:`Using seqspec`, for details.

