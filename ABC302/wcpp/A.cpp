#include <iostream>

int main()
{
    long long A, B, count = 0; std::cin >> A >> B;
    std::cout << (A % B == 0? A/B : A/B + 1);
    return 0;
}