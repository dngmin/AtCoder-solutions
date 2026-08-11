#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    for (int C = 0; C < 256; C++)
    {
        if ((A^C) == B)
        {
            std::cout << C;
            return 0;
        }
    }
}