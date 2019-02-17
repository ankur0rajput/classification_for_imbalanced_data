# classification_for_imbalanced_data

Imbalanced Classification:Imbalanced classification is a supervised learning problem where one class outnumbers other class by a large proportion. This problem is faced more frequently in binary classification problems than multi-level classification problems.

ML algorithms tend to tremble when faced with imbalanced classification data sets. Moreover, they result in biased predictions and misleading accuracies.With imbalanced data sets, an algorithm doesn’t get the necessary information about the minority class to make an accurate prediction.

The methods to solve this problem are widely known as ‘Sampling Methods’. Generally, these methods aim to modify an imbalanced data into balanced distribution using some mechanism. The modification occurs by altering the size of original data set and provide the same proportion of balance.

Below are the methods used to treat imbalanced datasets:

1.Undersampling:

    -Random majority under-sampling with replacement
  
    -Extraction of majority-minority Tomek links 
  
    -Under-sampling with Cluster Centroids
  
    -NearMiss-(1 & 2 & 3) 
  
    -Condensed Nearest Neighbour
  
    -One-Sided Selection 
  
    -Neighboorhood Cleaning Rule
  
    -Edited Nearest Neighbours
  
    -Instance Hardness Threshold
  
    -Repeated Edited Nearest Neighbours
  
    -AllKNN

2.Oversampling:

    -Random minority over-sampling with replacement

    -SMOTE - Synthetic Minority Over-sampling Technique

    -bSMOTE(1 & 2) - Borderline SMOTE of types 1 and 2

    -SVM SMOTE - Support Vectors SMOTE

    -ADASYN - Adaptive synthetic sampling approach for imbalanced learning 

3.Oversampling followed by Undersampling:

    -Over-sampling followed by under-sampling

    -SMOTE + Tomek links

    -SMOTE + ENN

1.Undersampling:This method works with majority class. It reduces the number of observations from majority class to make the data set balanced. This method is best to use when the data set is huge and reducing the number of training samples helps to improve run time and storage troubles.

2.Oversampling:This method works with minority class. It replicates the observations from minority class to balance the data. It is also known as upsampling.

Final Conclusion of the project

Making predictions on this data should atleast give us ~94% accuracy. However, while working on imbalanced problems, accuracy is considered to be a poor evaluation metrics because:

1.Accuracy is calculated by ratio of correct classifications / incorrect classifications.

2.This metric would largely tell us how accurate our predictions are on the majority class (since it comprises 94% of values). But, we need to know if we are predicting minority class correctly. We’re doomed here.

3.In the end the we will select that algorithm that will give higher accuracy_score as well as higher recall_score
