#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    std::cout << (A <= B and B <= A * 6? "Yes" : "No");
    return 0;
}