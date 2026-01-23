#include <iostream>
#include <stdexcept>
using int64 = long long;

int64 qe001_direct(int N) {
    int64 total = 0;
    for (int n = 1; n < N; ++n) {
        if (n % 3 == 0 || n % 5 == 0) total += n;
    }
    return total;
}

int64 sum_of_multiples(int k, int N) {
    int64 m = (N - 1) / k;
    return (int64)k * m * (m + 1) / 2;
}

int64 qe001_inclusion_exclusion(int N) {
    return sum_of_multiples(3, N) +
           sum_of_multiples(5, N) -
           sum_of_multiples(15, N);
}

int main() {
    int N = 1000;
    std::cout << qe001_inclusion_exclusion(N) << std::endl;
}
