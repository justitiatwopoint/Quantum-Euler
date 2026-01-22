# Quantum Euler #1 — Hilbert Slice (3|5)

## Formal Problem Statement

Consider a quantum system with a discrete, non-degenerate spectrum of energy
eigenstates labeled by integers

n = 1, 2, 3, ...

Each eigenstate |n⟩ has energy

Eₙ = n

(in arbitrary units).

A symmetry constraint imposes the following selection rule:

A state |n⟩ is allowed if

n ≡ 0 (mod 3) or n ≡ 0 (mod 5).

All other states are forbidden and contribute zero to physical observables.

Define a symmetry-projected observable

S(N) = Σₙ₌₁ⁿ⁻¹ Eₙ · P(n),

where the projector P(n) is defined as

P(n) = 1,  if n ≡ 0 (mod 3) or (mod 5)  
P(n) = 0,  otherwise.

### Task

Compute S(1000).

### Example

For N = 10, the allowed states are

n = 3, 5, 6, 9,

so

S(10) = 3 + 5 + 6 + 9 = 23.

---

## Selection-Rule Interpretation

This problem reformulates the classical Euler multiples problem as a projection
onto a symmetry-allowed subspace of Hilbert space.

The integer label n represents a discrete energy eigenstate. The modular
conditions act as symmetry constraints selecting physically allowed states.

- n ≡ 0 (mod 3) corresponds to symmetry class A
- n ≡ 0 (mod 5) corresponds to symmetry class B
- n ≡ 0 (mod 15) corresponds to states invariant under both symmetries

The observable S(N) can be written as

S(N) = Σₙ ⟨n|Ĥ|n⟩ · P(n),

which represents the expectation value of a diagonal operator projected onto an
allowed subspace.

This structure mirrors selection rules arising from conservation laws, parity
constraints, or symmetry-protected subspaces in quantum mechanics.

---

## Reference Solution Structure

Two complementary solution strategies are used.

### Method 1: Direct Projection

Each state n from 1 to N − 1 is tested against the selection rule. If the rule is
satisfied, its energy contribution is added to the sum.

This method corresponds to an explicit Hilbert-space projection.

- Time complexity: O(N)
- Space complexity: O(1)

### Method 2: Inclusion–Exclusion (Analytic Projection)

The sum is decomposed using symmetry overlap:

S(N) = S₃ + S₅ − S₁₅,

where Sₖ is the sum of all multiples of k below N.

Each partial sum is computed using the arithmetic series formula:

Sₖ = k · m(m + 1) / 2,

with m = ⌊(N − 1) / k⌋.

This method avoids double counting and runs in constant time.

---

## Expected Result

For N = 1000, the symmetry-projected sum is

S(1000) = 233168.

