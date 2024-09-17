Frequently asked questions
==========================

.. contents::
   :local:
   
.. _FAQ installation questions:

Installation questions
----------------------

.. _FAQ illegal instruction:

I run kb ref or kb count and kallisto is giving me an illegal instruction (SIGILL) error. How do I fix this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is because the kallisto binary is unfortunately incompatible with your system. This means you must follow the instructions to install kallisto from source. You can then run kb-python as follows:

::

 kb ref --kallisto=/path/to/kallisto ...
 kb count --kallisto=/path/to/kallisto ...

.. _FAQ incompatible index:

When loading in an index using kallisto or kb count, I'm getting either an "incompatible indices" error or a segmentation fault (SIGSEGV). How do I fix this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different versions of kallisto use different index formats. You either need to use a different version of kallisto or create a new index using your current version.


What version of kallisto, bustools, and kb-python should I install?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We always recommend installing the newest version unless you have a specific reason not to. The newest version of those tools contains the newest features that may not be present in older versions. The protocols paper published alongside this documentation in 2024 correspond to kb-python version 0.28.2, kallisto 0.50.1, and bustools 0.43.2, and all options and workflows present in that paper will work with those versions. As these tools develop, additional features are added and it would be necessary to use more recent versions in order to utilize those features. The installation instructions show you how to install the latest version of these tools or specific versions of these tools.

Choice of index and output matrices
-----------------------------------

When should I use the standard index type versus the nac index type?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The standard index type does not contain introns, however is much more lightweight (lower memory usage and runtime). For conventional single-cell RNA-seq quantification, the standard index type is all you need. However, whenever you need to work with nascent transcripts, then you must use the nac index type. This arises when you use biophysical models that jointly model nascent and mature RNA species, quantify single-nucleus RNA-seq data, or want to incorporate intron-containing reads into your single-cell RNA-seq quantification.

When using the nac index type, what matrix should I use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


It depends. When using the nac index type, three matrices are produce: nascent (N), mature (M), and ambiguous (A) matrices. The M+A matrix corresponds to the matrix that you get from running the standard index type. When jointly modeling nascent and mature species in biophysical models, we use the M+A matrix for the "mature" species and the N matrix for our nascent matrix. It is straightforward to directly obtain the M+A (and other matrices added up) by using --sum=total in kb count; the M+A matrix would be the matrix ending in .cell.mtx. For single-nucleus RNA-seq, you can the matrix ending in .nucleus.mtx (N+A) or, if you need to include splice junction spanning reads in your quantification, you can use the total matrix (N+M+A). The total matrix (N+M+A) corresponds to the matrix produced by default for both single-cell and single-nucleus RNA-seq in Cell Ranger version 7 and above.

Run options
-----------

I have an assay where the barcode and UMI don't fit the format of -x technology string. What do I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may need to use additional steps to preprocess the reads to make them "fit". In simple cases, some shell scripts may be sufficient to reformat the reads. In more complex cases, you might want to use a tool such as `splitcode <https://splitcode.readthedocs.io/en/latest/>`_.


Quality check
-------------

Why am I getting a low mapping (pseudoalignment) rate?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can get the mapping rate by looking at p_pseudoaligned in run_info.json in the output folder. If this value is low, there might be a few things to investigate:

* You may want to specifically specify the "unstranded" mode (i.e. specifying --strand=unstranded in kb count). By default, many technologies (i.e. specifying -x 10xv3 as the technology string) are run in forward strand-specific mapping mode. However, some assays may not have the same strand-specificity in which case the default option will not apply. You can try all of --strand=forward, --strand=unstranded, and --strand=reverse to determine the optimal option (i.e. what results in the best mapping rate) for strand-specificity.
* You may want to ensure that you're using the correct index type. First, make sure you're using the correct species. Second, make sure your index is appropriate for the assay type; if you're using the standard index type for single-nucleus RNA-seq, you'll get a low mapping rate (for single-nucleus RNA-seq or any RNA-seq assay with high intronic content, you must use the nac index type).



The nac index type produces multiple matrices. Which one should I use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It depends. The nac index type produces nascent (N), mature (M), and ambiguous (A) matrices. For single-cell RNA-seq, the M+A matrix is generally used for quantification as it includes all non-nascent transcripts and corresponds to the results you will get from quantification using the standard index type. However, you may want to use N+M+A if you want to include nascent transcripts in your quantification and i


Runtime questions
-----------------

Why does the workflow hang at bustools count?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While bustools count can take some time to complete, especially when using the nac index type, if it never seems to complete, then the issue is more serious. This would be due to a mismatch between your transcripts-to-gene (t2g) mapping file and your kallisto index. Please ensure that the t2g file contains the exact same transcript names in the exact same order as the transcripts.txt file produced in the output folder. If you use the prebuilt index and associated files that we distribute or use the files created by kb ref from the official Ensembl or Gencode genome FASTA and GTF files, then bustools count should not hang.


Other questions
---------------

Where do I go for additional help?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please visit the `kallisto issues page <https://github.com/pachterlab/kallisto/issues>`_ on GitHub and post a GitHub issue asking your question.

