#include <iostream>
#include <vector>

int main()
{
    int N, X, P; std::cin >> N >> X;
    for (int i = 0; i < N; i++)
    {
        std::cin >> P;
        if (P == X) 
        {
            std::cout << i+1;
            return 0;
        }
    }
}