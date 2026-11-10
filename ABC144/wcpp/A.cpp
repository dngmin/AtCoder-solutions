#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    std::cout << (A < 10 and B < 10? A*B : -1);
    return 0;
}