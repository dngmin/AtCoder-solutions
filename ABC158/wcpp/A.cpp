#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    std::cout << (S == "AAA" or S == "BBB"? "No" : "Yes");
    return 0;
}