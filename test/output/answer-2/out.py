import pandas as pd
path = 'D:\\New folder\\htdocs\\test\\input\\question-2\\main.csv'
data = pd.read_csv(path)
data.drop('user_id', inplace=True, axis=1)
data.drop('gender', inplace=True, axis=1)
data.drop('zip_code', inplace=True, axis=1)
out = data.groupby('occupation').age.agg(['min', 'max'])
out.to_csv('D:/New folder/htdocs/test/output/answer-2/main.csv',index=False)
print(out)