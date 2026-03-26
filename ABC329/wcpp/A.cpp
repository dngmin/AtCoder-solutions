#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    for (size_t i = 0; i < S.size(); i++)
    {
        std::cout << S[i] << ' ';
    }
    return 0;
}