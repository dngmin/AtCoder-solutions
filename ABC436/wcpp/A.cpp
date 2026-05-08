#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;
    std::cin >> N >> S;
    std::cout << std::string(N-S.size(),'o') << S;
    return 0;
}