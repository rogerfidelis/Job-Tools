from yahooquery import Ticker

# financial report
petr = Ticker("PETR4.SA")        # Pick up data
petr = petr.income_statement()   # Call income statement function
petr = petr.transpose()          # Transpor matrix
petr.columns = petr.iloc[0,:]    # Rename columns
petr = petr.iloc[2:,:-1]         # Select data
petr = petr.iloc[:, ::-1]        # Invert columns
print(petr)
