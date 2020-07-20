# Retworkx Benchmarks

This repository contains benchmarks for the
[retworkx](https://github.com/Qiskit/retworkx) library. It is built using the
[airspeed velocity](https://github.com/airspeed-velocity/asv) benchmarking tool.

Benchmark results can be found here:
https://mtreinish.github.io/retworkx-bench/

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
