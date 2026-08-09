#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    std::cout << (S == "Hello,World!"? "AC" : "WA");
    return 0;
}