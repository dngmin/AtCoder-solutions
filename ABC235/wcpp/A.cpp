#include <iostream>

int main()
{
    int abc; std::cin >> abc;
    int h = abc/100, t = (abc%100)/10, o = abc%10;
    int tho = h + t + o;
    std::cout << tho*111;
    return 0;    
}