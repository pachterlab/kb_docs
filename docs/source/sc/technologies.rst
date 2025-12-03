.. _technologies-section:

Technologies and the ``-x`` string
===============================

This section describes how to configure ``kb count`` to process sequencing reads according to the assay that produced them. Because each sequencing technology uses its own read structure—differing in barcodes, strandedness, and parity—kb-python requires the user to supply technology-specific specifications so the reads are interpreted correctly.


``-x`` string
^^^^^^^^^

A **technology string** for a particular type of assay can be supplied via the ``-x`` option. The technology string can be specified in one of three ways:

* Specify the technology directly using ``-x NAME`` if it is included in kb-python's list of predefined technologies (viewable with ``kb --list``).

* Define a custom technology string that specifies the positions of the barcodes, UMIs, and the biological read sequence to be mapped (see below).


.. admonition:: Custom technology string

  The **custom** technology string (supplied to ``-x``) has the format ``barcode:UMI:DNA``, representing the locational information of the barcode, UMI, and the DNA (where DNA is the biological read to be mapped):

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

  Sequences can be stitched together by specifying multiple locations. For example, instead of a single, continuous cell barcode, the **SPLiT-seq** assay generates three separate unlinked cell barcodes. A SPLiT-seq technology string would look as follows:

  .. code-block:: text

    -x 1,10,18,1,48,56,1,78,86:1,0,10:0,0,0

  .. tip::
    If the paired-end read mapping option ``parity=paired`` is enabled, exactly two DNA locations should be specified (for the first and second read in the pair).

  If a technology does not fit into this format (e.g. due to barcodes or UMIs of variable lengths and positions), preprocessing of the FASTQ file should be performed beforehand to reformat the reads into a structure that can be handled by this format.

* Finally, the tool **seqspec** can generate custom technology strings based on the assay specifications provided to it. Please see the section, :ref:`seqspec<seqspec intro>`, for details.

strandedness
^^^^^^^^^^^^

One uses the ``--strand`` option to specify how a read should be mapped in terms of strand orientation.

* ``--strand=forward``: If a read (or the first read in the case of paired-end reads) is to be mapped in forward orientation.
* ``--strand=reverse``: If a read (or the first read in the case of paired-end reads) is to be mapped in reverse orientation.
* ``--strand=unstranded``: If one does not want to map reads with strand-specificity.


If a predefined name is used in the technology string ``-x`` option (option 1), then kb-python uses a default stranded option for that technology (e.g. for 10xv3, the default is *forward*); otherwise, the default is *unstranded*. Setting the ``--strand`` option explicitly will overrule the default option.

  .. tip::
    If very few reads are being mapped, sometimes it's because the specified ``--strand`` setting is incorrect (or the default stranded option for the technology is incorrect and needs to be overwritten explicitly by setting the correct ``--strand`` option). 

parity
^^^^^^

Using the ``--parity`` option:

If the technology involves two biological read files that are derived from paired-end sequencing (as is the case with **Smartseq2** and **Smartseq3** and many bulk RNA sequencing kits), one should specify ``--parity=paired`` to perform mapping that takes into account the fact that the reads are paired-end. Otherwise, one can specify ``--parity=single``. If a predefined name is used in the ``-x`` technology string option, then kb-python uses the default parity option for that technology (e.g for ``-x Smartseq2``, the option ``--parity=paired`` is already enabled by default).

on-list
^^^^^^^

Using the ``-w`` option:

For single-cell and single-nucleus sequencing assays, barcodes are used to identify each cell or nucleus. The **on-list** of barcodes represents the known barcode sequences that are included in the assay. Barcodes extracted from the sequencing reads will be error-tolerantly mapped to this list in a process known as *barcode error correction*. 

The on-list filename can be specified with the ``-w`` option in kb count (e.g. ``-w onlist_file.txt``. It can also be obtained by :ref:`seqspec<seqspec intro>`. If an on-list is not provided or cannot be found for the given technology, then an on-list is created by bustools via the :ref:`bustools allowlist<bustoolsbarcodes>` command which identifies repeating barcodes in sequencing reads. 

If the technology does not include cell barcodes (as is the case in bulk RNA-seq), the on-list option is irrelevant and no barcode processing occurs. This should be the case for assays that don’t include cell/nuclei barcodes. Skipping barcode error correction can also be done by specifying ``-w None``. If a predefined name is used in the ``-x`` technology string option, then kb-python uses the default on-list option for that technology.

For more information on the on-list format, see the :ref:`barcodes on-list format<advanced-barcodes-onlist>` section.

replacement list
^^^^^^^^^^^^^^^^^^^^
**SPLiT-seq** (or **Parse Biosciences Evercode WT**) uses a combinatorial barcoding strategy where multiple rounds of barcoding are used to label cells. In some cases, the same barcode may be used in different rounds of barcoding. To disambiguate these barcodes, one can provide a **replacement list** file via the ``-r`` option. 

The replacement list should contain two columns: 

- **Column 1**: the original barcode sequence
- **Column 2**: the replacement barcode sequence 

During processing, any barcode that matches an entry in the first column will be replaced with the corresponding entry from the second column. This ensures that each barcode is unique and can be accurately associated with a specific cell or nucleus.

For more information on the replacement list format, see **replacement list** in the :ref:`barcodes on-list format<advanced-barcodes-replacement>` section.





