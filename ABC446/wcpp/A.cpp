#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    S[0] += 32;
    std::cout << "Of" << S;
    return 0;
}