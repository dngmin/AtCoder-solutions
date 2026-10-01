#include <iostream>

int main()
{
    int N, X; std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> X;
        if (X >= 0)
        {
            std::cout << "No";
            return 0;
        }
    }
    std::cout << "Yes";
    return 0;
}