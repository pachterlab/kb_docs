bustools
=============================

bustools sort     
^^^^^^^^^^^^^^^^^^^^       
Sort a BUS file by barcodes and UMIs (or other fields in the BUS file).

``bustools sort`` (using the default options) should always be done before any additional processing of the BUS file following generation of the BUS file from the ``kallisto bus`` command. Many bustools commands will not work properly with an unsorted BUS file. Increasing the number of threads and maximum memory will speed up sorting.

The default behavior is to sort by barcode, UMI, equivalence class (ec), then the flag column.

**Usage:**


.. code-block:: text

   bustools sort [options] bus-files

**Arguments:**


-t, --threads=INT  Number of threads to use (default: 1).

-m, --memory=STRING  Maximum memory used (default: 4G).

-T, --temp=STRING  Location and prefix for temporary files (required if using -p, otherwise defaults to output path).

-o, --output=STRING  Filename to output sorted BUS file into.

-p, --pipe  Write to standard output.

--umi  Sort by UMI, barcode, then ec.

--count  Sort by multiplicity (count), barcode, UMI, then ec.

--flags  Sort by flag, ec, barcode, then UMI.

--flags-bc  Sort by flag, barcode, UMI, then ec.

--no-flags  Ignore and reset the flag column while sorting. If read numbers are present in the flag column of the BUS file, sorting using this option renders BUS file suitable for use in generating count matrices.




bustools correct    
^^^^^^^^^^^^^^^^^^^^    
Error-corrects the barcodes in a BUS file to an **on list**.

Error correction is done based on a hamming distance 1 mismatch between each BUS file barcode sequence and each **on list** sequence. For barcode error correction, the **on list** file simply contains a list of sequences in the **on list**.

Another operation supported is the replacement operation: Each **on list** sequence (in the first column of the **on list** file) has a replacement sequence (in the second column of the **on list** file) designated therefore if a BUS file barcode has an exact match to one of those “on list” sequences, it is replaced with its replacement sequence.

Note: The input BUS file need not be sorted.

**Usage:**


.. code-block:: text

   bustools correct [options] bus-files

**Arguments:**


-o, --output=STRING  Filename to output barcode-corrected BUS file into.

-w, --onlist=FILE  File containing the *on list* sequences.

-p, --pipe  Write to standard output.

-r, --replace  Perform the replacement operation rather than the barcode error correction operation for the file supplied in the -w option.


bustools count           
^^^^^^^^^^^^^^^^^^^^
Generates count matrices from BUS files that have been sorted and barcode-error-corrected.

**Usage:**


.. code-block:: text

   bustools count [options] sorted-bus-files

**Arguments:**


-o, --output=STRING  The prefix of the output files for count matrices.

-g, --genemap=FILE  File for mapping transcripts to genes (when using ``kb ref`` in kb-python, this is the **t2g.txt** file produced by it).

-e, --ecmap=FILE  File for mapping equivalence classes to transcripts.

-t, --txnames=FILE  File with names of transcripts.

--genecounts  Aggregate counts to genes only. This option generates a **gene count matrix**; if this option is not supplied, a *transcript-compatibility counts (TCC) matrix* (where each equivalence class gets a count) is generated instead.

--umi-gene  Handles cases of UMI collisions. For example, a case may be where two reads with the same UMI sequence and the same barcode map to different genes. With this option enabled, those reads are considered to be two distinct molecules which were unintentionally labeled with the same UMI, and hence each gene gets a count.

--cm  Counts multiplicities rather than UMIs. In other words, no UMI collapsing is performed and each mapped read is its own unique molecule regardless of the UMI sequence (i.e. the UMI sequence is ignored).

-m, --multimapping  Include bus records that map to multiple genes. When --genecounts is enabled, this option causes counts to be distributed uniformly across all the mapped genes (for example, if a read multimaps to two genes, each gene will get a count of 0.5).

-s, --split=FILE  Split output matrix in two (plus ambiguous) based on the list of transcript names supplied in this file. If a UMI (after collapsing) or a read maps to transcripts found in this file, the count is entered into a matrix file with the extension ``.2.mtx``; if it maps to transcripts not in this file, the count is entered into a separate matrix file with the extension ``.mtx``; if it maps to some transcripts in this file and some transcripts not in this file, the count is entered into a third matrix file with the extension ``.ambiguous.mtx``. When quantifying **nascent**, **ambiguous**, and **mature** RNA species, the nascent transcript names (which will actually simply be the gene IDs themselves) will be listed in the file supplied to --split so that the ``.mtx`` file contains the mature RNA counts, the ``.2.mtx`` file contains the nascent RNA counts, and the ``.ambiguous.mtx`` file contains the ambiguous RNA counts. Note that **kb-python** renames ``.mtx`` to ``.mature.mtx`` and renames ``2.mtx`` to ``.nascent.mtx``.


