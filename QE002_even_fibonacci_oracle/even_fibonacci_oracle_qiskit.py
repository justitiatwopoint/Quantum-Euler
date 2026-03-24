try:
    from qiskit import QuantumCircuit
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Qiskit is not installed in this Python environment.\n"
        "Install it with:\n"
        "  python -m pip install \"qiskit>=1\"\n"
        "Then run this file again."
    ) from exc


def even_fibs_upto(limit: int) -> list[int]:
    a, b = 1, 2
    values = []

    while a <= limit:
        if a % 2 == 0:
            values.append(a)
        a, b = b, a + b

    return values


def mark_basis_state_phase(
    circuit: QuantumCircuit,
    value: int,
    data_qubits: list[int],
    ancilla_qubit: int,
) -> None:
    bits = format(value, f"0{len(data_qubits)}b")[::-1]

    for index, bit in enumerate(bits):
        if bit == "0":
            circuit.x(data_qubits[index])

    circuit.h(ancilla_qubit)
    circuit.mcx(data_qubits, ancilla_qubit)
    circuit.h(ancilla_qubit)

    for index, bit in enumerate(bits):
        if bit == "0":
            circuit.x(data_qubits[index])


def even_fibonacci_oracle(num_qubits: int) -> QuantumCircuit:
    limit = (2**num_qubits) - 1
    marked_values = even_fibs_upto(limit)

    circuit = QuantumCircuit(num_qubits + 1, name="Uf_even_fib")
    data_qubits = list(range(num_qubits))
    ancilla_qubit = num_qubits

    for value in marked_values:
        mark_basis_state_phase(circuit, value, data_qubits, ancilla_qubit)

    return circuit


if __name__ == "__main__":
    oracle = even_fibonacci_oracle(6)
    print("Marked even Fibonacci values:", even_fibs_upto(63))
    print(oracle.draw(output="text"))
