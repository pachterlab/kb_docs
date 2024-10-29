kallisto
=============================

Running kallisto usually involves two steps:

#. Indexing a FASTA file of target sequences via ``kallisto index``
#. Mapping sequencing reads to kallisto index using ``kallisto bus``

.. _kallisto index:

kallisto index         
^^^^^^^^^^^^^^^^^^^^
Builds a kallisto index from an input FASTA file containing transcript sequences.

**Example usage:**


.. code-block:: text

   kallisto index -i index.idx transcripts.fasta



**Arguments:**


-i, --index=STRING  Filename for the kallisto index to be constructed. Required argument.

-k, --kmer-size=INT  k-mer (odd) length (default: 31, max value: 31).

-t, --threads=INT  Number of threads to use (default: 1).

-d, --d-list=STRING  Path to a FASTA-file containing sequences to mask from quantification (i.e. to extract distinguishing flanking k-mers from).

--make-unique  Replace repeated target names with unique names.

--aa  Generate index from a FASTA-file containing amino acid sequences.

--distinguish  Generate index where sequences are distinguished by the sequence name, for example, when indexing k-mers distributed across multiple targets rather than across a single contiguous target sequence.

-T, --tmp=STRING  Temporary directory (default: tmp).

-m, --min-size=INT  Length of minimizers (default: automatically chosen).

-e, --ec-max-size=INT  Maximum number of targets in an equivalence class (default: no maximum).



Among the arguments in kallisto index, in a general use case, typically only ``-i`` (**--index**; to specify the name of the index output filename), ``-t`` (**--threads**; to specify the number of threads), and ``-d`` (**--d-list**; to specify the filename from which to extract distinguishing flanking k-mers) are used.


kallisto bus           
^^^^^^^^^^^^^^^^^^^^
Generate BUS files for single-cell data.

**Usage:**


.. code-block:: text

   kallisto bus [arguments] FASTQ-files
   kallisto bus [arguments] --batch=batch.txt


**Arguments:**

-i, --index=STRING  Filename for the kallisto index to be used for pseudoalignment. Required argument.

-o, --output-dir=STRING  Directory to write output to. Required argument.

-x, --technology=STRING  The “technology” string for the sequencing technology used. Required argument.

-l, --list  List the technologies that are hard-coded into kallisto so the name of the technology can simply be supplied as the technology string.

-B, --batch=FILE  Path to a batch file. The batch file is a text file listing all the samples to be analyzed with the paths to their respective FASTQ files. If a batch file is supplied, then one shouldn’t supply FASTQ files on the command line.

-t, --threads=INT  Number of threads to use (default: 1).

-b, --bam  Input file is a BAM file rather than a set of FASTQ files. Note: This is a nonstandard workflow. It is strongly recommended to supply FASTQ files rather than use this option and not all technologies are supported by this option.

-n, --num  Output read number in flag column of BUS file. The read number is zero-indexed. One can view the read numbers by inspecting the BUS file using bustools text. This option is useful for pulling specific mapped reads out of the FASTQ file or for examining which reads did not end up being mapped by kallisto. (Important note: BUS files with read numbers in the flag column should NOT be used in quantification tasks with bustools). (Note: incompatible with --bam)

-N, --numReads=INT  Maximum number of reads to process from supplied input. This is useful for processing a small subset of reads from a large sequencing experiment as a quick quality control. Moreover, the program returns 1 if the number of reads processed from the input is less than the number supplied here. This is useful for catching errors when we expect a certain number of reads to be present in the input but not all the reads end up being there.

-T, --tag=STRING  5′ tag sequence to identify UMI reads for certain technologies. This is useful for smart-seq3 where the UMI-containing reads have an 11-bp tag sequence (ATTGCGCAATG) located at the beginning of the UMI location. If this tag sequence is present immediately before the UMI location, then the UMI is processed into the output BUS file; for all other sequences, the UMI field in the BUS file is left empty (the field is populated with the value -1 in binary format). Note: Matching the tag sequence is done with a hamming distance error tolerance of 1 if the tag is longer than 5 nucleotides. Otherwise, no error tolerance is permitted. Note: If strand-specificity is enabled, it will only be applied to the UMI-containing reads.

--fr-stranded  Strand specific reads, first read forward.

--rf-stranded  Strand specific reads, first read reverse.

--unstranded  Treat all read as non-strand-specific.

--paired  Treat reads as paired (i.e. if two biological read sequences are present across two FASTQ files, they will be mapped taking into account their paired-endness: fragment length distribution will be estimated for the read pairs, and only one read in the pair needs to map successfully in order to be considered successful pseudoalignment).

--long  Run lr-kallisto for long-read sequence mapping.

--threshold=DOUBLE  Threshold in lr-kallisto for rate of unmapped k-mers per read (default: 0.8).

--aa  Align to index generated from a FASTA-file containing amino acid sequences.

--inleaved  Specifies that input is an interleaved FASTQ file. That is, only one FASTQ file is supplied and the sequences are interleaved. For example, instead of an R1 and R2 FASTQ file, a single FASTQ file can be supplied where the reads are listed in order of each R2 read immediately following each R1 read. This is also useful when piping interleaved output generated by another program directly into kallisto bus which can be done by supplying - as the input file in lieu of FASTQ file names.

