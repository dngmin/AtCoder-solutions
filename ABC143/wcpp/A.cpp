#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    std::cout << (A <= 2*B? 0 : A - 2*B);
    return 0;
}