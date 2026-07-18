#include <iostream>

int main()
{
    long N; std::cin >> N;
    std::cout << (N == static_cast<int32_t>(N)? "Yes" : "No");
    return 0;
}