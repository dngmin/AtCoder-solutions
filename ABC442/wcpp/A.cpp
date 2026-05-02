#include <iostream>
#include <string>

int main()
{
    int output = 0;
    std::string S;
    std::cin >> S;
    for (char s : S)
    {
        if (s == 'i' | s == 'j') output += 1;
    }
    std::cout << output;
    return 0;
}