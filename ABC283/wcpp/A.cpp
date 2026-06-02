#include <iostream>

int main()
{
    int A, B, output = 1; std::cin >> A >> B;
    for (int i = 0; i < B; i++)
    {
        output *= A;
    }
    std::cout << output;
    return 0;
}