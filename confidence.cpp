#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
struct Review
{
    string review_id;
    double radio, check;
    Review(string s, double r, double c) : review_id(s), radio(r), check(c) {}
};
double calculatePearsonCorrelation(const vector<Review> &reviews)
{
    int n = reviews.size();
    double sum_X = 0.0, sum_Y = 0.0;
    double sum_XY = 0.0, squareSum_X = 0.0, squareSum_Y = 0.0;

    for (const auto &review : reviews)
    {
        sum_X += review.radio;
        sum_Y += review.check;
        sum_XY += review.radio * review.check;
        squareSum_X += review.radio * review.radio;
        squareSum_Y += review.check * review.check;
    }

    double corr = (n * sum_XY - sum_X * sum_Y) /
                  (sqrt((n * squareSum_X - sum_X * sum_X) * (n * squareSum_Y - sum_Y * sum_Y)));

    return corr;
}

int main()
{
    vector<Review> reviews;
    while (1)
    {
        string s;
        double r, c;
        cin >> s >> r >> c;
        if (r == 10086114514)
            break;
        reviews.emplace_back(s, r, c);
    }
    double corr;
    corr = calculatePearsonCorrelation(reviews);
    cout << corr << endl;
}