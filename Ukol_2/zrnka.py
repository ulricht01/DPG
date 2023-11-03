import pandas as pd

seznam = []
for i in range(0,65):
    x = (2**i)
    seznam.append(x)

x = pd.DataFrame(data = seznam, columns=['Výsledky'])

print(x.head(5))
print(x.tail(5))
