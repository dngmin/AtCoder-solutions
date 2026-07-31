#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    std::cout << (S[S.size()-1] == 'r'? "er" : "ist");
    return 0;
}