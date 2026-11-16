#include <iostream>
#include <string>

int main()
{
    int a; std::cin >> a;
    std::string s; std::cin >> s;
    std::cout << (a >= 3200? s : "red");
    return 0;
}