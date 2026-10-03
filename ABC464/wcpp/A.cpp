#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    int East = 0, West = 0;
    for (char s : S)
    {
        if (s == 'E') East += 1;
        else West += 1;
    }
    std::cout << (East > West? "East" : "West");
    return 0;
}