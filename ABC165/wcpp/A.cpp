#include <iostream>

int main()
{
    int K, A, B; std::cin >> K >> A >> B;
    int d = (B / K) * K;
    std::cout << (A <= d and d <= B? "OK" : "NG");
    return 0;
}