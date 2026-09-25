#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (char s : S) std::cout << (s == 'A'? 'A' : '.');
    return 0;
}