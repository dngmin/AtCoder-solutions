#include <iostream>

int main()
{
    int N, P, rival, need = 0;
    std::cin >> N >> P;
    for (int i = 1; i < N; i ++)
    {
        std::cin >> rival;
        if (rival - P + 1 > need) need = rival - P + 1;
    }
    std::cout << need;
    return 0;
}