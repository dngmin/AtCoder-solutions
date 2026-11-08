#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<std::string> week = {"###", "SAT", "FRI", "THU", "WED" ,"TUE", "MON", "SUN"};
    std::string S; std::cin >> S;
    for (int i = 1; i < 8; i++)
    {
        if (S == week[i])
        {
            std::cout << i;
            return 0;
        }
    }
}