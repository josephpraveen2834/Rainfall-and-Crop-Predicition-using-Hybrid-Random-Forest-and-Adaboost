# -*- coding: utf-8 -*-
"""Copy of testcode_Final_Rainfall_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YhfmzbI2M4jHON_0YuarsA3_fZcgj9Sd

# Praveen
"""

from google.colab import drive
drive.mount('/content/drive')

# importing libraries
import pandas as pd
import numpy as np

# read the data in a pandas dataframe
data = pd.read_csv("/content/drive/MyDrive/Final Project/austin_weather.csv")

# drop or delete the unnecessary columns in the data.
data = data.drop(['Events', 'Date', 'SeaLevelPressureHighInches',
                  'SeaLevelPressureLowInches'], axis=1)

# some values have 'T' which denotes trace rainfall
# we need to replace all occurrences of T with 0
# so that we can use the data in our model
data = data.replace('T', 0.0)

# the data also contains '-' which indicates no
# or NIL. This means that data is not available
# we need to replace these values as well.
data = data.replace('-', 0.0)

# save the data in a csv file
data.to_csv('austin_final.csv')

import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree

import seaborn as sns
import pandas as pd
# read the cleaned data
data = pd.read_csv("/content/drive/MyDrive/Final Project/austin_weather1.csv")



# the features or the 'x' values of the data
# these columns are used to train the model
# the last column, i.e, precipitation column
# will serve as the label
#X = data.drop(['PrecipitationSumInches'], axis=1)
#data = data.drop(['Date', 'SeaLevelPressureHighInches',
                  #'SeaLevelPressureLowInches'], axis=1)
#features = data[['TempHighF','TempAvgF','TempLowF','DewPointHighF','DewPointAvgF','DewPointLowF','HumidityHighPercent','HumidityAvgPercent','HumidityLowPercent','SeaLevelPressureAvgInches','VisibilityHighMiles','VisibilityAvgMiles','VisibilityLowMiles','WindHighMPH','WindAvgMPH','WindGustMPH']]

rainfall_data = data[['SeaLevelPressureAvgInches','PrecipitationSumInches']]
#print(rainfall_data)
# Create a joint plot
sns.jointplot(data=rainfall_data, x='SeaLevelPressureAvgInches', y='PrecipitationSumInches', kind='scatter')

# Show the plot
import matplotlib.pyplot as plt
plt.show()



rainfall_data = data[['HumidityAvgPercent','PrecipitationSumInches']]
#print(rainfall_data)
# Create a joint plot
sns.jointplot(data=rainfall_data, x='HumidityAvgPercent', y='PrecipitationSumInches', kind='scatter')

# Show the plot
import matplotlib.pyplot as plt
plt.show()


rainfall_data = data[['DewPointAvgF','PrecipitationSumInches']]
#print(rainfall_data)
# Create a joint plot
sns.jointplot(data=rainfall_data, x='DewPointAvgF', y='PrecipitationSumInches', kind='scatter')

# Show the plot
import matplotlib.pyplot as plt
plt.show()

rainfall_data = data[['VisibilityAvgMiles','PrecipitationSumInches']]
#print(rainfall_data)
# Create a joint plot
sns.jointplot(data=rainfall_data, x='VisibilityAvgMiles', y='PrecipitationSumInches', kind='scatter')

# Show the plot
import matplotlib.pyplot as plt
plt.show()


rainfall_data = data[['WindAvgMPH','PrecipitationSumInches']]
#print(rainfall_data)
# Create a joint plot
sns.jointplot(data=rainfall_data, x='WindAvgMPH', y='PrecipitationSumInches', kind='scatter')

# Show the plot
import matplotlib.pyplot as plt
plt.show()

"""# RainFall Prediction Using Random Forest Classifier"""

import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
# read the cleaned data
data = pd.read_csv("/content/drive/MyDrive/Final Project/austin_weather1.csv")



# the features or the 'x' values of the data
# these columns are used to train the model
# the last column, i.e, precipitation column
# will serve as the label
#X = data.drop(['PrecipitationSumInches'], axis=1)
data = data.drop(['Date', 'SeaLevelPressureHighInches',
                  'SeaLevelPressureLowInches'], axis=1)
