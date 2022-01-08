import pandas as pd
df = pd.read_csv("frauda.csv") 
df.head() 
df.type.unique()

# array(['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'],
#      dtype=object)

# Transform categorical data
df['type'] = df.type.replace({
    'PAYMENT': 0,
    'TRANSFER': 1,
    'CASH_OUT': 2,
    'DEBIT': 3,
    'CASH_IN': 4
})

df.type.head()
df.head()

############################ DATA CLEANING ############################
# remove texts so that we can create classifier
# for columns, axis = 1
df.drop(['step','nameOrig', 'nameDest', 'isFlaggedFraud'],
        axis=1, inplace=True)
# inplace = True overwrites the existing dataframe
df.head()
# until -1 as the last column is -1
x = df.iloc[:, :-1] # select all columns except last
y = df.iloc[:, -1] # select the last col

y.head()

############################ STANDARD SCALER ############################
from sklearn.preprocessing import StandardScaler
# reducing dimension to decimal points

ss = StandardScaler()
x_transformed = ss.fit_transform(x)

############################ PARTIONING ################################
# partitioning, split training vs test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x_transformed, y, test_size = 0.3, random_state =0 ) 
# random state is optional, =0 to make sure you receive the same result
# random state for consistency as it starts from same point

############################ CLASSIFIER ################################
from sklearn.svm import SVC

classifier = SVC(kernel="linear", random_state=0)
classifier.fit(x_train, y_train)

############################ PREDICTION ################################
y_pred = classifier.predict(x_test)

############################ RESULTS ###################################
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
accuracy = accuracy_score(y_test, y_pred)
accuracy

# confusion matrix
cm = confusion_matrix(y_test, y_pred)
cm

# report 
report = classification_report(y_test, y_pred)
print(report) # precision shows 1 which is good
