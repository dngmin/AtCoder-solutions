#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    if (A >= 13) std::cout << B;
    else if (A <= 5) std::cout << 0;
    else std::cout << B / 2;
    return 0;
}