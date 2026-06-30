#include <iostream>

int main()
{
    int R, C; std::cin >> R >> C;
    int C1, C2;
    for (int i = 1; i <= 2; i++)
    {
        std::cin >> C1 >> C2;
        if (R == i) std::cout << (C == 1? C1 : C2);
    }
    return 0;
}