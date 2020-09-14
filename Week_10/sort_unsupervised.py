
            features
PCA         M  -->  N  ;  N <= M    dimensionality reduction, features ranked by importance
NMF         M  -->  N  ;  N <  M    smooth segmentation, segments are equal *
t-SNE       M  -->  2  ;            visualize data
Clustering  M  -->  1 (cat)         strict segmentation, visualize data
GMM         M  -->  p(outlier)      outlier/anomaly detection

collaborative filtering   Mi, Mj --> similarity   recommender systems *

* used this week on movie data

#-----------------------------------------------------------------------
'Unsupervised learning is a family of machine learning methods that do not require labeled data.',
'Non-negative Matrix Factorization (NMF) is an algorithm frequently used in recommender systems and customer segmentation.',
 'Principal Component Analysis (PCA) is a method for dimensionality reduction.',
 'Principal Component Analysis (PCA) is frequently used as part of a supervised learning pipeline.',
 't-SNE reduces data to two dimensions to visualize complex datasets.',
 'Most clustering algorithms are based on a distance metric e.g. Euclidean or Manhatten distance.',
 'Gaussian Mixture Models (GMM) are a generative model for detecting outliers.',
 'Outlier or anomaly detection is used to identify credit card fraud.',
 'There are many clustering method like K-means, DBSCAN or Ward.'
 'The "curse of dimensionality" is a problem that becomes worse the more features you have.',
