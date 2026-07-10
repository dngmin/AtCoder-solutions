#include <iostream>

int main()
{
    int A, B, C, D; std::cin >> A >> B >> C >> D;
    if (A < C or (A == C and B <= D)) std::cout << "Takahashi";
    else std::cout << "Aoki";
    return 0;
}