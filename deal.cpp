#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>

int main()
{
    std::unordered_map<std::string, double> hair_check_data;
    std::string line, review_id;
    double radio, check_value;

    // 读取hair_check.in的数据
    while (std::getline(std::cin, line))
    {
        std::istringstream iss(line);
        if (iss >> review_id >> check_value)
        {
            hair_check_data[review_id] = check_value;
        }
    }

    // 重定向标准输入到result.out文件
    freopen(nullptr, "r", stdin);

    // 读取result.out的数据并合并
    while (std::getline(std::cin, line))
    {
        std::istringstream iss(line);
        if (iss >> review_id >> radio)
        {
            auto it = hair_check_data.find(review_id);
            if (it != hair_check_data.end())
            {
                std::cout << review_id << " " << radio << " " << it->second << std::endl;
            }
            else
            {
                std::cout << review_id << " " << radio << " -1" << std::endl; // 如果没有找到对应的review_id
            }
        }
    }

    return 0;
}
