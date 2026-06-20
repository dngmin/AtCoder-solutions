#include <iostream>

int main()
{
    int X, Y, N; std::cin >> X >> Y >> N;
    std::cout << (3*X <= Y? X * N: (N/3) * Y + (N%3) * X);
    return 0;
}