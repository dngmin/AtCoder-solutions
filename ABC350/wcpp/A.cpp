#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    int numbering = std::stoi(S.substr(3));
    std::cout << (1 < numbering && numbering < 350 && numbering != 316? "Yes":"No");
    return 0;
}