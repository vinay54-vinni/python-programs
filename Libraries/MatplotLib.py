#Bar Graph:

import matplotlib.pyplot as plt
x = ['A','B','C','D','E']
y = [5.4,4.5,55.4,44.5,34.5]
new_colors = ['Red','Yellow','Blue','Green','Pink']

plt.title('BAR GRAPH')
plt.xlabel("person Name")
plt.ylabel('Height')
plt.bar(x,y,color=new_colors)
plt.show()



#HISTOGRAM:
import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(170,10,250)
plt.title('Histogram')
plt.hist(x)
plt.show()





#BAX PLOt:
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data_1 = np.random.normal(100,10,200)
data_2 = np.random.normal(100,10,200)
data_3 = np.random.normal(100,10,200)
data_4 = np.random.normal(100,10,200)
data = [data_1,data_2,data_3,data_4]
fig = plt.figure(figsize=(10,7))
ax = fig.add_axes([0,0,1,1])
bp = ax.boxplot(data,patch_artist = True)
plt.title('Bax Plot')
plt.show()





#PIE CHART:
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabels = ["apples","bananas","cherries","Dates"]
plt.title('Pie Chart')
plt.pie(y,labels=mylabels)
plt.legend()
plt.show()





#Scatter PLot:
import matplotlib.pyplot as plt
x1 = [10,20,30,40,50]
x2 = [5,10,15,20,25]
y1 = [40,50,60,70,80]
y2 = [4,8,16,24,32]
plt.title("Scatter PLot")
plt.scatter(x1,y1,c='red',marker = 's')
plt.scatter(x2,y2,c='Green',marker = 'o')
plt.show()