#include <iostream>

int main()
{
    int a, b, c; std::cin >> a >> b >> c;
    std::cout << (std::min(a,c) <= b and b <= std::max(a,c)? "Yes" : "No");
    return 0;
}