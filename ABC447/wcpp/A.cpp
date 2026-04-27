#include <iostream>

int main()
{
    int N, M;
    std::cin >> N >> M;
    std::cout << (N >= 2*M - 1? "Yes" : "No");
    return 0;
}