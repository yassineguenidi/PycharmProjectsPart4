import numpy as np # linear algebra
import pandas as pd # data processing

data=pd.read_csv("train_credit.csv")
data.head(10)
data['Credit_History']=data['Credit_History'].fillna(data['Credit_History'].median())
data['LoanAmount']=data['LoanAmount'].fillna(data['LoanAmount'].median())
data = data.drop(columns=['Loan_ID']) ## Dropping Loan ID
dummy_Loan_status = pd.get_dummies(data['Loan_Status'], prefix = "Approve",drop_first=True)
frames = [data,dummy_Loan_status]
frames
data_train = pd.concat(frames, axis = 1)
data_train = data_train.drop(columns = ['Loan_Amount_Term', 'Gender', 'Married', 'Dependents', 'Education','Self_Employed', 'Property_Area','Loan_Status'])

"""# *Lets work on testing dataset..*"""

dataTest=pd.read_csv("test_credit.csv")
dataTest['LoanAmount']=dataTest['LoanAmount'].fillna(dataTest['LoanAmount'].median())
dataTest['Credit_History']=dataTest['Credit_History'].fillna(dataTest['Credit_History'].median())
dataTest = dataTest.drop(columns=['Loan_ID']) ## Dropping Loan ID
df_test = dataTest.drop(columns = [ 'Gender','Loan_Amount_Term', 'Married', 'Dependents', 'Education','Self_Employed', 'Property_Area'])

Final_df=pd.concat([data_train,df_test],axis=0)
Final_df['Approve_Y']
Train_df=Final_df.iloc[:614,:]
Test_df=Final_df.iloc[614:,:]

X=Train_df.drop(['Approve_Y'],axis=1)
y=Train_df['Approve_Y']

from sklearn.ensemble import RandomForestClassifier ,AdaBoostClassifier,BaggingClassifier,ExtraTreesClassifier,GradientBoostingClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=4)
from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
X_train[['ApplicantIncome','CoapplicantIncome','LoanAmount']]=scaler.fit_transform(X_train[['ApplicantIncome','CoapplicantIncome','LoanAmount']])
X_train=pd.DataFrame(X_train)
X_test[['ApplicantIncome','CoapplicantIncome','LoanAmount']]=scaler.transform(X_test[['ApplicantIncome','CoapplicantIncome','LoanAmount']])
X_test=pd.DataFrame(X_test)
from sklearn.metrics import confusion_matrix, classification_report
RFC = RandomForestClassifier(criterion = 'gini',
  max_features= 'auto',
  min_samples_leaf= 5,
  min_samples_split= 4,
  n_estimators= 100,
  oob_score= True,
  random_state= 1)
RFC.fit(X_train,y_train)

y_pred = RFC.predict(X_test)
import pickle
# save the model to disk
filename = 'finalized_model.sav' 
pickle.dump(RFC, open('model2.pkl','wb'))

# load the model from disk
loaded_model = pickle.load(open('model2.pkl', 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
model = pickle.load(open('model2.pkl','rb'))
print(model.predict(X_test))
print(model.predict([[-0.462307,	0.094875,	-0.001219,	1.0]]))
def pred(a1,a2,a3,a4):
  df1=pd.DataFrame(np.array([[a1,a2,a3,a4]]) ,columns=X.columns)
  df2=X.append(df1,ignore_index = True)
  print(df2.shape)
  df2[['ApplicantIncome','CoapplicantIncome','LoanAmount']]=scaler.fit_transform(df2[['ApplicantIncome','CoapplicantIncome','LoanAmount']])
  df2=pd.DataFrame(df2)
  y=df2.tail(1)
  return int(model.predict(y))

if(pred(5849	,0.0	,128.0,	1.0)==1):
  print("felicitation vous etes eligible au credit")
else :
  print("Desolé vous n'etes pas eligible au credit")


