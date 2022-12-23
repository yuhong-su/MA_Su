import matplotlib.pyplot as plt
import pandas as pd
## command to install all the packages
## pip3 install -r requirements.txt

## run the project 
## python3 start.py



# plt.plot([1,2,3,4],[1,4,9,16])
# plt.ylabel('y numbers')
# plt.xlabel('x numbers')

# plt.show()
data = pd.read_excel('/home/baohui/Desktop/thesis_project/data/sample.xlsx')
df = pd.DataFrame(data, columns=['product_name','price'])
print(df)