**Output:**

Each output file is prefixed with what is supplied to the **--output** option. In **kb count** within **kb-python**, the prefix is **cells_x_genes**. Thus, the files outputted (when generating a gene count matrix via **--genecounts**) will be ``cells_x_genes.mtx`` (the matrix file), ``cells_x_genes.barcodes.txt`` (the barcodes; i.e. the rows of the matrix), and ``cells_x_genes.genes.txt`` (the genes; i.e. the columns of the matrix). When generating a TCC matrix, ``cells_x_genes.ec.txt`` will be generated in lieu of ``cells_x_genes.genes.txt`` as the columns of the matrix will be equivalence classes (ECs) rather than genes. If both sample-specific barcodes and cell barcodes are supplied (as is the case when one uses **--batch-barcodes** in **kallisto bus**), then an additional ``cells_x_genes.barcodes.prefix.txt`` file will be created containing the sample-specific barcodes. The lines of this file correspond to the lines in the ``cells_x_genes.barcodes.txt`` (both files will have the same number of lines). Finally, when **--split** is supplied, additional **.mtx** matrix files will be generated (see the **--split** option described above).




bustools inspect     
^^^^^^^^^^^^^^^^^^^^
Produces a report summarizing the contents of a sorted BUS file. The report can be output either to standard output or to a JSON file.


**Usage:**


.. code-block:: text

   bustools inspect [options] sorted-bus-file

**Arguments:**


-o, --output=STRING  Filename for JSON file output (optional).

-e, --ecmap=FILE  File for mapping equivalence classes to transcripts.

-w, --onlist=FILE  File containing the barcodes "on list".

-p, --pipe  Write to standard output.



**Output:**

.. code-block:: text
  :caption: Example report output in standard output (using -p)

  Read in 3148815 BUS records
  Total number of reads: 3431849

  Number of distinct barcodes: 162360
  Median number of reads per barcode: 1.000000
  Mean number of reads per barcode: 21.137281

  Number of distinct UMIs: 966593
  Number of distinct barcode-UMI pairs: 3062719
  Median number of UMIs per barcode: 1.000000
  Mean number of UMIs per barcode: 18.863753

  Estimated number of new records at 2x sequencing depth: 2719327

  Number of distinct targets detected: 70492
  Median number of targets per set: 2.000000
  Mean number of targets per set: 3.091267

  Number of reads with singleton target: 1233940

  Estimated number of new targets at 2x seuqencing depth: 6168

  Number of barcodes in agreement with on-list: 92889 (57.211752%)
  Number of reads with barcode in agreement with on-list: 3281671 (95.623992%)


.. code-block:: text
  :caption: Example report output in JSON format

  {
    "numRecords": 3148815,
    "numReads": 3431849,
    "numBarcodes": 162360,
    "medianReadsPerBarcode": 1.000000,
    "meanReadsPerBarcode": 21.137281,
    "numUMIs": 966593,
    "numBarcodeUMIs": 3062719,
    "medianUMIsPerBarcode": 1.000000,
    "meanUMIsPerBarcode": 18.863753,
    "gtRecords": 2719327,
    "numTargets": 70492,
    "medianTargetsPerSet": 2.000000,
    "meanTargetsPerSet": 3.091267,
    "numSingleton": 1233940,
    "gtTargets": 6168,
    "numBarcodesOnOnlist": 92889,
    "percentageBarcodesOnOnlist": 0.57211752,
    "numReadsOnOnlist": 3281671,
    "percentageReadsOnOnlist": 0.95623992
  }


.. note::

  The *numTargets*, *medianTargetsPerSet*, *meanTargetsPerSet*, *numSingleton*, and *gtTargets* values are only generated if the **--ecmap** option is provided. The *numBarcodesOnOnlist*, *percentageBarcodesOnOnlist*, *numReadsOnOnlist*, *percentageReadsOnOnlist* values are only generated if **--onlist** is provided.


.. _faq bustools barcodes make onlist:


bustools allowlist
^^^^^^^^^^^^^^^^^^^^
Generates an **on list** based on the barcodes in a sorted BUS file.

This is a way of generating an **on list** that the barcodes in the BUS file will be corrected to, for technologies that don’t provide an **on list**.

**Usage:**


.. code-block:: text

   bustools allowlist [options] bus-files

**Arguments:**


