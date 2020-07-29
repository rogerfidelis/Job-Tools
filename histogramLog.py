from yahooquery import Ticker
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

# calling stock code
print("Ex: abev3.sa")
paper = input("Type stock code, please: ")

# Input amount of minutes
amountMinutes =int(input("Type amountMinutes, please: "))
print("You choose: "+paper)

# Printting date and time 
time = time.asctime()
print("time: "+time)

# Running code
paper = Ticker(paper)
paper = paper.history(period='7d',  interval = "1m")

paper = pd.DataFrame(paper)
paper = paper.tail(amountMinutes) 
lastClosePriceRange = paper["close"].tolist()

a = lastClosePriceRange
plt.hist(a)
#dy=[]

#for i in lastClosePriceRange:
 #   dx = i
  #  y = a
   # dy = np.diff(y)/dx

#dy =dy 

# setting y
# y = dy
#plt.hist(dy)

# Show the plot
plt.show()