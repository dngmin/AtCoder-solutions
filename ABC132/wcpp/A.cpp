#include <iostream>
#include <string>
#include <algorithm>

int main()
{
    std::string S; std::cin >> S;
    std::sort(S.begin(),S.end());
    std::cout << (S[0] == S[1] and S[1] != S[2] and S[2] == S[3]? "Yes" : "No");
    return 0;
}