#include <iostream>
#include <string>

int main()
{
    int output = -1;
    std::string S; std::cin >> S;
    for (size_t i = 0; i < S.size(); i++)
    {
        if (S[i] == 'a') output = i + 1; 
    }
    std::cout << output;
    return 0;
}