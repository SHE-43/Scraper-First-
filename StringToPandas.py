import numpy as np
import pandas as pd

a = "This is the land of humans"
b = "We live on this very land"
c = "No one should leave this alone"

list_a = a.split(" ")
list_b = b.split(" ")
list_c = c.split(" ")

# First let's do it column wise, and then row wise.

df = pd.DataFrame({'a': list_a, 'b':list_b, 'c':list_c}, index=[x for x in range(1,len(list_a) + 1)])
print(df)

for x in df.loc[0:, 'a']:
    print(x, end=" ")

print(list(map(print, list(df.loc[0:, 'a']))))

print()

print(" ".join(list(df.loc[0:, 'a'])))

# def taker(x):
#     abc = d;

a = "I We You".split(" ")
b = "am are are".split(" ")
c = "Hamza alive it".split(" ")

df2 = pd.DataFrame({"a": a, "b":b, "c":c})

print(df2)

print(" ".join(list(df2.loc[0])))
print(" ".join(list(df2.loc[1])))
print(" ".join(list(df2.loc[2])))

# Use a for loop;

print(list_a)

