#include <iostream>

int main()
{
    int N, A, X, Y; std::cin >> N >> A >> X >> Y;
    if (N <= A) std::cout << N * X;
    else std::cout << (A * X + (N - A) * Y);
    return 0;
}