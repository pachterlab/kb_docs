.. _kb-usage:

kb-python
=============================

Running kb-python usually involves two steps:

#. Indexing a FASTA file of target sequences via ``kb ref``
#. Mapping sequencing reads to kallisto index using ``kb count``

kb-python supports several different sequencing technologies. Run ``kb --list`` to view technology information.

.. _kb ref:

kb ref
^^^^^^^^^^^^^^^^^^^^
Build a kallisto index and transcript-to-gene mapping.

**Usage:**


.. code-block:: text

   kb ref -i index.idx -g t2g.txt -f1 cdna.fasta [arguments] genome.fasta genome.gtf

**Required Arguments:**

-i INDEX  Path to the kallisto index to be constructed.

-g T2G  Path to transcript-to-gene mapping to be generated

-f1 `FASTA`  
    Path to the cDNA FASTA (standard, nac) or mismatch FASTA (kite) to be generated. Optional with ``-d``, or with ``--aa`` when no GTF file(s) are provided. Not used with ``--workflow=custom``.

**Positional Arguments (required only if `-d` is not used):**

- `fasta`: Genomic FASTA file(s), comma-delimited
- `gtf`: Reference GTF file(s), comma-delimited. Not required with ``--aa``.
- `feature`: Path to TSV containing barcodes and feature names. **kite workflow** only.
                        
**required arguments for `nac` workflow:**

-f2 `FASTA`  
    Path to the unprocessed transcripts FASTA to be generated

-c1 `T2C`  
    Path to generate cDNA transcripts-to-capture

-c2 `T2C`  
    Path to generate unprocessed transcripts-to-capture

**optional arguments:**

-h, --help  Show a help message and exit 

--temp TMP  Override default temporary directory

--keep-tmp  Keep temporary files

--verbose  Print debugging information

--include-attribute KEY:VALUE  
    Only process GTF entries that have the provided KEY:VALUE attribute. May be specified multiple times.

--exclude-attribute KEY:VALUE 
    Only process GTF entires that do not have the provided KEY:VALUE attribute. May be specified multiple times.

-k K  Use this option to override the k-mer length of the index (max value: 31). Usually, the k-mer length automatically calculated by `kb` provides the best results (typically k=31, which is also the default).

-t THREADS  Number of threads to use (default: 8)

--d-list FASTA  D-list file(s) (default: the Genomic FASTA file(s) for standard/nac workflow)

--aa  Generate index from a FASTA-file containing amino acid sequences

--workflow  {standard,nac,kite,custom} 
    The type of index to create. Use `nac` for an index type that can quantify nascent and mature RNA. Use `custom` for indexing targets directly. Use `kite` for feature barcoding. (default: standard)

-d NAME  Download a pre-built kallisto index (along with all necessary files) instead of building it locally

--make-unique         Replace repeated target names with unique names
  
--overwrite           Overwrite existing kallisto index

--kallisto KALLISTO   Path to kallisto binary to use (default: /opt/anaconda3/lib/python3.13/site-packages/kb_python/bins/darwin/m1/kallisto/kallisto)

--bustools BUSTOOLS   Path to bustools binary to use (default: /opt/anaconda3/lib/python3.13/site-packages/kb_python/bins/darwin/m1/bustools/bustools)

--opt-off             Disable performance optimizations

**Output:**

* **index.idx:** A binary kallisto index file (path specified by ``-i``)
* **t2g.txt:** A two-column TSV mapping transcripts to genes (path specified by ``-g``)
* **f1:** A FASTA file of cDNA sequences (standard, nac) or mismatch sequences (kite) [path specified by ``-f1``]
* **f2:** A FASTA file of unprocessed transcript sequences (nac only) (path specified by ``-f2``)
* **c1:** A two-column TSV mapping cDNA transcripts to capture sequences (standard, nac) [path specified by ``-c1``]
* **c2:** A two-column TSV mapping unprocessed transcripts to capture sequences (nac only) [path specified by ``-c2``]

.. _kb count:

kb count     
^^^^^^^^^^^^^^^^^^^^
Generate count matrices from a set of single-cell FASTQ files

**Usage:**

.. code-block:: text

   kb count -i INDEX -g T2G -x TECHNOLOGY [arguments] [FASTQs]

