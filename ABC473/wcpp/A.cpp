#include <iostream>

int main()
{
    int N; std::cin >> N;
    int sum = 0, A;
    for (int i = 1; i <= N; i++)
    {
        std::cin >> A;
        if (i > N/2) sum += A;
    }
    std::cout << sum;
    return 0;
}