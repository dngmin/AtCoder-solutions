#include <iostream>

int main()
{
    int A, B, C; std::cin >> A >> B;
    C = A + B;
    if (C >= 15 and B >= 8) std::cout << 1;
    else if (C >= 10 and B >= 3) std::cout << 2;
    else if (C >= 3) std::cout << 3;
    else std::cout << 4;
    return 0;
}