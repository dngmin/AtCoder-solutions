#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (int i = 0; i < 6 / S.size(); i++)
    {
        std::cout << S;
    }
    return 0;
}