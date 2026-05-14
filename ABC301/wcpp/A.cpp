#include <iostream>
#include <string>

int main()
{
    int N, T = 0, A = 0, i = 0;
    std::string S;
    std::cin >> N >> S;
    for (; i < N; i++)
    {
        if (S[i] == 'T') T += 1;
        else A += 1;
    }
    if (T == A) std::cout << (S[i-1] == 'A'? "T" : "A");
    else std::cout << (T > A? "T" : "A");
    return 0;
}