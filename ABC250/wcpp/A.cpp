#include <iostream>

int main()
{
    int H, W, R, C, output = 4; std::cin >> H >> W >> R >> C;
    if (R == 1) output -= 1;
    if (R == H) output -= 1;
    if (C == 1) output -= 1;
    if (C == W) output -= 1;
    std::cout << output;
    return 0;
}