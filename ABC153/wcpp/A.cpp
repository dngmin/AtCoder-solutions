#include <iostream>

int main()
{
    int H, A; std::cin >> H >> A;
    std::cout << H/A + (H%A != 0);
    return 0;
}