features = data[['TempHighF','TempAvgF','TempLowF','DewPointHighF','DewPointAvgF','DewPointLowF','HumidityHighPercent','HumidityAvgPercent','HumidityLowPercent','SeaLevelPressureAvgInches','VisibilityHighMiles','VisibilityAvgMiles','VisibilityLowMiles','WindHighMPH','WindAvgMPH','WindGustMPH']]

acc = []
model = []

target = data['Events']
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
print("Random Forest's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

"""# RainFall Prediction Using Neural Network Classifier"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# read the cleaned data
data = pd.read_csv("/content/drive/MyDrive/Final Project/austin_weather1.csv")



# the features or the 'x' values of the data
# these columns are used to train the model
# the last column, i.e, precipitation column
# will serve as the label
# X = data.drop(['PrecipitationSumInches'], axis=1)



acc = []
model = []

data = data.drop(['Date', 'SeaLevelPressureHighInches',
                  'SeaLevelPressureLowInches'], axis=1)

features = data[['TempHighF','TempAvgF','TempLowF','DewPointHighF','DewPointAvgF','DewPointLowF','HumidityHighPercent','HumidityAvgPercent','HumidityLowPercent','SeaLevelPressureAvgInches','VisibilityHighMiles','VisibilityAvgMiles','VisibilityLowMiles','WindHighMPH','WindAvgMPH','WindGustMPH']]

target = data['Events']
X=features.values
y=target.values
print(y)

# Assuming 'y' is your categorical target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(target)
print(y_encoded)
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, y_encoded, test_size=0.2, random_state=42)
#print(X_train)
# Normalize/Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create MLPClassifier model
mlp_classifier = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, activation='relu', random_state=42)

# Train the model
mlp_classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = mlp_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Generate classification report
report = classification_report(y_test, predictions)
print("Classification Report:\n", report)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(mlp_classifier, X, y, cv=5, scoring='accuracy')

"""# RainFall Prediction Using hybrid Random Forest and Adaboost Classifier Classifier"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =32)
# Initialize classifiers
rf_classifier = RandomForestClassifier(n_estimators=40, random_state=42)
ada_classifier = AdaBoostClassifier(n_estimators=100, random_state=42)

# Create a voting classifier combining RandomForest and AdaBoost
voting_classifier = VotingClassifier(estimators=[('RandomForest', rf_classifier), ('AdaBoost', ada_classifier)],
                                     voting='soft')  # Soft voting for probabilities

# Train the voting classifier
voting_classifier.fit(Xtrain, Ytrain)

# Make predictions using the voting classifier
predictions = voting_classifier.predict(Xtest)
print("Hybrid Random Forest and Adaboost Classifier" )
# Calculate accuracy
accuracy = accuracy_score(Ytest, predictions)
print(f'Test Accuracy (Voting Classifier): {accuracy * 100:.2f}%')

print(classification_report(Ytest,predictions))
# Calculate accuracy
# give a sample input to test our model
# this is a 2-D vector that contains values
# for each column in the dataset.
temphigh = int(input("Enter TempHighF : "))
tempavg = int(input("Enter TempAvgF : "))
templow = int(input("Enter TempLowF : "))
DewPointHigh = int(input("Enter DewPointHighF : "))
DewPointAvg = int(input("Enter DewPointAvgF : "))
DewPointLow = int(input("Enter DewPointLowF : "))
HumidityHigh = int(input("Enter HumidityHighPercent : "))
HumidityAvg = int(input("Enter HumidityAvgPercent : "))
HumidityLow = int(input("Enter HumidityLowPercent : "))
SeaLevelPressureAvg = float(input("Enter SeaLevelPressureAvgInches : "))
VisibilityHighMiles = int(input("Enter VisibilityHighMiles : "))
VisibilityAvgMiles = int(input("Enter VisibilityAvgMiles : "))
VisibilityLowMiles = int(input("Enter VisibilityLowMiles : "))
WindHigh = int(input("Enter WindHighMPH : "))
WindAvg = int(input("Enter WindAvgMPH : "))
WindGust = int(input("Enter WindGustMPH : "))

inp = np.array([[temphigh],[tempavg],[templow],[DewPointHigh],[DewPointAvg],[DewPointLow],[HumidityHigh],[HumidityAvg],[HumidityLow],[SeaLevelPressureAvg],[VisibilityHighMiles],[VisibilityAvgMiles],[VisibilityLowMiles],[WindHigh],[WindAvg],[WindGust]])
# inp = np.array([[56], [48], [39], [43], [36], [28], [36], [28],
#                 [43], [30.13], [10], [10], [5], [16], [6], [25]])
inp = inp.reshape(1, -1)
# print the output.
print('\nThe Rainfall Prediction For the input is:', voting_classifier.predict(inp))

# 'TempHighF'
# 'TempAvgF'
# 'TempLowF'
# 'DewPointHighF'
# 'DewPointAvgF'
# 'DewPointLowF'
# 'HumidityHighPercent'
# 'HumidityAvgPercent'
# 'HumidityLowPercent'
# 'SeaLevelPressureAvgInches'
# 'VisibilityHighMiles'
# 'VisibilityAvgMiles'
# 'VisibilityLowMiles'
# 'WindHighMPH'
# 'WindAvgMPH'
# 'WindGustMPH'

!pip install xgboost

from xgboost import XGBClassifier
xgb_classifier = XGBClassifier(n_estimators=100, random_state=42)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(target)

Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,y_encoded,test_size = 0.2,random_state =32)

