#include <iostream>

int main()
{
    int K; std::cin >> K;
    int output = 'A';
    for (int i = 0; i < K; i++)
    {
        std::cout << (char)(output+i);
    }
    return 0;
}