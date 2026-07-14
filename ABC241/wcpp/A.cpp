#include <iostream>
#include <vector>

int main()
{
    std::vector<int> A(10);
    int n = 0;
    for (int i = 0; i < 10; i++)
    {
        std::cin >> A[i];
    }
    for (int i = 0; i < 3; i++)
    {
        n = A[n];
    }
    std::cout << n;
    return 0;
}