#include <iostream>

int main()
{
    int N, X; std::cin >> N >> X;
    std::cout << (char)(65 + (X-1)/N);
    return 0;
}