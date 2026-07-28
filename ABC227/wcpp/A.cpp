#include <iostream>

int main()
{
    int N, K, A; std::cin >> N >> K >> A;
    int output = (A + K - 1) % N;
    std::cout << (output? output : N);
    return 0;
}