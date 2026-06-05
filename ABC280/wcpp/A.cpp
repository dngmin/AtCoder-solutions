#include <iostream>
#include <string>

int main()
{
    int H, W, output = 0; std::cin >> H >> W;
    std::string S;
    for (int i = 0; i < H; i++)
    {
        std::cin >> S;
        for (char s : S)
        {
            output += (s == '#'? 1 : 0);
        }
    }
    std::cout << output;
}