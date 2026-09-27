#include <iostream>

int main()
{
    int N; std::cin >> N;
    for (int i = 1; i <= N; i++)
    {
        if (i % 3 == 0) std::cout << "Fizz";
        else std::cout << i;
        std::cout << "\n";
    }
    return 0;
}