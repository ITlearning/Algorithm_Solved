#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> temps;

    for (int i = 0; i < commands.size(); i++)
    {
        int begin = commands[i][0] - 1;
        int end = commands[i][1];
        int ans = commands[i][2] - 1;
        for (; begin < end; begin++)
        {
            temps.push_back(array[begin]);
        }
        sort(temps.begin(), temps.end());

        answer.push_back(temps[ans]);

        temps.clear();
    }
    return answer;
}