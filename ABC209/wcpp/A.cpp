#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    std::cout << (A > B? 0 : B - A + 1);
    return 0;
}