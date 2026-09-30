#include <iostream>

int main()
{
    int H, W; std::cin >> H >> W;
    std::cout << (W * 10000>= 25 * H * H? "Yes" : "No");
    return 0;
}