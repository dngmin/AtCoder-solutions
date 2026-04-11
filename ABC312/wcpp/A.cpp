#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<std::string> chords = {"ACE","BDF","CEG","DFA","EGB","FAC","GBD"};
    std::string S;
    std::cin >> S;
    for (std::string chord : chords)
    {
        if (S == chord)
        {
            std::cout << "Yes";
            return 0;
        }
    }
    std::cout << "No";
    return 0;
}