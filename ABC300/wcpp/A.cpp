#include <iostream>

int main()
{
    int N, A, B, choice; std::cin >> N >> A >> B;
    int sum = A + B;
    for (int i = 1; i <= N; i++)
    {
        std::cin >> choice;
        if (sum == choice)
        {
            std::cout << i;
            return 0;
        }
    }
    return -1;
}