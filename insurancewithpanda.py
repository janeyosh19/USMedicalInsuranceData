import pandas as pd 

df = pd.read_csv(r"C:\Users\j_ney\Python\Python Project Medical Insurance Analysis\insurance.csv")

age_list = df[['age']]
unique_values = age_list.value_counts()
max_age = unique_values.idxmax()
print(type(max_age))
print(f'The most common age with insurance is {max_age[0]} with a number of {unique_values.max()} insured people')

region_sex_list = df[['region', 'sex']] ##how many female and male insured people per region
print(region_sex_list)
sex_region_values = region_sex_list.value_counts()
print(sex_region_values)


region_age_list = df[['region', 'age']] ##how many female and male insured people per region
age_region_values = region_age_list.value_counts()


dfnew = pd.DataFrame(age_region_values) #regions with ages and no. of people
dfnew.sort_values(by=['age'], inplace=True)
sorted_region_data = dfnew.loc[['southeast', 'southwest', 'northeast', 'northwest']]



region_children_list = df[['region', 'children']] ##how many children range(0,5) insured people per region
children_region_values = region_children_list.value_counts()

print(children_region_values)









