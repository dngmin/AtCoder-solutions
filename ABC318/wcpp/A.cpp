#include <iostream>

int main()
{
    int N, M, P;
    std::cin >> N >> M >> P;
    std::cout << (N < M? 0 : 1 + (N-M)/P);
    return 0;
}