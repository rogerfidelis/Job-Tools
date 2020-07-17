from yahooquery import Ticker

# Informações financeiras
petr = Ticker("PETR4.SA")     # Coleta dados
petr = petr.income_statement()# Chama função de Demonstração de resultados
petr = petr.transpose()        # Transpoe a matriz
petr.columns = petr.iloc[0,:] # Renomeia colunas
petr = petr.iloc[2:,:-1]      # Seleciona dados
petr = petr.iloc[:, ::-1]     # Inverte colunas
print(petr)