#include <iostream>
#include <string>

int main()
{
    int N; std::string S;
    bool good = false, poor = false;
    std::cin >> N >> S;
    for (int i = 0; i < N; i++)
    {
        if (S[i] == 'o') good = true;
        else if (S[i] == 'x') poor = true;
    }
    std::cout << (good && !poor? "Yes" : "No");
    return 0;
}