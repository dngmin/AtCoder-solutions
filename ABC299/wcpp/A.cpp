#include <iostream>
#include <string>

int main()
{
    int N; std::string S;
    bool isopen = false;
    std::cin >> N >> S;
    for (char s : S)
    {
        if (s == '|')
        {
            isopen = (!isopen? true : false);
        }
        else if (s == '*')
        {
            std::cout << (isopen? "in" : "out");
            return 0;
        }
    }
    return -1;
}