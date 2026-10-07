#include <iostream>

int main()
{
    int N, M, count = 0; std::cin >> N >> M;
    while (M != 0)
    {
        M = N % M;
        count ++;
    }
    std::cout << count;
    return 0;
}