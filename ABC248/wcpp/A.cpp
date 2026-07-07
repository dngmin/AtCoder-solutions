#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (int i = 48; i < 58; i++)
    {
        if (S.find((char)i) == std::string::npos)
        {
            std::cout << (char)i;
            break;
        }
    }
    return 0;
}