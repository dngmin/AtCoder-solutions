#include <iostream>
#include <string>


int main()
{
    int N;
    std::string S;
    std::cin >> N >> S;
    for (int i = 1; i < N; i++)
    {
        if ((S[i] == 'a' && S[i-1] == 'b') || (S[i] == 'b' && S[i-1] == 'a'))
        {
            std::cout << "Yes";
            return 0;
        }
    }
    std::cout << "No";
    return 0;
}