#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    std::cout << (S[0] == S[S.size()-1]? "Yes" : "No");
    return 0;
}