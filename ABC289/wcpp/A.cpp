#include <iostream>
#include <string>

int main()
{
    std::string s; std::cin >> s;
    for (char c : s)
    {
        std::cout << (c == '0'? 1 : 0);
    }
    return 0;
}