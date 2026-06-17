#include <iostream>

int main()
{
    
    int integers[101] = {0}, A, count = 0;
    for (int i = 0; i < 5; i++)
    {
        std::cin >> A;
        if (not integers[A])
        {
            integers[A] = 1;
            count += 1;
        }
    }
    std::cout << count;
    return 0;
}