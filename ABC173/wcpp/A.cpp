#include <iostream>

int main()
{
    int N; std::cin >> N;
    std::cout << (((N/1000) + 1) * 1000 - N) % 1000;
    return 0;
}