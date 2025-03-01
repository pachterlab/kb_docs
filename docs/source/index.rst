kallisto | bustools
===================

The **kallisto**, **bustools**, and **kb-python** programs are free, open-source software tools that are used together to perform RNA-seq quantification.

* `kallisto <https://github.com/pachterlab/kallisto>`_  
   Maps RNA-seq reads to a reference transcriptome and stores the results in a BUS file.
* `bustools <https://github.com/BUStools/bustools>`_    
   Processes the results in the BUS file to correct barcodes, deduplicate UMIs, and generate quantification files (e.g. count matrices).
* `kb-python <https://github.com/pachterlab/kb_python>`_  
   A wrapper around kallisto and bustools that facilitates usage of those tools and facilitates the generation of a reference transcriptome. The kallisto and bustools binaries come packaged in kb-python.


.. note::

   This is unofficial documentation that is under active development.


.. toctree::
   :maxdepth: 1
   :caption: Overview:

   overview/introduction
   overview/references
   overview/used_by

.. toctree::
   :maxdepth: 1
   :caption: Quick Start:

   quick_start/installation
   quick_start/usage

.. toctree::
   :maxdepth: 2
   :caption: Index generation:

   index/index_generation

.. toctree::
   :maxdepth: 2
   :caption: Bulk RNA seq:

   bulk/pseudoalignment
   bulk/tutorials

.. toctree::
   :maxdepth: 2
   :caption: Single-cell RNA seq:

   sc/pseudoalignment
   sc/technologies
   sc/tutorials

.. toctree::
   :maxdepth: 2
   :caption: Long read RNA seq:

   lr/pseudoalignment_bulk
   lr/pseudoalignment_sc
   lr/tutorials

.. toctree::
   :maxdepth: 2
   :caption: Translated alignment:

   translated/pseudoalignment
   translated/tutorials

.. toctree::
   :maxdepth: 2
   :caption: Seqspec:

   seqspec/introduction

.. toctree::
   :maxdepth: 1
   :caption: Manuals:
   
   manuals/kallisto
   manuals/bustools
   manuals/kb

.. toctree::
   :maxdepth: 1
   :caption: Advanced installation:

   adv_installation/from_source
   adv_installation/releases


.. toctree::
   :maxdepth: 1
   :caption: Advanced bustools:

   bus_adv/bus_adv_onlist

.. toctree::
   :maxdepth: 1
   :caption: FAQ:

   FAQ

