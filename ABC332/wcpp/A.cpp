#include <iostream>

int main()
{
    int N, S, K, P, Q, total = 0;
    std::cin >> N >> S >> K;
    for (int i = 0; i < N;i++)
    {
        std::cin >> P >> Q;
        total += P * Q;
    }
    std::cout << (total >= S? total:total+K) << std::endl;
    return 0;
}