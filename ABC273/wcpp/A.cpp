#include <iostream>

int f(unsigned int k)
{
    if (k == 0) return 1;
    else return k * f(k-1);
}

int main()
{
    unsigned int N; std::cin >> N;
    std::cout << f(N);
    return 0;
}