#include <iostream>

int main()
{
    int N, A; std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        if (A%2 == 0) std::cout << A << " ";
    }
    return 0;
}