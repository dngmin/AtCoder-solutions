#include <iostream>

int main()
{
    int A, B, C; std::cin >> A >> B >> C;
    std::cout << (B + C <= A? 0 : B + C - A);
    return 0;
}