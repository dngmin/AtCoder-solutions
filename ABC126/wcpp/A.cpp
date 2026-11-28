#include <iostream>
#include <string>

int main()
{
    int N, K; std::cin >> N >> K;
    std::string S; std::cin >> S;
    for (int i = 0; i < N; i++)
    {
        std::cout << (i+1 == K? char(S[i] + 32) : S[i]);
    }
    return 0;
}