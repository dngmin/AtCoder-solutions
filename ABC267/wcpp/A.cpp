#include <iostream>
#include <string>

int main()
{
    std::string S; std::cin >> S;
    if (S == "Monday") std::cout << 5;
    else if (S == "Tuesday") std::cout << 4;
    else if (S == "Wednesday") std::cout << 3;
    else if (S == "Thursday") std::cout << 2;
    else if (S == "Friday") std::cout << 1;
    return 0;
}