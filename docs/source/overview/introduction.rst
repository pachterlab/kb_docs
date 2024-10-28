Introduction
============

This website provides manuals, tutorials, and information on how to use the kallisto-bustools suite of tools for bulk and single-cell RNA sequencing (scRNA-seq) pre-processing and analysis. These tools include:

* `kallisto <https://github.com/pachterlab/kallisto>`_: kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-seq data, or more generally, of target sequences using high-throughput sequencing reads. It is based on the concept of pseudoalignment, which enables rapid assessment of read compatibility with targets without conventional alignment. The pseudoalignment approach maintains key information required for accurate quantification, making kallisto not only extremely fast but also highly accurate and robust to errors in reads.

   The input to kallisto consists of reads, an index built from the target sequences that is to be used for pseudoalignment, and optionally a technology string that specifies where various features are located in the input reads. Importantly, kallisto is compatible with the `seqspec <https://github.com/pachterlab/seqspec>`_ format, which can be used to describe a wide variety of single-cell genomics assays, and seqspec can be used to construct the technology strings required to run kallisto. The output of kallisto can be reported in BUS format, a file format suitable for storing both bulk and scRNA-seq pseudoalignments.

* `bustools <https://github.com/BUStools/bustools>`_: bustools works with files in the BUS (Barcode, UMI, Set) format and is designed to support modular workflows in data processing for both bulk and scRNA-seq data. The BUS format includes a binary representation of barcode and UMI sequences derived from scRNA-seq reads, along with equivalence classes determined by pseudoalignment to a reference transcriptome. BUS files act as useful checkpoints during bulk or single-cell RNA-seq processing, enabling efficient handling of complex scRNA-seq data. The bustools program includes a suite of commands that can be used to work with BUS files.

* `kb-python <https://github.com/pachterlab/kb_python>`_: kb-python serves as a wrapper for kallisto and bustools, simplifying the usage of these tools, including the generation of an index needed by kallisto for pseudoalignment. kb-python packages the kallisto and bustools binaries for convenience.
