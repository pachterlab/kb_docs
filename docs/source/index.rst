kallisto | bustools
===================

*kallisto*, *bustools*, and *kb-python* are free, open-source tools used
together to perform fast, lightweight RNA-seq quantification and preprocessing. 
These tools support the analysis of both **bulk** and **single-cell RNA-seq**
data.

**kallisto** performs *pseudoalignment*, a method that assigns reads to
transcripts without fully aligning them. This enables extremely fast and
accurate transcript quantification.

**bustools** processes barcode and UMI information and provides utilities
for manipulating BUS files, a compact representation of barcodes, UMIs,
and transcript equivalence classes.

**kb-python** offers high-level workflows that automate common tasks
using kallisto and bustools, including reference generation and the
processing of both bulk and single-cell RNA-seq experiments. It
automatically handles downloading and formatting reference transcriptomes,
manages file organization, and ensures that kallisto and bustools are
invoked with consistent parameters.

You may run kallisto and bustools directly, or use kb-python to streamline
complete workflows. Many users benefit from the convenience and reproducibility
provided by kb-python, especially for multi-step analyses.


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

   lr/pseudoalignment
   lr/tutorials

.. toctree::
   :maxdepth: 2
   :caption: Translated alignment:

   translated/pseudoalignment
   translated/tutorials

.. toctree::
   :maxdepth: 2
   :caption: seqspec:

   seqspec/introduction

.. toctree::
   :maxdepth: 1
   :caption: Troubleshooting:

   troubleshooting/troubleshooting.rst

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

