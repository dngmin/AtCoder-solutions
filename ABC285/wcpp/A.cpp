#include <iostream>

int main()
{
    int a, b; std::cin >> a >> b;
    std::cout << (b == a*2 || b == a*2+1? "Yes" : "No");
    return 0;
}