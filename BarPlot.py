# bar plot

import pandas as pd
import matplotlib.pyplot as plt
  
# A dictionary which represents data
data_dict = {'name': ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'],
             'age': [20, 20, 21, 20, 21, 20],
             'math_marks': [100, 90, 91, 98, 92, 95],
             'physics_marks': [90, 100, 91, 92, 98, 95],
             'chem_marks': [93, 89, 99, 92, 94, 92]
             }
  
# creating a data frame object
df = pd.DataFrame(data_dict)
df.plot(kind='bar',
        x='name',
        y='physics_marks',
        color='green')
  
# set the title
plt.title('BarPlot')
  
# show the plot
plt.show()