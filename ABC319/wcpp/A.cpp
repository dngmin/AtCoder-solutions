#include <iostream>
#include <unordered_map>
#include <string>

int main()
{
    std::unordered_map<std::string,int> Legendary_Players =
    {
    {"tourist", 3858},
    {"ksun48", 3679},
    {"Benq", 3658},
    {"Um_nik", 3648},
    {"apiad", 3638},
    {"Stonefeang", 3630},
    {"ecnerwala", 3613},
    {"mnbvmar", 3555},
    {"newbiedmy", 3516},
    {"semiexp", 3481}
    };
    std::string player;
    std::cin >> player;
    std::cout << Legendary_Players[player];
    return 0;
}