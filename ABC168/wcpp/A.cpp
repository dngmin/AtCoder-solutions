#include <iostream>

int main()
{
    int N; std::cin >> N;
    N = N%10;
    if (N == 3) std::cout << "bon";
    else if (N == 0 or N == 1 or N == 6 or N == 8) std::cout << "pon";
    else std::cout << "hon";
    return 0;
}