**required arguments:**

-i INDEX
    Path to kallisto index
-g T2G  
    Path to transcript-to-gene mapping
-x TECHNOLOGY   
    Single-cell technology used (``kb --list`` to view). If ``x=BULK``, bulk RNA-seq quantification is performed instead. 

**positional arguments**

- `FASTQs`:
    FASTQ files. For paired-end data, list each R2 file immediately after its corresponding R1 files.

    For technology `SMARTSEQ`, sort all input FASTQs alphabetically by path and paired in order, and assign cell IDs as incrementing integers starting from zero. A single batch TSV with cell ID, read 1, and read 2 as columns can be provided to override this behavior.

    In place of listing FASTQ files, a batch TSV file with three columns (*cell ID*, *read 1*, *read 2*) can be provided to specify multiple samples (for single-end reads the batch file is formatted as (*cell ID*, *read1*)).

**required arguments for `nac` workflow:**

-c1 T2C  
    Path to mature transcripts-to-capture
-c2 T2C  
    Path to nascent transcripts-to-capture

**optional arguments**

-h, --help            Show a help message and exit

--tmp TMP             Override default temporary directory

--keep-tmp            Do not delete the tmp directory

--verbose             Print debugging information

-o OUT  Path to output directory (default: current directory)

--num                 Store read numbers in BUS file

--parity {single, paired}
    If both paired-end reads contain biological sequence, specify `paired`. Otherwise, specify `single`. (default: see ``kb --list``)
    
-w ONLIST             Path to file of on-listed barcodes to correct to. If not provided and bustools supports the technology, a pre-packaged on-list is used. Otherwise, the ``bustools allowlist`` command is used. Specify NONE to bypass barcode error correction. (``kb --list`` to view on-lists)

--exact-barcodes      Only exact matches are used for matching barcodes to on-list.

-r REPLACEMENT        Path to file of a replacement list to correct to. In the file, the first column is the original barcode and second is the replacement sequence.

-t THREADS  Number of threads to use (default: 8)

--strand {unstranded,forward,reverse}   
    Strandedness (default: see ``kb --list``)

-m MEMORY             Maximum memory used (default: 2G for standard, 4G for others)

--inleaved            Specifies that input is an interleaved FASTQ file

--aa                  Map to index generated from FASTA-file containing amino acid sequences

--workflow {standard,nac,kite,kite:10xFB}    
    Type of workflow. Use `nac` to specify a nac index for producing mature/nascent/ambiguous matrices. Use `kite` for feature barcoding. Use `kite:10xFB` for 10x Genomics Feature Barcoding technology. (default: standard)

--mm  
    Include reads that pseudoalign to multiple genes. Automatically enabled when generating a TCC matrix.

--h5ad
    Generate h5ad file from count matrix

--tcc   Generate a TCC matrix instead of a gene count matrix.

--filter {bustools} 
    Produce a filtered gene count matrix (default: bustools)

--filter-threshold THRESH  Barcode filter threshold (default: auto)

--overwrite           Overwrite existing output.bus file

--dry-run             Do a dry run (no kallisto or bustools commands executed)

--batch-barcodes      When a batch file is supplied, store sample identifiers in barcodes

--loom                Generate loom file from count matrix

--loom-names col_attrs/{name},row_attrs/{name}
    Names for `col_attrs` and `row_attrs` in loom file (default: `barcode`, `target_name`). Use ``--loom-names=velocyto`` for velocyto-compatible loom files

--sum TYPE  Produced summed count matrices (Options: none, cell, nucleus, total). Use `cell` to add ambiguous and processed transcript matrices. Use `nucleus` to add ambiguous and unprocessed transcript matrices. Use `total` to add all three matrices together. (Default: none)

--cellranger  Convert count matrices to cellranger-compatible format

--union  Take the union of all k-mer alignments (default: intersection)

--gene-names          Group counts by gene names instead of gene IDs when generating the loom or h5ad file

-N NUMREADS           Maximum number of reads to process from supplied input

--report              Generate a HTML report containing run statistics and basic plots. Using this option may cause kb to use more memory than specified with the ``-m`` option. It may also cause it to crash due to memory.

--long                Use lr-kallisto for long-read mapping
  
