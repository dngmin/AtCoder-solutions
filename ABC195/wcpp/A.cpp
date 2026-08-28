#include <iostream>

int main()
{
    int M, H; std::cin >> M >> H;
    std::cout << (H%M == 0? "Yes" : "No");
    return 0;
}