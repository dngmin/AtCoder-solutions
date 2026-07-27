#include <iostream>

int main()
{
    int S, T, X; std::cin >> S >> T >> X;
    if (S > T) T+= 24;
    if (S > X) X+= 24;
    std::cout << (S <= X and X < T? "Yes" : "No");
    return 0;
}