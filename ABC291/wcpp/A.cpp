#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    for (int i = 0; i < S.size(); i++)
    {
        if (static_cast<int>(S[i]) < 97)
        {
            std::cout << i+1;
            return 0;
        }
    }
}