Introduction
============

This website provides manuals, tutorials, and information on how to use the kallisto-bustools suite of tools for bulk and single-cell RNA sequencing (scRNA-seq) pre-processing and analysis. These tools include:

* `kallisto <https://github.com/pachterlab/kallisto>`_: kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-seq data, or more generally, of target sequences using high-throughput sequencing reads. It is based on the concept of pseudoalignment, which enables rapid assessment of read compatibility with targets without conventional alignment. The pseudoalignment approach maintains key information required for accurate quantification, making kallisto not only extremely fast but also highly accurate and robust to errors in reads. The input to kallisto consists of reads, an index built from the target sequences that is to be used for pseudoalignment, and optionally a technology string that specifies where various features are located in the input reads. Importantly, kallisto is compatible with the `seqspec <https://github.com/pachterlab/seqspec>`_ format, which can be used to describe a wide variety of single-cell genomics assays, and seqspec can be used to construct the technology strings required to run kallisto. The output of kallisto can be reported in BUS format, a file format suitable for storing both bulk and scRNA-seq pseudoalignments.

* `bustools <https://github.com/BUStools/bustools>`_: bustools works with files in the BUS (Barcode, UMI, Set) format and is designed to support modular workflows in data processing for both bulk and scRNA-seq data. The BUS format includes a binary representation of barcode and UMI sequences derived from scRNA-seq reads, along with equivalence classes determined by pseudoalignment to a reference transcriptome. BUS files act as useful checkpoints during bulk or single-cell RNA-seq processing, enabling efficient handling of complex scRNA-seq data. The bustools program includes a suite of commands that can be used to work with BUS files.

* `kb-python <https://github.com/pachterlab/kb_python>`_: kb-python serves as a wrapper for kallisto and bustools, simplifying the usage of these tools, including the generation of an index needed by kallisto for pseudoalignment. kb-python packages the kallisto and bustools binaries for convenience.

Background
^^^^^^^^^^^

The kallisto project began in August 2013 when Nicolas Bray, then a postdoctoral researcher in the Pachter Lab, had the insight that the sufficient statistics for RNA-seq quantification did not depend on read alignment, but only on compatibility of reads with transcripts. This distinction led him to the idea of pseudoalignment, which was published in:

**Nicolas L Bray, Harold Pimentel, Páll Melsted, and Lior Pachter.** "Near-optimal probabilistic RNA-seq quantification." *Nature Biotechnology*, 34, 525–527 (2016). `doi:10.1038/nbt.3519 <https://doi.org/10.1038/nbt.3519>`_

The paper also contains details of the methodology underlying the first implementation of pseudoalignment in kallisto, and extensive benchmarks of the initial version of the program.

The kallisto pseudoalignment framework was extended to single-cell RNA-seq with the introduction of the BUS format, and the bustools program for working with BUS files, in the pair of papers:

**P. Melsted, V. Ntranos, and L. Pachter.** "The Barcode, UMI, Set format and BUStools." *Bioinformatics*, btz279, 2019. `doi:10.1093/bioinformatics/btz279 <https://academic.oup.com/bioinformatics/article/35/21/4472/5487515>`_

**P. Melsted, M. Booeshaghi, F. Gao, J. Beltrame, H. Lu, K. Hjorleifsson, V. Gehring, and L. Pachter.** "Modular and efficient pre-processing of single-cell RNA-seq." *Nature Biotechnology*, 39, 813–818 (2021). `doi:10.1038/s41587-021-00870-2 <https://www.nature.com/articles/s41587-021-00870-2>`_

The Melsted, Booeshaghi et al. paper describes how kallisto can generate BUS format files from single-cell RNA-seq technologies. With bustools, BUS files can be used for barcode error correction, unique molecular identifier (UMI) deduplication, and efficient creation of transcript compatibility count (TCC) and gene count matrices. The paper provides extensive benchmarks of kallisto demonstrating state-of-the-art performance for single-cell RNA-seq.

In 2024, Sina Booeshaghi formalized the library and read structure of single-cell genomics assays in the seqspec format, published in:

**Booeshaghi, A. S., Chen, X., Pachter, L.** "A machine-readable specification for genomics assays." *Bioinformatics*, 40, 4 (2024). `doi:10.1093/bioinformatics/btae168 <https://doi.org/10.1093/bioinformatics/btae168>`_

seqspec can now be used to generate the information needed by kallisto to correctly extract barcode, UMI, and other information needed to process genomics data, making kallisto immediately useful for dozens of popular bulk and single-cell genomics assays.

In 2023, Delaney Sullivan and Kristján Hjörleifsson implemented major updates to kallisto and bustools, including improving the data structures used and making numerous performance upgrades. Their work is described in:

**Hjörleifsson, K. E., Sullivan, D. K., Swarna, N. P., Holley, G., Melsted, P., & Pachter, L.** "Accurate quantification of single-cell and single-nucleus RNA-seq transcripts using distinguishing flanking k-mers." *bioRxiv*, 2022. `doi:10.1101/2022.12.02.518832 <https://www.biorxiv.org/content/10.1101/2022.12.02.518832v3>`_

The use cases for the kallisto and bustools programs, along with a wrapper called kb-python that simplifies their use, are described in the following paper:

**Sullivan, D. K., Min, K. H. (Joseph), Hjörleifsson, K. E., Luebbert, L., Holley, G., Moses, L., Gustafsson, J., Bray, N. L., Pimentel, H., Booeshaghi, A. S., Melsted, P., & Pachter, L.** "kallisto, bustools and kb-python for quantifying bulk, single-cell and single-nucleus RNA-seq." *Nature Protocols*, (2024). `doi:10.1038/s41596-024-01057-0 <https://www.nature.com/articles/s41596-024-01057-0>`_

The kallisto-bustools suite of tools has also been extended for *translated* pseudoalignment, which has many applications, including the identification of viral sequences in genomics datasets. These improvements to kallisto are described here:

**Luebbert, L., Sullivan, D. K., Carilli, M., Hjörleifsson, K. E., Winnett, A. V., Chari, T., & Pachter, L.** "Efficient and accurate detection of viral sequences at single-cell resolution reveals putative novel viruses perturbing host gene expression." *bioRxiv*, 2023. `doi:10.1101/2023.12.11.571168v2 <https://www.biorxiv.org/content/10.1101/2023.12.11.571168v2>`_