-o, --output=STRING  Filename to output the *on list* into.

-f, --threshold=INT  A *highly* optional parameter specifying the minimum number of times a barcode must appear to be included in the *on list*. If not provided, a threshold will be determined based on the first 200 to 100200 BUS records.


bustools capture         
^^^^^^^^^^^^^^^^^^^^
Separates a BUS file into multiple files according to the capture criteria.

**Usage:**


.. code-block:: text

   bustools capture [options] bus-files

**Arguments:**

Capture options:

-F, --flags  Capture list is a list of flags to capture.

-s, --transcripts  Capture list is a list of transcripts to capture.

-u, --umis  Capture list is a list of UMI sequences to capture.

-b, --barcode  Capture list is a list of barcodes to capture.

Other arguments:

-o, --output=STRING  Name of file for the captured BUS output.

-x, --complement  Take complement of captured set. (i.e. output all BUS records that do NOT match an entry in the capture list).

-c, --capture=FILE  File containing the “capture list” (i.e. list of transcripts, transcripts, flags, UMI sequences, or barcode sequences).

-e, --ecmap=FILE  File for mapping equivalence classes to transcripts (required for --transcripts).

-t, --txnames=FILE  File with names of transcripts (required for --transcripts).

-p, --pipe  Write to standard output.


.. note::

  If you use the **-b** (**--barcode**) option and want to capture all records containing a sample-specific barcode from running **--batch-barcodes** in **kallisto bus**, in the "capture list" file, enter the 16-bp sample-specific barcode followed by a * character (e.g. AAAAAAAAAAAAAACT*).


bustools text            
^^^^^^^^^^^^^^^^^^^^
Converts a binary BUS file into its plaintext representation.

The plaintext will have the columns (in order): barcode, UMI, equivalence class, count, flag, and pad. (Note: The last two columns will only be outputted if the respective option is specified by the user).

**Usage:**


.. code-block:: text

   bustools text [options] bus-files

**Arguments:**

-o, --output=STRING  Filename of the output text file.

-f, --flags  Write the flag column.

-d, --pad  Write the pad column (the "pad" column is an additional 32-bit field in the BUS file, in case one would like to use the BUS format to store additional data for each BUS record; this column is typically not used).

-p, --pipe Write to standard output

-a, --showAll  Show all 32 bases in the barcodes field (e.g. if --batch-barcodes is specified in kallisto bus, the cell barcodes are stored in barcodes field and are used for bustools barcode correction to an "on list"; however, the artificial sample-specific barcodes are stored as an additional “hidden” field in the barcodes column, immediately preceding the cell barcodes, and may be truncated or left-padded with A’s to fill the 32 bases. For example, if the cell barcode is 12 bases, there will be 4 A’s followed by the 16-bp sample-specific barcode followed by the 12-base cell barcode. If the cell barcode is 26 bases, the last 6 bases of the sample-specific barcode will be shown followed by the 26-base cell barcode).


.. code-block:: text
  :caption: An example of the plaintext output of a BUS file (with the flag column)

  AAAAGATCACTATGCACTATCATC  GCAAAACCTT  156   2  0
  AAAAGATCAGATCGCACACTTTCA  TAGAGTAACC  438   3  0
  AAAAGATCAGATCGCAGCTCTACT  TTAGGTATAG  1808  1  0
  AAAAGATCAGCACCTCCTGACTTC  AATCGGCATT  4481  1  0


.. note::

  If one runs kallisto bus with the **-n** (**--num**) option, the read number (zero-indexed) of the mapped reads will be stored in the *flags* column (i.e. the *fifth* column). One can view those read numbers using **bustools text** to identify which reads in the input FASTQ files mapped (and which reads were unmapped).


bustools fromtext            
^^^^^^^^^^^^^^^^^^^^
Converts a plaintext representation of a BUS file to a binary BUS file.

The plaintext input file should have four columns: barcode, UMI, equivalence class, and count. Optionally, a fifth column (the flags column) can be supplied.

**Usage:**


.. code-block:: text

   bustools fromtext [options] text-files

**Arguments:**


-o, --output=STRING  Filename to write the output BUS file.

-p, --pipe  Write to standard output.


bustools extract         
^^^^^^^^^^^^^^^^^^^^
Extracts FASTQ reads corresponding to reads in BUS file.

This will extract the successfully mapped sequencing reads from the input FASTQ files that were processed with kallisto bus with the **-n** (**--num**) option, which places the read number (zero-indexed) in the flags column of the BUS file. Although BUS files with read numbers present in the flags column should not be used for downstream quantification, they can be used by **bustools extract** to extract the original sequencing reads (as well as by **bustools text** to view the sequencing read number along with the barcode, UMI, and equivalence class).

