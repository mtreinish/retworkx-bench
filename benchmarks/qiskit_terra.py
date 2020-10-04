# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from qiskit.compiler import transpile
from qiskit.test.mock import FakeRochester
from qiskit.circuit.library import QuantumVolume


class QiskitTranspilerBenchmarks:
    params = [0, 1, 2, 3]
    param_names = ['transpiler optimization level']
    version = '0.15.1'
    timeout = 240

    def setup(self, _):
        self.backend = FakeRochester()
        self.circuit = QuantumVolume(53, seed=42)
        self.circuit.measure_all()

    def time_transpile(self, level):
        transpile(self.circuit, backend=self.backend, seed_transpiler=4242,
                  optimization_level=level)

    def peakmem_transpile(self, level):
        transpile(self.circuit, backend=self.backend, seed_transpiler=4242,
                  optimization_level=level)
