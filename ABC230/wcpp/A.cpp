#include <iostream>

int main()
{
    int N; std::cin >> N;
    std::cout << "AGC0";
    if (N >= 42) std::cout << N+1;
    else if (N < 10) std::cout << '0' << N;
    else std::cout << N;
    return 0;
}