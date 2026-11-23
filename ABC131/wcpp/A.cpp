#include <iostream>

int main()
{
    char S[5]; std::cin >> S;
    std::cout << (S[0] != S[1] and S[1] != S[2] and S[2] != S[3]? "Good" : "Bad");
    return 0;
}