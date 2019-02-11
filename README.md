# classification_for_imbalanced_data

Imbalanced Classification:Imbalanced classification is a supervised learning problem where one class outnumbers other class by a large proportion. This problem is faced more frequently in binary classification problems than multi-level classification problems.

ML algorithms tend to tremble when faced with imbalanced classification data sets. Moreover, they result in biased predictions and misleading accuracies.With imbalanced data sets, an algorithm doesn’t get the necessary information about the minority class to make an accurate prediction.

The methods to solve this problem are widely known as ‘Sampling Methods’. Generally, these methods aim to modify an imbalanced data into balanced distribution using some mechanism. The modification occurs by altering the size of original data set and provide the same proportion of balance.

Below are the methods used to treat imbalanced datasets:

1.Undersampling
2.Oversampling
3.Synthetic Data Generation
4.Cost Sensitive Learning

1. Undersampling:This method works with majority class. It reduces the number of observations from majority class to make the data set balanced. This method is best to use when the data set is huge and reducing the number of training samples helps to improve run time and storage troubles.

2. Oversampling:This method works with minority class. It replicates the observations from minority class to balance the data. It is also known as upsampling.

3.Synthetic Data Generation:In simple words, instead of replicating and adding the observations from the minority class, it overcome imbalances by generates artificial data.In regards to synthetic data generation, synthetic minority oversampling technique (SMOTE) is a powerful and widely used method.

4.Cost Sensitive Learning:It does not create balanced data distribution. Instead, it highlights the imbalanced learning problem by using cost matrices which describes the cost for misclassification in a particular scenario.
