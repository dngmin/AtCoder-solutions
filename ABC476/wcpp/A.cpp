#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    std::cout << S << (S[S.size()-1] == 'e'? "r" : "er");
    return 0;
}