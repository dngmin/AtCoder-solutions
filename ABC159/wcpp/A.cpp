#include <iostream>

int main()
{
    int N, M; std::cin >> N >> M;
    std::cout << (N * (N-1) + M * (M-1)) / 2;
    return 0;
}