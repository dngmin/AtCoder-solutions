#include <iostream>

int main()
{
    int N, P, Q, D;
    std::cin >> N >> P >> Q;
    int minimum = P;
    for (int i = 0; i < N; i++)
    {
        std::cin >> D;
        if (D + Q < minimum) minimum = D + Q;
    }
    std::cout << minimum;
    return 0;
}