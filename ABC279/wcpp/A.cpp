#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    int output = 0;
    for (char s : S)
    {
        output += (s == 'v'? 1 : 2);
    }
    std::cout << output;
    return 0;
}