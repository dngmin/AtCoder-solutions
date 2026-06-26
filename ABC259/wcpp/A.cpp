#include <iostream>

int main()
{
    int N, M, X, T, D; std::cin >> N >> M >> X >> T >> D;
    if (M < X) std::cout << T - (X - M) * D;
    else std::cout << T;
    return 0;
}