xgb_classifier.fit(Xtrain, Ytrain)

# Make predictions using the voting classifier
predictions = xgb_classifier.predict(Xtest)
print("XGBoost model" )
# Calculate accuracy
accuracy = accuracy_score(Ytest, predictions)
print(f'Test Accuracy (Voting Classifier): {accuracy * 100:.2f}%')

from sklearn.model_selection import train_test_split

Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,y_encoded,test_size = 0.2,random_state =32)

rf_classifier = RandomForestClassifier(n_estimators=40, random_state=42)
ada_classifier = AdaBoostClassifier(n_estimators=100, random_state=42)
xgb_classifier = XGBClassifier(n_estimators=60, random_state=42)


# Create a voting classifier combining RandomForest and AdaBoost
voting_classifier = VotingClassifier(estimators=[('RandomForest', rf_classifier), ('AdaBoost', ada_classifier),('XGBoost',xgb_classifier)],
                                     voting='soft')  # Soft voting for probabilities

# Train the voting classifier
voting_classifier.fit(Xtrain, Ytrain)

# Make predictions using the voting classifier
predictions = voting_classifier.predict(Xtest)
print("Hybrid Random Forest and Adaboost Classifier" )
# Calculate accuracy
accuracy = accuracy_score(Ytest, predictions)
print(f'Test Accuracy (Voting Classifier): {accuracy * 100:.2f}%')

""" # Crop Recommendation"""

# importing libraries
# Crop Recommendation For Particular Rainfall
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/drive/MyDrive/Final Project/Rainfall_and_Crop.csv')

# the features or the 'x' values of the data
# these columns are used to train the model
# the last column, i.e, precipitation column
# will serve as the label Date	TempHighF	TempAvgF	TempLowF	DewPointHighF	DewPointAvgF	DewPointLowF	HumidityHighPercent	HumidityAvgPercent	HumidityLowPercent	SeaLevelPressureHighInches	SeaLevelPressureAvgInches	SeaLevelPressureLowInches	VisibilityHighMiles	VisibilityAvgMiles	VisibilityLowMiles	WindHighMPH	WindAvgMPH	WindGustMPH
df = df.drop(['Date','TempHighF','TempAvgF','TempLowF','DewPointHighF','DewPointAvgF','DewPointLowF','HumidityHighPercent','HumidityAvgPercent','HumidityLowPercent','SeaLevelPressureHighInches','SeaLevelPressureAvgInches','SeaLevelPressureLowInches','VisibilityHighMiles','VisibilityAvgMiles','VisibilityLowMiles','WindHighMPH','WindAvgMPH','WindGustMPH'], axis=1)
#X = data.drop(['PrecipitationSumInches'], axis=1)

df.head()

df.tail()

df.size

df.shape

df.columns

df['label'].unique()

df.dtypes

df['label'].value_counts()

newdf = df.copy()
newdf['label'] = label_encoder.fit_transform(newdf['label'])
print(newdf['label'])

sns.heatmap(newdf.corr(),annot=True)

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['Events'] = label_encoder.fit_transform(df['Events'])
print(df['Events'])

features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'PrecipitationSumInches','Events']]
target = df['label']
labels = df['label']

"""# Crop Recommendation Using Hybrid Random Forest and Adaboost  Classifier"""

