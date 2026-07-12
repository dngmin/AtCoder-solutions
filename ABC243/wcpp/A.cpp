#include <iostream>

int main()
{
    int V, A, B, C; std::cin >> V >> A >> B >> C;
    while (1)
    {
        if (V < A)
        {
            std::cout << 'F';
            break;
        }
        V -= A;

        if (V < B)
        {
            std::cout << 'M';
            break;
        }
        V -= B;

        if (V < C)
        {
            std::cout << 'T';
            break;
        }
        V -= C;
    }
    return 0;
}