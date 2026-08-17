#include <iostream>
#include <algorithm>

int main()
{
    int A, B, C; std::cin >> A >> B >> C;
    std::cout << A + B + C - std::min({A, B, C});
    return 0;
}