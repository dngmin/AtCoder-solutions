#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;
    bool delete_o = true;
    std::cin >> N >> S;
    for (char s : S)
    {
        if (delete_o)
        {
            if (s == 'o') continue;
            else delete_o = false;
        }
        std::cout << s;
    }
    return 0;
}