.. _Advanced Installation:

Installing from source
======================

Although the kallisto and bustools binaries already come packaged within kb-python, perhaps the simple ``pip install`` isn't working for you and you wish to install kallisto and bustools separately.


Precompiled binaries
^^^^^^^^^^^^^^^^^^^^

If you want to download the binaries separately, you can visit:

* https://github.com/pachterlab/kallisto/releases to obtain the kallisto binaries
* https://github.com/BUStools/bustools/releases to obtain the bustools binaries. 


Compiling from source
^^^^^^^^^^^^^^^^^^^^^

If you want to install the kallisto and bustools software separately from source, you can do the following:

For kallisto:

.. code-block:: shell

  git clone --branch v0.50.1 https://github.com/pachterlab/kallisto
  cd kallisto
  mkdir build
  cmake ..
  make
  make install

For bustools:

.. code-block:: shell

  git clone --branch v0.43.2 https://github.com/BUStools/bustools
  cd kallisto
  mkdir build
  cmake ..
  make
  make install

If you want to install the latest version (not just specific versions), you can omit the --branch version specification from the above commands (e.g. omit "--branch 0.43.2" when running git clone).

.. tip::

  If you get permission denied errors from the *make install* step (e.g. because you don't have sudo privileges), you can simply use the local binaries. Those binaries will be located at ``kallisto/build/src/kallisto`` and ``bustools/build/src/bustools`` after compiling from source per the instructions above, and you can execute those binaries directly. Additionally, if you'd like, you can add those src directories to your path for easy access to running those binaries.

.. warning::

  Installing kallisto from source in the manner above will not allow the production of h5ad files when doing bulk RNA-seq quantification. The h5ad files may be required for certain bulk RNA-seq differential gene expression programs. To enable generation of h5ad files, please modify the cmake command to be: ``cmake .. -DUSE_HDF5=ON``

.. note::

  By default, kallisto will only support *k*-mer lengths up to 31. In order to enable support for *k*-mer lengths up to 63 (which is optimal for long-read data), please modify the cmake command to be ``cmake .. -DMAX_KMER_SIZE=64``. Important: Always use a fresh installation when doing this (i.e. redownload the source code from github) because files that exist from a previous build may cause the binary to be generated incorrectly.


Using the binaries
^^^^^^^^^^^^^^^^^^

You can also run the ``kb ref`` and ``kb count`` commands using your kallisto and bustools binaries downloaded separately or installed from source:

.. code-block:: shell

  kb ref --kallisto=/path/to/kallisto --bustools=/path/to/bustools ...
  kb count --kallisto=/path/to/kallisto --bustools=/path/to/bustools ...



