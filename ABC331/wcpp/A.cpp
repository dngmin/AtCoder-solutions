#include <iostream>

int main()
{
    int M, D, y, m, d;
    std::cin >> M >> D >> y >> m >> d;
    d += 1;
    if (d > D)
    {
        m += 1;
        d = 1;
        if (m > M)
        {
            y += 1;
            m = 1;
        }
    }
    std::cout << y << ' ' << m << ' ' << d << std::endl;
    return 0;
}