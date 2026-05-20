#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    int N; std::cin >> N;
    std::vector<std::string> words = {"and", "not", "that", "the", "you"};
    std::string W;
    for (int i = 0; i < N; i++)
    {
        std::cin >> W;
        if (std::find(words.begin(), words.end(), W) != words.end())
        {
            std::cout << "Yes";
            return 0;
        }
    }
    std::cout << "No";
    return 0;
}