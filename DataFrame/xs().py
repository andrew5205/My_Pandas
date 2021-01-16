

# xs() - Return cross-section from the Series/DataFrame.
# xs can not be used to set values.



import pandas as pd 

d = {
    'num_legs': [4, 4, 2, 2],
    'num_wings': [0, 0, 2, 2],
    'class': ['mammal', 'mammal', 'mammal', 'bird'],
    'animal': ['cat', 'dog', 'bat', 'penguin'],
    'locomotion': ['walks', 'walks', 'flies', 'walks']
}

df = pd.DataFrame(data=d)
df = df.set_index(['class', 'animal', 'locomotion'])

# print(df)
# #                           num_legs  num_wings
# # class  animal  locomotion                     
# # mammal cat     walks              4          0
# #        dog     walks              4          0
# #        bat     flies              2          2
# # bird   penguin walks              2          2



# Get value
print(df.xs('mammal'))
#                    num_legs  num_wings
# animal locomotion                     
# cat    walks              4          0
# dog    walks              4          0
# bat    flies              2          2



print(df.xs(('mammal', 'dog')))
#             num_legs  num_wings
# locomotion                     
# walks              4          0


print(df.xs('cat', level=1))
#                     num_legs  num_wings
# class  locomotion                     
# mammal walks              4          0



print(df.xs(('bird', 'walks'), level=[0, 'locomotion']))
#         num_legs  num_wings
# animal                      
# penguin         2          2



print(df.xs('num_wings', axis=1))
# class   animal   locomotion
# mammal  cat      walks         0
#         dog      walks         0
#         bat      flies         2
# bird    penguin  walks         2
# Name: num_wings, dtype: int64


