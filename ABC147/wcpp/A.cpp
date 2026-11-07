#include <iostream>

int main()
{
    int A1, A2, A3; std::cin >> A1 >> A2 >> A3;
    std::cout << (A1+A2+A3 >= 22? "bust" : "win");
    return 0;
}