#include <iostream>

int main()
{
    int A, B, C; std::cin >> A >> B >> C;
    A += C;
    std::cout << (A > B? "Takahashi" : "Aoki");
    return 0;
}