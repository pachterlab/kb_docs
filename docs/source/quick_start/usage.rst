The kb-python workflow
======================

kb-python provides four analysis workflows. What you use depends on the assay and your
quantification goals:

- **standard** — typical workflow for most single-cell or bulk RNA-seq experiments (default)
- **nac** — separates nascent and mature RNA; recommended for single-nucleus data
- **kite** — for feature barcoding experiments (e.g. CRISPR screens or antibody tags)
- **custom** — for quantifying non-standard target sequences (or targets supplied directly by the user)

Each workflow modifies how indices are built and how counts are computed, but
the command structure remains the same across all of them.


Core commands
-------------

Two kb-python commands cover nearly all use cases:

1. ``kb ref`` — builds (or downloads) a reference index
2. ``kb count`` — maps reads and performs quantification

The workflow is selected using the ``--workflow`` argument with both commands:

.. code-block:: shell

   kb ref --workflow nac ...
   kb count --workflow nac ...

If not specified, kb-python defaults to the **standard** workflow.


Minimal workflow structure
--------------------------

A typical processing pipeline is simply:

.. code-block:: shell

   kb ref ...
   kb count ...

These two commands wrap a sequence of kallisto and bustools operations:

.. code-block:: shell

   # kb ref
   kallisto index ...

   # kb count
   kallisto bus ...
   bustools inspect ...
   bustools correct ...
   bustools sort ...
   bustools count ...


Output files
------------

For single cell RNA-seq, ``kb count`` produces one or more count matrix files suitable for downstream
analysis:

- **.mtx** — sparse matrix format compatible with most analysis frameworks
- **.h5ad** (with ``--h5ad``) — loads directly into Python workflows such as Scanpy
- **.loom** (with ``--loom``) — interoperable with both R and Python tools

These files represent gene-level (or TCC-level, if configured) counts
extracted using the specified workflow.

For bulk RNA-seq, ``kb count`` produces gene-level (or TCC-level) abundance files
in TSV and H5 format, similar to kallisto's standard output, in addition to the count matrix files.

Tutorials
----------------
For step-by-step instructions on producing a reference index with ``kb ref``, see :ref:`generate a reference Index <index-generation>` .

The particular usage of ``kb count`` depends on the type of data being analyzed and your analysis goals:

- For single-cell RNA-seq data, see :ref:`pseudoalignment of single-cell rna seq data <single-cell-rna-seq>`. 
- For bulk RNA-seq data, see :ref:`bulk RNA-seq <bulk-rna-seq>`.
- To perform long read pseudoalignment of RNA-seq data, see :ref:`long read pseudoalignment of bulk RNA seq data <lr-bulk-rna-seq>`  or :ref:`long read pseudoalignment of single-cell RNA seq data <lr-sc-rna-seq>`.
- To align RNA-seq data against a protein or amino acid reference, see :ref:`pseudoalignment of RNA seq data against a protein reference <translated-pseudoalignment>`.

Manual
---------------   
For more detailed usage instructions, please refer to the :ref:`kb-python manual <kb-usage>`.
