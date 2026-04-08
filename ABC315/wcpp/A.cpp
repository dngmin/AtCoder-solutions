#include <iostream>
#include <string>

int main()
{
    std::string S, aeiou = "aeiou";
    std::cin >> S;
    for (size_t i = 0; i < S.size(); i ++)
    {
        if (aeiou.find(S[i]) == std::string::npos) std::cout << S[i];
    }
    return 0;
}