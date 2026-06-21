#include <iostream>

int main()
{
    char atcoder[] = "atcoder";
    int L, R; std::cin >> L >> R;
    for (int i = L-1; i < R; i++)
    {
        std::cout << atcoder[i];
    }
    return 0;
}