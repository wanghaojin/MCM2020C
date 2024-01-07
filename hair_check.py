import pandas as pd
import math
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import stopwords

# 定义Review类，并加入review_id属性
class Review:
    def __init__(self, marketplace, customer_id, review_id, product_id, product_parent, product_title, product_category, star_rating, helpful_votes, total_votes, vine, verified_purchase, review_headline, review_body, review_date):
        self.marketplace = marketplace
        self.customer_id = customer_id
        self.review_id = review_id
        self.product_id = product_id
        self.product_parent = product_parent
        self.product_title = product_title
        self.product_category = product_category
        self.star_rating = star_rating
        self.helpful_votes = helpful_votes
        self.total_votes = total_votes
        self.vine = vine
        self.verified_purchase = verified_purchase
        self.review_headline = review_headline
        self.review_body = review_body
        self.review_date = review_date
        self.negative_votes = self.total_votes - self.helpful_votes
        self.weight = 1
        self.alpha1 = 1
        self.alpha2 = 1
        self.check = 0.3

    def deal(self):
        self.vine = 1 if self.vine == "Y" else 0
        self.verified_purchase = 1 if self.verified_purchase == "Y" else 0
    
    def get_weight(self):
        if self.total_votes != 0:
            if self.helpful_votes == 0:
                self.check = 1/self.total_votes
            else:
                self.check = 1 - (math.e * self.total_votes)/(self.helpful_votes * math.exp(self.helpful_votes))
            self.check = min(max(self.check, 0), 1)
        self.alpha1 = f(self.check)
        self.alpha2 = 3 if self.vine == 1 else 1
        self.weight = self.weight * self.alpha1 * self.alpha2

def f(x):
    if x < 0 or x > 1:
        assert("Error")
    elif x <= 0.3:
        return math.sin(math.pi/2 * (x - 0.3) /0.3) + 1.1
    else:
        return 2 * math.sin(math.pi/2 * (x - 0.3) / 0.7) + 1.1
    
def process_tsv_file(file_path):
    df = pd.read_csv(file_path, sep='\t')
    reviews = []
    for _, row in df.iterrows():
        review = Review(*row)
        review.deal()
        review.get_weight()
        reviews.append(review)
    return reviews

# 处理TSV文件并输出每一行的review_id和check
tsv_path = 'Problem_C_Data/hair_dryer.tsv'
reviews = process_tsv_file(tsv_path)

# 输出每一行的review_id和check
for review in reviews:
    print(f"{review.review_id} {review.check}")

