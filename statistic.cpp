#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <map>
#include <algorithm>
#include <cctype>

using namespace std;

bool sortbysec(const pair<string, int> &a, const pair<string, int> &b)
{
    return (a.second > b.second);
}

string processWord(string word)
{
    transform(word.begin(), word.end(), word.begin(),
              [](unsigned char c)
              { return tolower(c); });
    word.erase(remove_if(word.begin(), word.end(), ::ispunct), word.end());

    return word;
}

int main()
{
    map<string, int> wordCount;
    string word;

    while (cin >> word)
    {
        if (word == ";")
            break;
        word = processWord(word);
        wordCount[word]++;
    }

    vector<pair<string, int>> vec;
    for (const auto &it : wordCount)
    {
        vec.push_back(it);
    }

    sort(vec.begin(), vec.end(), sortbysec);

    for (const auto &it : vec)
    {
        cout << it.first << " " << it.second << endl;
    }

    return 0;
}
