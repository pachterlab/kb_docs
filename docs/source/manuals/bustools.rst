bustools
=============================

bustools sort     
^^^^^^^^^^^^^^^^^^^^       
Sort a BUS file by barcodes and UMIs (or other fields in the BUS file).

``bustools sort`` (using the default options) should always be done before any
additional processing of the BUS file following generation of the BUS file from the ``kallisto
bus`` command. Many bustools commands will not work properly with an unsorted BUS file.
Increasing the number of threads and maximum memory will speed up sorting.

The default behavior is to sort by barcode, UMI, equivalence class (ec), then the flag column.

Usage
.....

.. code-block:: text

   bustools sort [options] bus-files

Arguments
.........

.. option:: -t, --threads=INT

   Number of threads to use (default: 1).

.. option:: -m, --memory=STRING

   Maximum memory used (default: 4G).


bustools correct    
^^^^^^^^^^^^^^^^^^^^    
Error correct a BUS file

bustools umicorrect      
^^^^^^^^^^^^^^^^^^^^
Error correct the UMIs in a BUS file

bustools count           
^^^^^^^^^^^^^^^^^^^^
Generate count matrices from a BUS file

bustools inspect     
^^^^^^^^^^^^^^^^^^^^
Produce a report summarizing a BUS file

bustools whitelist
^^^^^^^^^^^^^^^^^^^^
Generate a whitelist from a BUS file

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

bustools linker          
^^^^^^^^^^^^^^^^^^^^
Remove section of barcodes in BUS files

bustools version         
^^^^^^^^^^^^^^^^^^^^
Prints version number

bustools cite    
^^^^^^^^^^^^^^^^^^^^
Prints citation information
