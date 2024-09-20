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
Inspects and gives information about an index

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
