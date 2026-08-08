#include <iostream>
#include <string>

int main()
{
    std::string XY; std::cin >> XY;
    int Y = int(XY[XY.size()-1]);
    char sign;
    if (Y >= int('7')) sign = '+';
    else if (Y >= int('3')) sign = ' ';
    else sign = '-';
    std::cout << XY.substr(0,XY.size()-2) << sign;
    return 0;
}