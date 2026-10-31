#include <iostream>
#include <string>

int main()
{
    std::string S, T; std::cin >> S >> T;
    int A, B; std::cin >> A >> B;
    std::string U; std::cin >> U;
    A -= S == U; B-= T == U;
    std::cout << A << ' ' << B;
    return 0;
}