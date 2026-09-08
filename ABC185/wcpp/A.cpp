#include <iostream>
#include <algorithm>

int main()
{
    int A1, A2, A3, A4; std::cin >> A1 >> A2 >> A3 >> A4;
    std::cout << std::min(A1, std::min(A2, std::min(A3,A4)));
    return 0;
}