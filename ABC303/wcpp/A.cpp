#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S, T;
    std::cin >> N >> S >> T;
    for (int i = 0; i < N; i++)
    {
        if (S[i] == T[i] || S[i]*T[i] == '1'*'l' || S[i]*T[i] == '0'*'o') continue;
        else
        {
            std::cout << "No";
            return 0;
        }
    }
    std::cout << "Yes";
    return 0;
}