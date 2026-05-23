#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (char s : S) std::cout << (char)(s - 32);
    return 0;
}