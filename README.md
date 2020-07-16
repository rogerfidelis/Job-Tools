# Job-Tools
Job Tools for improve estimatives of the stock market.

print("Ex: abev3.sa")                           # the code to find enterprise on stock market through yahoofinance
paper = input("Type stock code, please: ")
print("You choose: "+paper)

time = time.asctime()
print("time: "+time)

paper = Ticker(paper)
paper = paper.history(period='7d',  interval = "1m")

paper = pd.DataFrame(paper)
paper = paper.tail(100) 
hundredLastClosePrice = paper["close"].tolist()
#print(hundredLastClosePrice)
average = np.average(hundredLastClosePrice)

print("average: " + str(average))
