#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (int i = 0; i < S.size() / 2; i++)
    {
        std::cout << S[2*i + 1] << S[2*i];
    }
    return 0;
}