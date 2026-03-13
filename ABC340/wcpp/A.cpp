#include <iostream>

int main()
{
    int A, B, D;
    std::cin >> A >> B >> D;
    for (A; A <= B; A += D)
    {
        std::cout << A << " ";
    }
    return 0;
}