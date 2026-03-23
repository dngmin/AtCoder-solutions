#include <iostream>

int main()
{
    int N, A = 1;
    std::cin >> N;
    for (int i = 1; i < N; i++)
    {
        for (int An = A; An >= 1; An = An/10)
        {
            A += An%10;
        }
    }
    std::cout << A << std::endl;
    return 0;
}