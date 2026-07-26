#include <iostream>
#include <string>

int main()
{
    std::string S1, S2; std::cin >> S1 >> S2;
    if (S1 == ".#" and S2 == "#.") std::cout << "No";
    else if (S1 == "#." and S2 == ".#") std::cout << "No";
    else std::cout << "Yes";
    
    return 0;
}