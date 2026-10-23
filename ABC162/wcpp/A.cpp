#include <iostream>
#include <string>

int main()
{
    std::string N; std::cin >> N;
    for (char n : N)
    {
        if (n == '7')
        {
            std::cout << "Yes";
            return 0;
        }
    }
    std::cout << "No";
    return 0;
}