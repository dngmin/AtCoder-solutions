#include <iostream>

int main()
{
    int output = 1, N; std::cin >> N;
    for (int i = 0; i < N; i++) output *= 2;
    std::cout << output;
    return 0;
}