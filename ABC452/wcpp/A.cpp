#include <iostream>
#include <vector>

int main()
{
    std::vector<int> m = {1, 3, 5, 7, 9}, d = {7, 3, 5, 7, 9};
    int M, D;
    std::cin >> M >> D;
    for (int i = 0; i < 5; i++)
    {
        if (M == m[i] & D == d[i])
        {
            std::cout << "Yes";
            return 0;
        }
    }
    std::cout << "No";
    return 0;
}