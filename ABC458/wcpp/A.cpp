#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    int S_size = S.size(), N; std::cin >> N;
    std::cout << S.substr(N,S_size - N - N);
    return 0;
}