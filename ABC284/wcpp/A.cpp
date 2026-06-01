#include <iostream>
#include <vector>
#include <string>

int main()
{
    size_t N; std::cin >> N;
    std::vector<std::string> S(N);
    for (int i = 0; i < N; i++) std::cin >> S[N-1-i];
    for (std::string s : S) std::cout << s << std::endl;
    return 0;
}