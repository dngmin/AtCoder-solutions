#include <iostream>
#include <vector>

int main()
{
    int N, M; std::cin >> N >> M;
    std::vector<int> As(N);
    int A, B, output = 0;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        As[i] = A;
    }
    for (int i = 0; i < M; i++)
    {
        std::cin >> B;
        output += As[B-1];
    }
    std::cout << output;
    return 0;
}