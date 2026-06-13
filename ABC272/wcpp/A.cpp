#include <iostream>

int main()
{
    int N, A, total = 0; std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        total += A;
    }
    std::cout << total;
    return 0;
}