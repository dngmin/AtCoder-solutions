#include <iostream>

int main()
{
    int S, W; std::cin >> S >> W;
    std::cout << (W >= S? "unsafe" : "safe");
    return 0;
}