#include <iostream>
#include <vector>

int main()
{
    int N, P, Q, R, S, A;
    std::cin >> N >> P >> Q >> R >> S;
    std::vector<int> A_list(100);
    for (int i = 0; i < N; i++)
    {
        std::cin >> A; A_list[i] = A;
    }
    for (int i = 0; i < N; i++)
    {
        if (P-1 <= i && i <= Q-1)
        {
            std::cout << A_list[i + R - P];
        }
        else if(R-1 <= i && i <= S-1)
        {
            std::cout << A_list[i -R + P];
        }
        else
        {
            std::cout << A_list[i];
        }
        std::cout << " ";
    }
    return 0;
}