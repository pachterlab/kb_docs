Pseudoalignment of single-cell RNA seq data
=======================================


To view examples/tutorials of processing single-cell or single-nucleus RNA-seq, see :ref:`Tutorials`



We'll assume that an index (**index.idx** and **t2g.txt**) has already been generated via ``kb ref``. We'll use ``kb count`` for pseudoalignment of single-cell RNA-seq reads.

Required arguments for the ``kb count`` command:

- The **index file** and **t2g file** (generated by ``kb ref``).
- The **sequencing technology** (check ``kb --list`` for supported technologies).
- The **output directory**.
- The **read FASTQ files**.


Single-cell RNA-seq quantification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Example:**

.. code-block:: bash

    kb count -i index.idx -g t2g.txt -x 10xv3 -o output_dir read1.fastq read2.fastq ...

- Read files should be listed sequentially as positional arguments.
- FASTQ files can be **gzipped or unzipped**.
- For single-cell data with multiple files, order files as follows: file1_R1.fastq.gz file1_R2.fastq.gz file2_R1.fastq.gz file2_R2.fastq.gz  file3_R1.fastq.gz file3_R2.fastq.gz ...
- For all technologies besides 10xv1 and multiplexed SMARTSEQ data, any index FASTQ files (i.e., containing I1/I2 in the name) should not be passed into kb count.


**Example:**

.. code-block:: bash

    kb count -i index.idx -g t2g.txt -x 10xv3 -o output_dir \
        SAMPLE_L001_R1_001.fastq.gz SAMPLE_L001_R2_001.fastq.gz \
        SAMPLE_L002_R1_001.fastq.gz SAMPLE_L002_R2_001.fastq.gz ...


For **paired-end** reads (e.g., much bulk RNA-seq, some SMARTSEQ), use ``--parity paired`` and  
list paired reads sequentially.

**Example:**

.. code-block:: bash

    kb count -i index.idx -g t2g.txt -x SMARTSEQ2 -o output_dir --parity paired \
        SAMPLE1_1.fastq.gz SAMPLE1_2.fastq.gz SAMPLE2_1.fastq.gz SAMPLE2_2.fastq.gz ...

Single-nucleus RNA-seq
^^^^^^^^^^^^^^^^^^^^^^

When using single-cell RNA-seq, you must use the ``--workflow=nac`` when constructing the index via ``kb ref``. However, you may use the default standard workflow in ``kb count`` for quantifying your single-nucleus RNA-seq reads (i.e. you're using the standard workflow to map against a nac index type). Thus, the ``kb count`` command will be the same as it is for single-cell.


Nascent and mature RNA quantification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to quantify nascent and mature RNAs separately, you would use ``--workflow=nac`` in ``kb count`` (see the nascent and mature RNA quantification tutorial for more details).

If using **nac** in ``kb count``, pass the generated ``c1`` and ``c2`` files from ``kb ref``.

**Example:**

.. code-block:: bash

    kb count -i index.idx -g t2g.txt -x 10xv3 -o output_dir --workflow=nac \
        -c1 c1_file.txt -c2 c2_file.txt read1.fastq read2.fastq ...


Counting Multimapped Reads
^^^^^^^^^^^^^^^^^^^^^^^^^^


By default, multimapped reads **are not counted**. To include multimapped reads, use the ``--mm`` flag to distribute the gene counts evenly across multimappers (which will produce fractional counts).

**Example:**

.. code-block:: bash

    kb count -i index_file.idx -g t2g_file.txt -x 10xv3 -o output_dir --mm R1.fastq R2.fastq ...


Output Files
^^^^^^^^^^^^

The output directory (``-o``) will contain:

- ``counts_unfiltered/`` (raw count matrix)

  - ``cells_x_genes.mtx`` → Matrix file
  - ``cells_x_genes.genes.txt`` → Gene IDs
  - ``cells_x_genes.genes.names.txt`` → Gene symbols
  - ``cells_x_genes.barcodes.txt`` → Cell barcodes

If the ``-o`` option is omitted, the output directory will be the current working directory.

If the ``--h5ad`` flag is used in kb count, an additional ``adata.h5ad`` file will be generated.

For more details on additional flags, output files, and other features, see the full documentation.



Batch file processing
^^^^^^^^^^^^^^^^^^^^^


Below, we show how to run kb count to perform an analysis of multiple samples. A batch file (batch.txt) can be provided, in lieu of FASTQ files, listing all the samples to be analyzed with the paths to their respective FASTQ files. The ``--batch-barcodes`` option is provided to store the sample-specific barcodes that are created in addition to the cell barcodes (without this option, only cell barcodes are stored).

.. code-block:: bash

    kb count ... --batch-barcodes batch.txt

The batch.txt file looks as follows:

.. code-block:: text

    Sample1 sample1_R1.fastq.gz sample1_R2.fastq.gz
    Sample2 sample2_R1.fastq.gz sample2_R2.fastq.gz
    Sample3 sample3_R1.fastq.gz sample3_R2.fastq.gz
    Sample4 sample4_R1.fastq.gz sample4_R2.fastq.gz


The sample ID is in the first column. Multiple rows can be provided for the same sample ID (e.g., if the FASTQ files are divided across multiple lanes). The third column can be omitted if only one FASTQ file is specified by the technology.

The output directory will contain two files: matrix.cells, which lists the sample IDs, and matrix.sample.barcodes, which contains the 16 bp sample-specific pseudobarcodes. These pseudobarcodes are not actual read barcodes but are generated to differentiate samples. Each line in matrix.cells corresponds to the same line in matrix.sample.barcodes. The pseudobarcodes appear in the cells_x_genes.barcodes.prefix.txt file within the counts_unfiltered directory, corresponding to the rows of the cell-by-gene matrix.



.. note::

   **To align single-cell RNA-seq data against a protein or amino acid reference, see:** 
   `Translated Pseudoalignment </../translated/pseudoalignment>`_


