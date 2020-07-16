# Job-Tools
Job Tools for improve estimatives of the stock market.
print("Ex: abev3.sa")
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
