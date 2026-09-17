#include <iostream>

int main()
{
    int N, X, T; std::cin >> N >> X >> T;
    std::cout << (N % X == 0? N/X : N/X+1) * T;
    return 0;
}