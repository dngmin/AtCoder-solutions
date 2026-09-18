#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    if (S == "RRR") std::cout << 3;
    else if (S == "SSS") std::cout << 0;
    else if (S == "RRS" or S == "SRR") std::cout << 2;
    else std::cout << 1;
    return 0;
}