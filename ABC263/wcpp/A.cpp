#include <iostream>

int main()
{
    int card, mul = 1;
    int cards[14] = {0};
    for (int i = 0; i < 5; i++)
    {
        std::cin >> card;
        cards[card] += 1;
    }
    for (int card : cards)
    {
        mul *= (card > 0? card : 1);
    }
    std::cout << (mul == 6? "Yes" : "No");
    return 0;
}