--batch-barcodes  Records both the generated sample-specific barcodes as well as the cell barcodes extracted from the reads in the output BUS file. If not supplied, then the sample-specific barcodes are not recorded.

**Example Usage for 10x single-cell:**

.. code-block:: text

   kallisto bus -x 10xv3 -o output_dir -i index.idx R1.fastq.gz R2.fastq.gz

**Output:**

In the output directory specified by ``-o`` or ``--output-dir``, the following files are made:

* **output.bus**: A BUS file containing the mapped reads information, which will be further processed using bustools.
* **transcripts.txt**: A text file containing a list of the names of the targets or transcripts used.
* **matrix.ec**: A text file containing the equivalence classes. The equivalence class number (zero-indexed) is in the first column and a comma-separated list of target or transcript IDs belonging to that equivalence class are in the second column. The transcript IDs are numbers (zero-indexed) that correspond to the line numbers (zero-indexed) in the transcripts.txt file.
* **run_info.json**: Contains information about the run, including percent of reads pseudoaligned, number of reads processed, index version, etc.
* **flens.txt**: Only produced when using paired-end mapping. Contains the fragment length distribution, which can be used by kallisto quant-tcc to produce TPM abundance values.



kallisto quant-tcc     
^^^^^^^^^^^^^^^^^^^^
Quantifies abundance from pre-computed transcript-compatibility counts. It takes in a transcript compatibility counts (TCC) matrix outputted by **bustools count** and runs an expectation-maximization (EM) algorithm to produce transcript abundances. This is useful for producing TPM values from bulk RNA-seq and smart-seq2 RNA-seq data. The output files can be used by bulk RNA-seq differential gene expression programs.

**Example usage:**

.. code-block:: text

   kallisto quant-tcc -i index.idx -o quant_output -e count_tcc.ec.txt count_tcc.mtx

(Note: count_tcc.ec.txt and count_tcc.mtx should have been outputted by running **bustools count** *without* the --genecounts option).

**Arguments:**

-o, --output-dir=STRING  Directory to write output to. Required argument.

-e, --ec-file=FILE  File containing equivalence classes (the equivalence class file in the same directory as the output matrix file should be used). Required argument.

-i, --index=STRING  Filename for the kallisto index to be used (required if --txnames is not supplied or if any of the fragment length options: -f, -l, -s, is supplied since the index contains transcript lengths, which is necessary for length normalization).

-T, --txnames=STRING  File with names of transcripts (required if index file not supplied).

-f, --fragment-file=FILE  File containing fragment length distribution (flens.txt outputted by kallisto).

-l, --fragment-length=DOUBLE  Estimated average fragment length.

-s, --sd=DOUBLE  Estimated standard deviation of fragment length.

--long  Use the lr-kallisto version of EM (for long reads)

-P, --platform=STRING  lr-kallisto option for the sequencing platform used. Options: PacBio or ONT.

-p, --priors=FILE  Priors for the EM algorithm, either as raw counts or as probabilities. Pseudocounts are added to raw counts to prevent zero valued priors. Supplied in the same order as the transcripts in the transcriptome (e.g. in --txnames).

-t, --threads=INT  Number of threads to use (default: 1).

-g, --genemap=FILE  File for mapping transcripts to genes (this is the t2g.txt file produced by kb ref in kb-python and is required for obtaining gene-level abundances).

-G, --gtf=FILE  GTF file for transcriptome information (can be used instead of --genemap for obtaining gene-level abundances).

-b, --bootstrap-samples=INT  Number of bootstrap samples (default: 0). Bootstrap samples are useful for obtaining inferential variance which can be used by programs such as sleuth or edgeR.

--matrix-to-files  Reorganize matrix output into abundance tsv files.

--matrix-to-directories  Reorganize matrix output into abundance tsv files across multiple directories.

--seed=INT  Seed for the bootstrap sampling (default: 42).

--plaintext  Output plaintext only, not HDF5. (When --matrix-to-directories or --matrix-to-files are supplied, HDF5 files are outputted by default, in addition to the plaintext abundance tsv files since HDF5 files containing abundance information are used by programs such as sleuth; this option disables that).

Note: -l, -s values only should be supplied when effective length normalization needs to be performed but --fragment-file is not specified). If none of the fragment length
options: -f -l, -s, are supplied, then effective length normalization is not performed (i.e. transcript length isn’t taken into account when quantification is performed).


**Output:**

In the output directory specified by ``-o`` or ``--output-dir``, the following files are made:

