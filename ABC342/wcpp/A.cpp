#include <iostream>
#include <string>

int main()
{
    std::string S;
    char standard;
    std::cin >> S;
    if (S[0] == S[1]) standard = S[0];
    else if (S[0] == S[2])
    {
        std::cout << 2;
        return 0;
    }
    else
    {
        std::cout << 1;
        return 0;
    }

    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] != standard)
        {
            std::cout << i+1;
            return 0;
        }
    }
}