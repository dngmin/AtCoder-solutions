#include <iostream>

int main()
{
    int K, X; std::cin >> K >> X;
    std::cout << (K * 500 >= X? "Yes" : "No");
    return 0;
}