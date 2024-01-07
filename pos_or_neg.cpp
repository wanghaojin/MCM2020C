#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Review
{
    string review_id;
    double pos_average;
    int check;
    double star_rating;
    double radio;
    Review(string r, double p, int c, double s) : review_id(r), pos_average(p), check(c), star_rating(s), radio(0) {}
};

int main()
{
    vector<Review> reviews;
    double t = 0;
    double times = 0;
    while (1)
    {
        string r;
        double p, s;
        int c;
        cin >> p >> c >> s >> r;
        if (p == 998967483)
            break;
        if (c != -1)
        {
            c == 1 ? t += 0.3 *p : t += 0.7 * p;
            c == 1 ? times += 0.3 : times += 0.7;
        }
        reviews.emplace_back(r, p, c, s);
    }
    double alpha = t / times;
    for (Review &review : reviews)
    {
        if (review.check == -1)
        {
            review.pos_average >= alpha ? review.check = 1 : review.check = 0;
        }
        review.radio = review.pos_average / review.star_rating;
        cout << review.review_id << " " << review.radio << endl;
    }
    return 0;
}