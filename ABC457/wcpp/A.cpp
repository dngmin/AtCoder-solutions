#include <iostream>
#include <vector>

int main()
{
    int N, X; std::cin >> N;
    std::vector<int> vectorA(N);
    for (int i = 0; i < N; i++) std::cin >> vectorA[i];
    std::cin >> X;
    std::cout << vectorA[X-1];
    return 0;
}