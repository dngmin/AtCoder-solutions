#include <iostream>

int main()
{
    int S_pre = -1, S;
    for (int i = 0; i < 8; i++)
    {
        std::cin >> S;
        if (S_pre > S | 100 > S | S > 675 | S%25 != 0)
        {
            std::cout << "No";
            return 0;
        }
        S_pre = S;
    }
    std::cout << "Yes";
    return 0;
}