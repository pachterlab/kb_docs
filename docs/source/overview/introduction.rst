Introduction
===============

The tools:

* **`kallisto <https://github.com/pachterlab/kallisto>`_**: Maps RNA-seq reads to a reference transcriptome and stores the results in a BUS file.

* **`bustools <https://github.com/BUStools/bustools>`_**: Processes the results in the BUS file to correct barcodes, deduplicate UMIs, and generate quantification files (e.g. count matrices).

* **`kb-python <https://github.com/pachterlab/kb_python>`_**: A wrapper around kallisto and bustools that facilitates usage of those tools and facilitates the generation of a reference transcriptome. The kallisto and bustools binaries come packaged in kb-python.

Background
^^^^^^^^

Once upon a time, kallisto and bustools decided to join forces...

A paper describing the protocols is available here:

* `Protocols Manual <https://www.biorxiv.org/content/10.1101/2023.11.21.568164v2.full.pdf>`_
* `Supplementary Manual <https://www.biorxiv.org/content/biorxiv/early/2024/01/23/2023.11.21.568164/DC1/embed/media-1.pdf>`_


.. seealso::

   If you want to know how to cite kallisto, bustools, and/or kb-python, please visit the section :ref:`Overview:References`.
