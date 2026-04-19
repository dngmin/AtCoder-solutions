#include <iostream>
#include <vector>
#include <string>

int main()
{
    int N, A, youngest = 1e9, start;
    std::string S;
    std::vector<std::string> player;
    std::vector<int> year;
    std::cin >> N;

    for (int i = 0; i < N; i++)
    {
        std::cin >> S >> A;
        player.push_back(S);
        if (A < youngest)
        {
            youngest = A;
            start = i;
        }
    }
    for (int i = 0; i < N; i++)
    {
        std::cout << player[(start+i)%N] << std::endl;
    }
    return 0;
}