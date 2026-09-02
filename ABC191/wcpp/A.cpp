#include <iostream>

int main()
{
    int V, T, S, D; std::cin >> V >> T >> S >> D;
    std::cout << (V*T <= D and D <= V*S? "No" : "Yes");
    return 0;
}