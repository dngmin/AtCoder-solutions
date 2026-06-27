#include <iostream>

int main()
{
    int K; std::cin >> K;
    int hh = 21, mm = 0;
    if (K >= 60)
    {
        hh += 1;
        K -= 60;
    }
    std::cout << hh << ':';
    if ( K >= 10) std::cout << K;
    else std::cout << '0' << K;
    return 0;
}