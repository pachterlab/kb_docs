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


bustools umicorrect      
^^^^^^^^^^^^^^^^^^^^
Error correct the UMIs in a BUS file

bustools count           
^^^^^^^^^^^^^^^^^^^^
Generate count matrices from a BUS file

bustools inspect     
^^^^^^^^^^^^^^^^^^^^
Produce a report summarizing a BUS file

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


bustools project        
^^^^^^^^^^^^^^^^^^^^
Project a BUS file to gene sets

bustools capture         
^^^^^^^^^^^^^^^^^^^^
Capture records from a BUS file

bustools merge           
^^^^^^^^^^^^^^^^^^^^
Merge bus files from same experiment

bustools text            
^^^^^^^^^^^^^^^^^^^^
Convert a binary BUS file to a tab-delimited text file

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
Extract FASTQ reads correspnding to reads in BUS file

bustools predict         
^^^^^^^^^^^^^^^^^^^^
Correct the count matrix using prediction of unseen species

bustools collapse        
^^^^^^^^^^^^^^^^^^^^
Turn BUS files into a BUG file

bustools clusterhist     
^^^^^^^^^^^^^^^^^^^^
Create UMI histograms per cluster

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
Prints version number

bustools cite    
^^^^^^^^^^^^^^^^^^^^
Prints citation information
