import pandas as pd
path = 'D:\\New folder\\htdocs\\test\\input\\question-1\\main.csv'
data = pd.read_csv(path)
data['Year'] = (10 * (data['Year'] // 10))
out = data.groupby('Year').sum()
out.to_csv('D:/New folder/htdocs/test/output/answer-1/main.csv',index=False)
print(out)