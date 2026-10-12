#include <iostream>

int main()
{
    int A, B, C; std::cin >> A >> B >> C;
    std::cout << (A != B and B == C? "Yes" : "No");
    return 0;
}