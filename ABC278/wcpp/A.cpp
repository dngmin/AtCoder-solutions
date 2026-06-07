#include <iostream>
#include <vector>

int main()
{
    int N, K, A; std::cin >> N >> K;
    std::vector<int> A_;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        A_.push_back(A);
    }
    for (int i = 0; i < K; i++) A_.push_back(0);
    for (int i = K; i < N+K; i++) std::cout << A_[i] << " ";
    return 0;
}