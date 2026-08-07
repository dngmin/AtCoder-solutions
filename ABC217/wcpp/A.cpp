#include <iostream>
#include <string>

int main()
{
    std::string S, T; std::cin >> S >> T;
    char s, t;
    size_t size = (S.size() > T.size()? S.size() : T.size());
    for (int i = 0; i < size; i++)
    {
        s = S[i]; t = T[i];
        if (s < t) std::cout << "Yes";
        else if (s > t) std::cout << "No";
        else continue;
        return 0;
    }
}