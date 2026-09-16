#include <iostream>

int main()
{
    int D, T, S; std::cin >> D >> T >> S;
    std::cout << (S * T >= D? "Yes" : "No");
    return 0;
}