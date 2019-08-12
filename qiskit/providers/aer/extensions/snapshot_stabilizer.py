# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from qiskit import QuantumCircuit
from qiskit.circuit.quantumregister import QuantumRegister
from qiskit.providers.aer.extensions import Snapshot

class SnapshotStabilizer(Snapshot):
    def __init__(self,
                 label,
                 snapshot_type='stabilizer',
                 num_qubits=0,
                 num_clbits=0,
                 params=None):
        super().__init__(label, snapshot_type, num_qubits, num_clbits, params)

def snapshot_stabilizer(self,
                        label,
                        qubits=None,
                        params=None):

    snapshot_register = Snapshot.define_snapshot_register(self, label, qubits)

    return self.append(
        SnapshotStabilizer(
            label,
            num_qubits=len(snapshot_register),
            params=params), snapshot_register)

QuantumCircuit.snapshot_stabilizer = snapshot_stabilizer
