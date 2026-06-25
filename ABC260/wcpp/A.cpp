#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    if (S[0] != S[1] and S[0] != S[2]) std::cout << S[0];
    else if (S[1] != S[0] and S[1] != S[2]) std::cout << S[1];
    else if (S[2] != S[0] and S[2] != S[1]) std::cout << S[2];
    else std::cout << -1;
    return 0;
}