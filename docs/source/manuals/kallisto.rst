kallisto
=============================

Running kallisto usually involves two steps:

1.  Indexing a FASTA file of target sequences via
``kallisto index``.
2. Mapping sequencing reads to kallisto index using ``kallisto bus``.

index         
^^^^^^^^^^^^^^^^^^^^
Builds a kallisto index 

quant         
^^^^^^^^^^^^^^^^^^^^
Runs the quantification algorithm 

quant-tcc     
^^^^^^^^^^^^^^^^^^^^
Runs quantification on transcript-compatibility counts

bus           
^^^^^^^^^^^^^^^^^^^^
Generate BUS files for single-cell data 

h5dump        
^^^^^^^^^^^^^^^^^^^^
Converts HDF5-formatted results to plaintext

inspect       
^^^^^^^^^^^^^^^^^^^^
Inspects and gives information about an index.

The index can be loaded more quickly by using multiple threads, which can be specified by the ``-t`` option.

**Example usage:**

.. code-block:: text

   kallisto inspect -t 8 /path/to/kallisto/index.idx


**Example output:**

.. code-block:: text

  [index] k-mer length: 31
  [index] number of targets: 252,301
  [index] number of k-mers: 155,644,518
  [index] number of distinguishing flanking k-mers: 7,425,493
  [inspect] Index version number = 12
  [inspect] number of unitigs = 9411252
  [inspect] minimizer length = 23
  [inspect] max EC size = 3873
  [inspect] number of ECs discarded = 0


version       
^^^^^^^^^^^^^^^^^^^^
Prints version information.

**Usage:**


.. code-block:: text

   kallisto version



cite          
^^^^^^^^^^^^^^^^^^^^
Prints citation information

**Usage:**


.. code-block:: text

   kallisto cite
