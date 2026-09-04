#include <iostream>
#include <string>

int main()
{
    std::string C; std::cin >> C;
    std::cout << (C[0] == C[1] and C[0] == C[2]? "Won" : "Lost");
    return 0;
}