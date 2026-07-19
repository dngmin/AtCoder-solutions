#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    int a, b; std::cin >> a >> b;
    a -= 1;
    b -= 1;
    for (int i = 0; i < S.size(); i++)
    {
        if (i == a) std::cout << S[b];
        else if (i == b) std::cout << S[a];
        else std::cout << S[i];
    }
    return 0;
}