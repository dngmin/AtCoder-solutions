#include <iostream>

int main()
{
    int N, output = 0; std::cin >> N;
    if (N <= 125) std::cout << 4;
    else if (N <= 211) std::cout << 6;
    else std::cout << 8;
    return 0;
}