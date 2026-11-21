#include <iostream>

int main()
{
    int N, A, B; std::cin >> N >> A >> B;
    std::cout << std::min(A*N,B);
    return 0;
}