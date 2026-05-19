#include <iostream>
#include <string>

int main()
{
    int N; std::string S;
    std::cin >> N >> S;
    char before = S[0];
    for (int i = 1; i < N; i++)
    {
        if (before == S[i])
        {
            std::cout << "No";
            return 0;
        }
        before = S[i];
    }
    std::cout << "Yes";
    return 0;
}