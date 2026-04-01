#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;

    for (size_t i = 1; i < S.size(); i += 2)
    {
        if (S[i] != '0')
        {
            std::cout << "No";
            return 0;
        }
    }
    std::cout << "Yes";
    return 0;
}