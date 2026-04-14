#include <iostream>

int main()
{
    int A, B;
    std::cin >> A >> B;
    std::cout << ((B-A == 1 & A != 3 & A != 6)? "Yes" : "No");
    return 0;
}