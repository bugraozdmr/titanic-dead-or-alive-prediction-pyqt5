import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score
import pandas as pd
from xgboost import XGBClassifier




# setimi cekiyorum
df = pd.read_csv("real_corrected_df")

df.drop(["parch","fare"],axis=1,inplace=True)

#setimi bagimli bagimsiz ayiriyorum

y = df["survived"]
X = df.drop("survived",axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                         test_size=0.30,
                                         random_state=42)

'''  
# train kismi parametreleri sectik
                                    
xgb_cv = GridSearchCV(model , xgb_params,
cv=10 , n_jobs=-1,
verbose=2)

xgb_cv.fit(X_train , y_train)

#40 mins                                         

xgb_cv.best_params_
                                         
'''

# calisacak buralar
# alpha degeri eklenmeden sorunlu calisiyordu
# parametre onemli
xgb_tuned = XGBClassifier(
    alpha=0,
    colsample_bytree=0.8,
    gamma=0,
    learning_rate=0.01,
    max_depth=3,
    min_child_weight=5,
    n_estimators=500,
    scale_pos_weight=1,
    subsample=0.6

).fit(X_train , y_train)


# 0.7454545454545455 dogruluk orani



def dondur(a,b,c,d):

    # float olmasi sart
    data_to_predict = [a,b,c,d]

    # parantezle cagirmayinca bile hata aldim
    # [data_to_predict]
    # Tahmin yapmak
    prediction = xgb_tuned.predict([data_to_predict])



    print(prediction[0])
    return prediction[0]


