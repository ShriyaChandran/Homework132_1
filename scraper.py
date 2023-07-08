import pandas as pd
import csv

df = pd.read_csv('bright_stars.csv')

df.head()

df.columns

df.columns

#Index(['Unnamed: 0', 'Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity',
       #'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],
     # dtype='object')
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

final_data = df.dropna()
df.dtypes

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = df['Gravity'].to_list()
distance = df['Distance'].to_list()

mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius, mass)

plt.title("radius & mass of the star")
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()

#converting solar mass and radius into km & kg
def convert_to_si(radius, mass):
      for i in range(0, len(radius) -1):
            radius[i] = radius[i] * 6.957e+8
            mass[i] = mass[i] * 1.989e+30

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

df["Gravity"] = gravity



            



final_data.reset_index(drop = True, inplace = True)
final_data.to_csv('final_data.csv')

final.data.info()

final_data.describe()

final_data.index()

final_data.head(5)

final_data.dtypes()