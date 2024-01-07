#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Review
{
    double pos_average;
    int check;
    Review(double p, int c) : pos_average(p), check(c) {}
};

int main()
{
    vector<Review> reviews;
    double t = 0;
    double times = 0;
    while (1)
    {
        double p;
        int c;
        cin >> p >> c;
        if (p == 998967483)
            break;
        if (c != -1)
        {
            c == 1 ? t += 0.3 *p : t += 0.7 * p;
            c == 1 ? times += 0.3 : times += 0.7;
        }
        reviews.emplace_back(p, c);
    }
    double alpha = t / times;
    for (Review &review : reviews)
    {
        if (review.check == -1)
        {
            review.pos_average >= alpha ? review.check = 1 : review.check = 0;
        }
        cout << review.pos_average << " " << review.check << endl;
    }
    return 0;
}