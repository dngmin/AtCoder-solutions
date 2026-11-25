#include <iostream>
#include <algorithm>

int main()
{
    int P, Q, R; std::cin >> P >> Q >> R;
    std::cout << P + Q + R - std::max(std::max(P,Q),R);
    return 0;
}