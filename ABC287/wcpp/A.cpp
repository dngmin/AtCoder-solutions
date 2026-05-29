#include <iostream>
#include <string>

int main()
{
    int N, result = 0;
    std::cin >> N;
    std::string S;
    for (int i = 0; i < N; i++)
    {
        std::cin >> S;
        result += (S == "For"? 1 : -1);
    }
    std::cout << (result > 0? "Yes" : "No");
    return 0;
}