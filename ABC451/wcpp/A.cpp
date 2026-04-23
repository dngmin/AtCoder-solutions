#include <iostream>
#include <string>

int main()
{
    std::string S;
    std::cin >> S;
    std::cout << (S.size()%5 == 0? "Yes" : "No");
    return 0;
}