--threshold THRESH    Set threshold for lr-kallisto read mapping (default: 0.8)

--platform {PacBio, ONT}  
    Set platform for lr-kallisto (default: ONT)

--kallisto KALLISTO   Path to kallisto binary to use (default: /opt/anaconda3/lib/python3.13/site-packages/kb_python/bins/darwin/m1/kallisto/kallisto)

--bustools BUSTOOLS   Path to bustools binary to use (default: /opt/anaconda3/lib/python3.13/site-packages/kb_python/bins/darwin/m1/bustools/bustools)

--opt-off             Disable performance optimizations

**optional arguments for BULK and SMARTSEQ2 technologies:**
--fragment-l L        Mean length of fragments. (single-end only)
  
--fragment-s S        Standard deviation of fragment lengths. (single-end only)

--bootstraps B        Number of bootstraps to perform

--matrix-to-files     Reorganize matrix output into abundance tsv files

--matrix-to-directories
                        Reorganize matrix output into abundance tsv files across multiple directories

**Output:**

In the output directory specified by ``-o``, the following files are made:

* **kb_info.json** : A JSON file containing information about the kb run
* ``kallisto bus`` **Output Files:** `output.unfiltered.bus`, `transcripts.txt`, `matrix.ec`, `run_info.json`
* ``bustools`` **Output Files:** `output.bus`, `inspect.json`
* **counts_unfiltered folder with:**
    - **Single-Cell Count Matrices:** in Market Matrix format `cell_x_genes.mtx` or `cells_x_tcc.mtx` if ``--ttc``. For ``--workflow nac``, `cell_x_genes.mature.mtx`, `cell_x_genes.nascent.mtx`, `cell_x_genes.ambiguous.mtx`
    - **Barcode and Gene/Transcript ID Files:** `cell_x_genes.barcodes.txt`, `cell_x_genes.genes.txt`, `cell_x_genes.genes.names.txt` (or `cells_x_tcc.barcodes.txt`, `cells_x_tcc.ec.txt` if ``--ttc``)
    - If ``--h5ad`` is specified, an **h5ad file** (`adata.h5ad`) is created from the count matrix. If ``--loom`` is specified, a **loom file** (`adata.loom`) is created from the count matrix. The resulting anndata object will contain:
        
        - the full count matrix in `adata.X`. If ``--workflow nac``, `adata.X` will contain the sum of the mature, nascent, and ambiguous count matrices. If ``--TCC``, `adata.X` will contain the TCC matrix.
        - cell barcodes in `adata.obs`. If ``batch-barcodes``, artificial sample barcodes will be appended to the beginning of each cell barcode.
        - gene/transcript IDs as the `adata.var` index. If `--gene-names` is specified, gene names will be used in `adata.var` instead of gene IDs. If ``-TCC``, equivalence classes (composed of semi-colon delimited transcript IDs) will be used instead.
        - If ``--workflow nac`` is used, the mature, nascent, and ambiguous count matrices will be stored in `adata.layers` as `mature`, `nascent`, and `ambiguous`, respectively. 
    - If ``--batch-barcodes`` is specified, a file with a 16 bp pseudobarcode for each cell (``cell_x_genes.barcodes.prefix.txt``) is created.
* If ``--batch-barcodes`` is specified, two additional files are created:
    - **`matrix.cells`**: A file listing the sample IDs for each cell in the count matrix
    - **`matrix.sample.barcodes`**: A file listing the 16 bp pseudobarcodes for each sample
* If ``-r`` is specified, the corrected count matrix, barcodes, and genes files are placed in the `counts_unfiltered_modified` folder.
* If ``--report`` is specified, an HTML report (`report.html`) and Jupyter notebook (`report.ipynb`) are created containing run statistics and basic plots.
* If ``--matrix-to-files``, transcript- and gene-level abundance files in TSV and H5 format are created in the `quant_unfiltered` folder.
* If ``--matrix-to-directories``, transcript- and gene-level abundance files in TSV and H5 format are created in the `quant_unfiltered` folder. The directories inside `quant_unfiltered` have the form `abundance_1`, `abundance_2`, etc. corresponding to the samples in the order they were provided.

.. _kb extract:

kb extract
^^^^^^^^^^^^^^^^^^^^
Extract reads that were pseudoaligned to specific genes/transcripts (or extract all reads that were / were not pseudoaligned)

