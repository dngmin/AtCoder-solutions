#include <iostream>
#include <cmath>
#include <cstdio>

int main()
{
    double H; std::cin >> H;
    double L = std::sqrt((H * (12800000 + H)));
    std::printf("%.10f", L);
    return 0;
}