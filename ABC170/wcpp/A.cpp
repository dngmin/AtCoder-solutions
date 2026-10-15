#include <iostream>

int main()
{
    int i = 1, x;
    for (; i <= 5; i++)
    {
        std::cin >> x;
        if (x == 0)
        {
            std::cout << i;
            return 0;
        }
    }
}