#include <iostream>

int main()
{
    int N; std::cin >> N;
    N *= 1.08;
    if (N < 206) std::cout << "Yay!";
    else if (N == 206) std::cout << "so-so";
    else std::cout << ":(";
    return 0;
}