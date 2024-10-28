Generate a reference index
=====================

To process RNA-seq reads, one must first use kallisto to build an **index** from a set of sequences, referred to as targets, representing the set of sequences that the sequencing reads can be mapped to. In a standard analysis, these targets are usually transcript sequences (i.e., each individual target corresponds to one transcript). 

**kb-python** enables the construction of kallisto indices through the ``kb ref`` command (Fig. 1). Different types of kallisto indices can be built by specifying the ``--workflow`` argument in kb ref, which selects the type of index to be constructed. The default is ``--workflow=standard``, which creates an index suitable for bulk and single-cell RNA-seq quantification. Specifying ``--workflow=nac`` should be used for quantifying single-nucleus RNA-seq or nascent/mature RNA species.

Downloading a premade index
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oftentimes, it is easy to simply download an index that has already been made.

To download a mouse index for bulk and single-cell RNA-seq (i.e. the **standard** workflow), one can run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt

The files **index.idx** and **t2g.txt** will then be created.

To download a mouse index for single-nucleus RNA-seq or for analyses that require quantification of nascent and mature RNA (i.e. the **nac** workflow), one can run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt -c1 cdna.txt -c2 nascent.txt --workflow=nac


The files **index.idx**, **t2g.txt**, **cdna.txt**, and **nascent.txt** will then be created.

One can replace *mouse* with *human* (or another species). A comprehensive list of pre-created indices (and how they were generated) is available `here <https://github.com/pachterlab/kallisto-transcriptome-indices>`_.  




Making an index for bulk and single-cell RNA-seq
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt

The files **index.idx** and **t2g.txt** will then be created. One can replace *mouse* with *human* (or another species). A comprehensive list of precreated indices (and how they were generated) is available `here <https://github.com/pachterlab/kallisto-transcriptome-indices>`_.  


Making an index for single-nucleus RNA-seq or nascent/mature RNA quantification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oftentimes, it is easy to simply download an index that has already been made. To download a mouse index for single-nucleus RNA-seq or for analyses that require quantification of nascent and mature RNA (i.e. the *nac* workflow), one can run the following:

.. code-block:: text

   kb ref -d mouse -i index.idx -g t2g.txt -c1 cdna.txt -c2 nascent.txt --workflow=nac

The files **index.idx**, **t2g.txt**, **cdna.txt**, and **nascent.txt** will then be created. One can replace *mouse* with *human* (or another species). A comprehensive list of pre-created indices (and how they were generated) is available `here <https://github.com/pachterlab/kallisto-transcriptome-indices>`_.  



