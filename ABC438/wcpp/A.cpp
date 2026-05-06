#include <iostream>

int main()
{
    int D, F;
    std::cin >> D >> F;
    while (F <= D) F += 7;
    std::cout << F - D;
    return 0;
}