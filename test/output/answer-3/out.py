import pandas as pd
path = 'D:\\New folder\\htdocs\\test\\input\\question-3\\main.csv'
data = pd.read_csv(path)
selection = data[['Team','Yellow Cards','Red Cards']]
out = selection.sort_values(by=['Red Cards','Yellow Cards'], ascending=False)
out.to_csv('D:/New folder/htdocs/test/output/answer-3/main.csv',index=False)
print(out)