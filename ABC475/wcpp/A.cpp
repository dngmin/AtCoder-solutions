#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (int i = 0; i < S.size(); i++)
    {
        std::cout << S[i];
        if (i == S.size() - 1) return 0;
        std::cout << 'o';
    }
}