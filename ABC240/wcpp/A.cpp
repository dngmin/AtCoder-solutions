#include <iostream>

int main()
{
    int a, b; std::cin >> a >> b;
    int c = b - a;
    std::cout << (c == 1 or c == 9? "Yes" : "No");
    return 0;
}