Note: The BUS file must be sorted by flag. The output BUS file directly from kallisto should already be sorted by flag, but, if not, one can use apply **bustools sort --flag** on the BUS file.

**Usage:**


.. code-block:: text

   bustools extract [options] sorted-by-flag-bus-file

**Arguments:**


-o, --output=STRING  Directory that the output FASTQ files will be stored in

-f, --fastq=STRING  FASTQ file(s) from which to extract reads (comma-separated list). These should be the same files used as input to ``kallisto bus``.

-N, --nFastqs=INT  Number of FASTQ file(s) per run. For example, in *10xv3* where there are two FASTQ files (and R1 and R2 file), **--nFastqs=2** should be set.


.. note::

  To continue working with BUS files with read numbers present in the flags column for downstream analysis, you must remove the flags by running ``bustools sort`` with ``--no-flags``. It is important that you do so otherwise the BUS file will not be suitable for further processing (including generating count matrices).


**Example:**

The extraction feature is especially useful to use in conjunction with bustools capture when one wishes to extract specific reads (e.g. reads that contain a certain barcode or reads whose equivalence class contains a certain transcript). Below, we show an example of how to extract reads from two input files: **R1.fastq.gz** and **R2.fastq.gz** entered into a ``kallisto bus`` run with results outputted into a directory named **output_dir**. We’ll extract reads that are compatible with either the transcript **ENSMUST00000171143.2** or **ENSMUST00000131532.2**.

Create a file called **capture.txt** containing the following two lines:

.. code-block:: text

  ENSMUST00000171143.2
  ENSMUST00000131532.2

Run the following:

.. code-block:: text

  bustools capture -c capture.txt --transcripts \
  --ecmap=output_dir/matrix.ec \
  --txnames=output_dir/transcripts.txt -p \
  output_dir/output.bus | bustools extract --nFastqs=2 \
  --fastq=R1.fastq.gz,R2.fastq.gz -o extracted_output -


The capture results are directly piped into the extract command, and the extracted FASTQ sequencing reads output are placed into the paths ``extracted_output/1.fastq.gz`` and ``extracted_output/2.fastq.gz`` (for the input files **R1.fastq.gz** and **R2.fastq.gz**, respectively). ``bustools extract`` does not work when you have sample-specific barcodes in your BUS file because each sample’s read number (as recorded in the flags column of the BUS file) starts from 0. To work around this, you should first use bustools capture to isolate a specific sample and then supply that specific sample’s FASTQ file(s).


bustools umicorrect      
^^^^^^^^^^^^^^^^^^^^
Implements the UMI correction algorithm of `UMI-tools <https://github.com/CGATOxford/UMI-tools>`_ (`Smith, Heger, Sudbery. *Genome Research*, 2017 <https://doi.org/10.1101/gr.209601.116>`_) and outputs a BUS file with the corrected UMIs.


**Usage:**


.. code-block:: text

   bustools umicorrect [options] sorted-bus-file

**Arguments:**


-o, --output=STRING  Filename to write the output BUS file with UMIs corrected.

-p, --pipe  Write to standard output.

-g, --genemap=FILE  File for mapping transcripts to genes (when using ``kb ref`` in kb-python, this is the **t2g.txt** file produced by it).

-e, --ecmap=FILE  File for mapping equivalence classes to transcripts.

-t, --txnames=FILE  File with names of transcripts.



bustools compress          
^^^^^^^^^^^^^^^^^^^^
Takes in a BUS file, sorted by *barcode-umi-ec* (i.e. the default option for ``bustools sort``), and compresses it.

**Usage:**


.. code-block:: text

   bustools compress [options] sorted-bus-file

**Arguments:**


-N, --chunk-size=INT  Number of rows to compress as a single block.

-o, --output=STRING  Filename for the output compressed BUS file.

-p, --pipe  Write to standard output.


bustools decompress          
^^^^^^^^^^^^^^^^^^^^
Takes in a compressed BUS file and inflates (i.e. decompresses) it.


**Usage:**


.. code-block:: text

   bustools decompress [options] compressed-bus-file

**Arguments:**


-o, --output=STRING  Filename for the output decompressed BUS file.

-p, --pipe  Write to standard output.


bustools version         
^^^^^^^^^^^^^^^^^^^^
Prints version information.

**Usage:**


.. code-block:: text

   bustools version

bustools cite    
^^^^^^^^^^^^^^^^^^^^
Prints citation information.

**Usage:**


.. code-block:: text

   bustools cite
