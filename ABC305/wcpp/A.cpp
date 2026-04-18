#include <iostream>

int main()
{
    int N;
    std::cin >> N;
    std::cout << (N%5 >= 3? 5 * (N/5) + 5 : 5 * (N/5));
    return 0;
}