* **matrix.abundance.mtx**: A sample-by-transcript (or cell-by-transcript) MatrixMarket sparse matrix file containing the estimated transcript counts.
* **matrix.abundance.gene.mtx**: A sample-by-gene (or cell-by-gene) MatrixMarket sparse matrix file containing the estimated transcript counts summed up to gene-level. Only made if a transcript-to-gene mapping was provided.
* **matrix.abundance.tpm.mtx**: A sample-by-transcript (or cell-by-transcript) MatrixMarket sparse matrix file containing the normalized transcript abundances (if effective length normalization is performed, then the results are in length-normalized TPM units; otherwise the results are in CPM [counts-per-million] units wherein each value is normalized by the sum of all counts for that particular sample or cell).
* **matrix.abundance.gene.tpm.mtx**: A sample-by-gene (or cell-by-gene) MatrixMarket sparse matrix file containing the same information as matrix.abundance.tpm.mtx except summed up to gene-level if a transcript-to-gene mapping was provided.
* **transcripts.txt**: A text file containing a list of the names of the targets or transcripts used (not made if a transcripts file was already provided via --txnames). These transcripts correspond to the columns of transcripts in the matrix abundance output files.
* **genes.txt**: A text file containing a list of genes, if a transcript-to-gene mapping was provided. These genes correspond to the columns of genes in the matrix abundance output files.
* **--matrix-to-files**: If this option is provided, the abundance output files will be named abundance_{n}.tsv and abundance_{n}.h5 (hdf5 format) where {n} is the sample number or cell number (which corresponds to the rows in the matrix files). If bootstrapping is enabled, additional abundance tsv files (starting with the prefix bs_abundance_{n}_) will be created for each bootstrap sample. If a transcript-to-gene mapping is provided, abundance.gene_{n}.tsv files will be created as well with the gene level quantification.
* **--matrix-to-directories**: If this option is provided, directories named abundance_{n} (where {n} is the sample number or cell number, corresponding to the rows in the matrix files) will be created. Within each directory, an abundance.tsv text file and abundance.h5 HDF5 file will be created containing the quantifications for that particular sample or cell. If bootstrapping is enabled, additional abundance tsv files (starting with the prefix bs_abundance_) will be created for each bootstrap sample. If a transcript-to-gene mapping is provided, an abundance.gene.tsv file will be created within each directory with the gene-level quantification.

The first few lines of an abundance tsv file looks as follows:

.. code-block:: text
  :caption: abundance.tsv

  target_id          length  eff_length  est_counts  tpm
  ENST00000641515.2  2618    2349.39     0           0
  ENST00000426406.4  939     670.39      0           0
  ENST00000332831.4  995     726.39      0           0
  ENST00000616016.5  3465    3196.39     5.68407     0.128913
  ENST00000618323.5  3468    3199.39     1.83535     0.041586


kallisto quant         
^^^^^^^^^^^^^^^^^^^^
The "old way" of running kallisto (we recommend using *kallisto bus* instead). Runs the pseudoalignment and quantification algorithm to produce transcript abundance estimates.

**Example usage:**

.. code-block:: text

   kallisto quant -i index.idx -o output_dir R1.fastq.gz R2.fastq.gz

**Arguments:**

-i, --index=STRING  Filename for the kallisto index to be used for quantification. Required argument.

-o, --output-dir=STRING  Directory to write output to. Required argument.

-b, --bootstrap-samples=INT  Number of bootstrap samples (default: 0).

--seed=INT  Seed for the bootstrap sampling (default: 42).

--plaintext  Output plaintext instead of HDF5.

--fr-stranded  Strand specific reads, first read forward.

--rf-stranded  Strand specific reads, first read reverse.

-l, --fragment-length=DOUBLE  Estimated average fragment length.

-s, --sd=DOUBLE  Estimated standard deviation of fragment length (default: -l, -s values are estimated from paired end data, but are required when using --single).

-p, --priors=FILE  Priors for the EM algorithm, either as raw counts or as probabilities. Pseudocounts are added to raw reads to prevent zero valued priors. Supplied in the same order as the transcripts in the transcriptome.

-t, --threads=INT  Number of threads to use (default: 1).

**Output:**

*kallisto quant* produces three output files by default:

* **abundance.h5** is a HDF5 binary file containing run info, abundance esimates, bootstrap estimates, and transcript length information length.
* **abundance.tsv** is a plaintext file of the abundance estimates. It does not contains bootstrap estimates. Please use the --plaintext mode to output plaintext abundance estimates. Alternatively, kallisto h5dump can be used to output an HDF5 file to plaintext. The first line contains a header for each column, including estimated counts, TPM, effective length.
* **run_info.json** is a json file containing information about the run.


kallisto h5dump        
^^^^^^^^^^^^^^^^^^^^
Converts HDF5-formatted results to plaintext.

**Example usage:**

.. code-block:: text

   kallisto h5dump -o output_dir abundance.h5

**Output:**

In the output directory specified by ``-o`` or ``--output-dir``, the following files are made:

* **abundance.tsv**: The plaiintext abundance tsv file.
* If bootstrapping is enabled, additional abundance tsv files (starting with the prefix **bs_abundance_**) will be created for each bootstrap sample. 



kallisto inspect       
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


kallisto version       
^^^^^^^^^^^^^^^^^^^^
Prints version information.

**Usage:**


.. code-block:: text

   kallisto version



kallisto cite          
^^^^^^^^^^^^^^^^^^^^
Prints citation information

**Usage:**


.. code-block:: text

   kallisto cite
