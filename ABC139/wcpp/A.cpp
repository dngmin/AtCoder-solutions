#include <iostream>

int main()
{
    char S[4], T[4]; std::cin >> S >> T;
    int count = 0;
    for (int i = 0; i < 3; i++)
    {
        count += (S[i] == T[i]? 1 : 0);
    }
    std::cout << count;
    return 0;
}