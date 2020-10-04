# Retworkx Benchmarks

This repository contains benchmarks for the
[retworkx](https://github.com/Qiskit/retworkx) library. It is built using the
[airspeed velocity](https://github.com/airspeed-velocity/asv) benchmarking tool.

Benchmark results can be found here:
https://mtreinish.github.io/retworkx-bench/

## Cloning the benchmarks

The retworkx-bench repo uses git-lfs to store large graph files which are used
for benchmarking. To locally clone these file you'll need git-lfs installed
to download the large files in git lfs. You can find instructions on that
here:

https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage

## Running Benchmarks

To run the benchmarks you need to have asv installed. You can install asv with
pip by running:

```bash
pip install asv
```

Then after asv is installed from the root of this repository you can run

```bash
asv run
```

This wiill build an isolated virtualenv for running benchmarks install
the curret HEAD of the retworkx git repository and then run the benchmarks.
If this is the first time you're using asv it will ask for information about
the system you're using which will be stored as metadata for the benchmark
results.

For more details on running benchmarks and using asv you can refer to the asv
documentation:

https://asv.readthedocs.io/en/stable/using.html
