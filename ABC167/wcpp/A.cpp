#include <iostream>
#include <string>

int main()
{
    std::string S, T; std::cin >> S >> T;
    std::cout << (S.size() + 1 == T.size() and S == T.substr(0, S.size())? "Yes" : "No");
    return 0;
}