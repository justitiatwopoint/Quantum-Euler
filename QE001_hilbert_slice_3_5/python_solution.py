"""
Quantum Euler #1 — Hilbert Slice (3|5)

Compute the symmetry-projected energy sum:

    S(N) = sum_{n=1}^{N-1} n * P(n)

where P(n) = 1 if n is divisible by 3 or 5, else 0.

Two methods are provided:
1) Direct projection (O(N))
2) Inclusion–exclusion analytic sum (O(1))
"""

from __future__ import annotations


def qe001_direct(N: int) -> int:
    """
    Directly iterate over n = 1..N-1 and apply the selection rule.
    Time: O(N), Space: O(1)
    """
    if N <= 1:
        return 0

    total = 0
    for n in range(1, N):
        if (n % 3 == 0) or (n % 5 == 0):
            total += n
    return total


def _sum_of_multiples(k: int, N: int) -> int:
    """
    Sum of multiples of k strictly below N:
        k + 2k + 3k + ... + mk, where mk <= N-1
    Let m = floor((N-1)/k). Then:
        sum = k * m(m+1)/2
    """
    if k <= 0:
        raise ValueError("k must be a positive integer.")
    if N <= 1:
        return 0

    m = (N - 1) // k
    return k * m * (m + 1) // 2


def qe001_inclusion_exclusion(N: int) -> int:
    """
    Analytic method using inclusion–exclusion:
        S(N) = S3 + S5 - S15
    Time: O(1), Space: O(1)
    """
    return _sum_of_multiples(3, N) + _sum_of_multiples(5, N) - _sum_of_multiples(15, N)


def main() -> None:
    N = 1000

    direct = qe001_direct(N)
    analytic = qe001_inclusion_exclusion(N)

    print(f"Quantum Euler #1 — Hilbert Slice (3|5)")
    print(f"N = {N}")
    print(f"Direct:   {direct}")
    print(f"Analytic: {analytic}")

    # Sanity check: both methods must match
    if direct != analytic:
        raise RuntimeError("Mismatch between direct and analytic methods!")

    # Expected classic value
    expected = 233168
    if analytic != expected:
        raise RuntimeError(f"Unexpected result: got {analytic}, expected {expected}")

    print("OK Result matches expected value (233168).")


if __name__ == "__main__":
    main()
