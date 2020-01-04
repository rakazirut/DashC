#Task1
import numpy as np
import pandas as pd

#Task2
np.random.seed(101)

#Task3
arr = np.random.randint(0,101,[100,5])

#Task4
pd.DataFrame(data=arr)

#Task5
pd.DataFrame(data=arr, columns=['f1','f2','f3','f4','label'])

#Task6
df = pd.DataFrame(data=np.random.randint(0,101,[50,4]), columns='A B C D'.split())
print(df)