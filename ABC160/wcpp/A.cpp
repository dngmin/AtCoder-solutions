#include <iostream>

int main()
{
    char S[7]; std::cin >> S;
    std::cout << (S[2] == S[3] and S[4] == S[5]? "Yes" : "No");
    return 0;
}