#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    if (A == 0) std::cout << "Silver";
    else if (B == 0) std::cout << "Gold";
    else std::cout << "Alloy";
    return 0;
}