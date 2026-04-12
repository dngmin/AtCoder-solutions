#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;
    bool A = false, B = false, C = false;
    std::cin >> N >> S;
    for (int i = 0; i< N; i++)
    {
        if (S[i] == 'A') A = true;
        else if (S[i] == 'B') B = true;
        else if (S[i] == 'C') C = true;
        if (A & B & C)
        {
            std::cout << i+1;
            return 0;
        }
    }
}