**Usage:**

.. code-block:: text

    kb extract [arguments] FASTQ

**required arguments:**

-i INDEX              Path to kallisto index
  
-ts, --targets TARGETS [TARGETS ...]
    Gene or transcript names for which to extract the raw reads that align to the index

**positional arguments**

- `FASTQ`: Single FASTQ file containing the sequencing reads (e.g. in case of 10x data, provide the R2 file). Sequencing technology will be treated as bulk here since barcode and UMI tracking is not necessary to extract reads.

**optional arguments**
  
-h, --help            Show a help message and exit
  
--tmp TMP             Override default temporary directory
  
--keep-tmp            Do not delete the tmp directory
  
--verbose             Print debugging information

-ttype, --target_type={gene, transcript}  
    Defines whether targets are gene or transcript names. (default: gene)
  
--extract_all         Extracts all reads that pseudo-aligned to any gene or transcript (as defined by target_type) (breaks down output by gene/transcript). Using extract_all might take a long time to run when there are a large number of genes/transcripts in the index.
  
--extract_all_fast    Extracts all reads that pseudo-aligned (does not break down output by gene/transcript; output saved in the *all* folder).
  
--extract_all_unmapped  Extracts all unmapped reads (output saved in the *all_unmapped* folder).

--mm                  Also extract reads that multi-mapped to more than one gene.

-g T2G                Path to transcript-to-gene mapping file (required when ``mm`` is false, ``--target_type=gene`` (and ``extract_all_fast`` and ``extract_all_unmapped`` is false), OR ``extract_all`` is true).

-o OUT                Path to output directory (default: current directory)

-t THREADS            Number of threads to use (default: 8)

-s, --strand {unstranded,forward,reverse} 
    Strandedness (default: unstranded)

--aa                  Map to index generated from FASTA-file containing amino acid sequences

-N NUMREADS           Maximum number of reads to process from supplied FASTQ

--kallisto KALLISTO   Path to kallisto binary to use (default: /opt/anaconda3/lib/python3.13/site-packages/kb_python/bins/darwin/m1/kallisto/kallisto)

--bustools BUSTOOLS   Path to bustools binary to use (default: /opt/anaconda3/lib/python3.13/site-packages/kb_python/bins/darwin/m1/bustools/bustools)

--opt-off             Disable performance optimizations

**Output:**
In the output directory specified by ``-o``, FASTQ files are created for each target specified with ``-ts`` containing the reads that pseudoaligned to that target. If ``--extract_all`` or ``--extract_all_fast`` is specified, FASTQ files are created containing all reads that pseudoaligned to any target in the index. If ``--extract_all_unmapped`` is specified, FASTQ files are created containing all unmapped reads.

.. _kb info:

kb info      
^^^^^^^^^^^^^^^^^^^^
Display package and citation information

**Usage:**

.. code-block:: text

    kb info

.. _kb compile:

kb compile   
^^^^^^^^^^^^^^^^^^^^
Compile **kallisto** and **bustools** binaries from source

**Usage:**

.. code-block:: text

    kb compile [arguments] [target]

**positional arguments:**

- `target`: Which binaries to compile. May be one of `kallisto`, `bustools` or `all`.

**optional arguments:**

--tmp TMP             Override default temporary directory

--keep-tmp            Do not delete the tmp directory

--verbose             Print debugging information

--view                See information about the current binaries, which are what will be used for ``kb ref`` and ``kb count``.

--remove              Remove the existing compiled binaries. Binaries that are provided with kb are never removed.

--overwrite           Overwrite the existing compiled binaries, if they exist.

-o OUT                Save the compiled binaries to a different directory. Note that if this option is specified, the binaries will have to be manually specified with ``--kallisto`` or ``--bustools`` when running ``kb ref`` or ``kb count``.

--url URL             Use a custom URL to a ZIP or tarball file containing the source code of the specified binary. May only be used with a single target.

--ref REF             Repository commmit hash or tag to fetch the source code from. May only be used with a single target.

--cmake-arguments URL  Additional arguments to pass to the cmake command. For example, to pass additional include directories, ``--cmake-arguments="-DCMAKE_CXX_FLAGS='-I /usr/include'"``