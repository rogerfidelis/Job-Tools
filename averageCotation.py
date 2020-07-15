from yahooquery import Ticker
import numpy as np
import pandas as pd
import time

paper = input("Type stock code, please: ")
print(paper)

time = time.asctime()
print(time)

paper = Ticker(paper)
paper = paper.history(period='7d',  interval = "1m")

paper = pd.DataFrame(paper)
paper = paper.tail(100) 
hundredLastClosePrice = paper["close"].tolist()
#print(hundredLastClosePrice)
average = np.average(hundredLastClosePrice)



print("average: " + str(average))



#data.to_excel("STBP3.xlsx")