acc = []
model = []

# Splitting into train and test data

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =52)

print('Hybrid Random Forest and Adaboost Classifier')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Initialize classifiers
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=52)
ada_classifier = AdaBoostClassifier(n_estimators=100, random_state=52)

# Create a voting classifier combining RandomForest and AdaBoost
voting_classifier = VotingClassifier(estimators=[('RandomForest', rf_classifier), ('AdaBoost', ada_classifier)],
                                     voting='soft')  # Soft voting for probabilities

# Train the voting classifier
voting_classifier.fit(Xtrain, Ytrain)

# Make predictions using the voting classifier
predictions = voting_classifier.predict(Xtest)

# Calculate accuracy
accuracy = accuracy_score(Ytest, predictions)
print(f'Test Accuracy (Voting Classifier): {accuracy * 100:.2f}%')

print(classification_report(Ytest,predictions))

# data = np.array([[104,18, 30, 23.603016, 60.3, 6.7, 140.91]])
# data = np.array([[95,21,47,27.93114233,93.56161439,6.431970877,0,0]])



# inp = [float(x) for x in input().split(',')][:8]
N = float(input("Enter the Value of Nitrogen : "))
P = float(input("Enter the Value of Phosphorus : "))
K = float(input("Enter the Value of Potassium : "))
Temp = float(input("Enter the Temperature : "))
Hum = float(input("Enter the Humidity : "))
ph = float(input("Enter the ph of the soil : "))
PSI = float(input("Enter the PrecipitationSumInches : "))
event = input("Enter the Event Type : ")

data = np.array([[N,P,K,Temp,Hum,ph,PSI,event]])
# print(data)
prediction = voting_classifier.predict(data)

print('\nRecommended Crop For Particular Rainfall')
print(prediction)



"""1# Crop Recommendation  Neural Network Classifier"""

#Neural Network Classifier

print('Neural Network Classifier')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


X=features.values
y=target.values
print(y)



y=target.values
# Assuming 'y' is your categorical target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Normalize/Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create MLPClassifier model
mlp_classifier = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, activation='relu', random_state=42)

# Train the model
mlp_classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = mlp_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Generate classification report
report = classification_report(y_test, predictions)
print("Classification Report:\n", report)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(mlp_classifier, X, y, cv=5, scoring='accuracy')

scores

# Crop Recommendation Using Random Forest Classifier

print('Random Forest Classifier')

from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
print("Random Forest's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [68.9,70.08,81.82]

# Set the figure size
# plt.figure(figsize=(18, 8))
plt.figure(figsize=(4, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('Accuracy(%)')
plt.title('Performance Evaluation (RainFall Prediction)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [65,69,80]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('Precision(%)')
plt.title('Performance Evaluation (RainFall Prediction)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [69,70,82]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('Recall(%)')
plt.title('Performance Evaluation (RainFall Prediction)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [66,69,80]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('F1-Score(%)')
plt.title('Performance Evaluation (RainFall Prediction)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

"""# Crop Recommenation Performence"""

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [99.2,98.48,99.62]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('Accuracy(%)')
plt.title('Performance Evaluation (Crop Recommendation)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [99,99,100]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('Precision(%)')
plt.title('Performance Evaluation (Crop Recommendation)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [99,98,100]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('Recall(%)')
plt.title('Performance Evaluation (Crop Recommendation)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()

# Evaluate the model on the training data
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
categories = ['1.RandomForest ', '2.Neural Network','3.Hybrid Randomforest and adaboost Classifier' ]
values = [99,98,100]

# Set the figure size
plt.figure(figsize=(18, 8))
# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Algorithm Name')
plt.ylabel('F1-Score(%)')
plt.title('Performance Evaluation (Crop Recommendation)')

# Annotate values inside the bars
for category, value in zip(categories, values):
    plt.text(category, value, str(value), ha='center', va='bottom')
# Display the chart
plt.show()



import scipy.stats as stats
columns = ['N','P','K','temperature','humidity','ph','PrecipitationSumInches','Events']
for feature in columns:
    print(feature)
    plt.figure(figsize=(15,6))
    plt.subplot(1,2,1)
    df[feature].hist()
    plt.subplot(1,2,2)
    stats.probplot(df[feature],dist="norm",plot=plt)
    plt.show()

