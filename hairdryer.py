import pandas as pd
import math
import matplotlib.pyplot as plt
from collections import defaultdict
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

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
        # print("vine:",self.vine)
        # print("verified_purchase:",self.verified_purchase)
    
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
        
        
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [WordNetLemmatizer().lemmatize(token) for token in tokens if token not in stopwords.words('english')]
    return ' '.join(tokens)

def f(x):
    if x<0 or x > 1:
        assert("Error")
    elif x <= 0.3:
        return math.sin(math.pi/2 * (x - 0.3) /0.3) + 1.1
    else:
        return 2*math.sin(math.pi/2 * (x-0.3)/0.7) + 1.1
    
def process_tsv_file(file_path):
    df = pd.read_csv(file_path, sep='\t')
    reviews = []
    for _, row in df.iterrows():
        review = Review(*row)
        review.deal()
        review.get_weight()
        reviews.append(review)
    return reviews

def find_cluster_names(tfidf_matrix, kmeans_model, product_titles):
    order_centroids = kmeans_model.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf_vectorizer.get_feature_names_out()
    cluster_names = {}
    for i in range(num_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :3]]
        cluster_names[i] = ' '.join(top_terms)
    return cluster_names

tsv_path = 'Problem_C_Data/hair_dryer.tsv'

reviews = process_tsv_file(tsv_path)
reviews_by_product = defaultdict(list)
for review in reviews:
    reviews_by_product[review.product_title].append(review)

# weighted_scores = {}
# for product_title, reviews in reviews_by_product.items():
#     total_weight = sum(review.weight for review in reviews)
#     weighted_score = sum(review.weight * review.star_rating for review in reviews) / total_weight
#     weighted_scores[product_title] = weighted_score

# product_titles = list(weighted_scores.keys())
# tfidf_vectorizer = TfidfVectorizer(preprocessor=preprocess)
# tfidf_matrix = tfidf_vectorizer.fit_transform(product_titles)

# num_clusters = 20 
# kmeans = KMeans(n_clusters=num_clusters)
# kmeans.fit(tfidf_matrix)
# clusters = kmeans.labels_
# clustered_reviews = defaultdict(list)
# for i, cluster_label in enumerate(clusters):
#     product_title = product_titles[i]
#     for review in reviews_by_product[product_title]:
#         clustered_reviews[cluster_label].append(review)
# cluster_average_scores = {}
# for cluster_label, cluster_reviews in clustered_reviews.items():
#     total_weight = sum(review.weight for review in cluster_reviews)
#     weighted_score = sum(review.weight * review.star_rating for review in cluster_reviews) / total_weight
#     cluster_average_scores[cluster_label] = weighted_score

# cluster_names = find_cluster_names(tfidf_matrix, kmeans, product_titles)

# sorted_clusters = sorted(cluster_average_scores.items(), key=lambda item: item[1], reverse=True)
# plt.figure(figsize=(15, 10))
# cluster_labels = [cluster_names[label] for label, _ in sorted_clusters]
# average_scores = [score for _, score in sorted_clusters]

# plt.barh(cluster_labels, average_scores, color='blue')
# plt.xlabel('Weighted Average Score')
# plt.ylabel('Product Cluster')
# plt.title('Weighted Average Scores by Product Cluster')
# plt.tight_layout()
# plt.savefig('result/clustered_weighted_average_scores.png')
# plt.show()