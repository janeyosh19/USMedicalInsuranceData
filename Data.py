import csv
from operator import sub
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from zmq import has

with open(r'C:\Users\j_ney\Python\Python Project Medical Insurance Analysis\insurance.csv', 'r') as insurance_data_csv:
    insurance_data = csv.reader(insurance_data_csv, delimiter = ' ')
    insurance_data_list = []
    for row in insurance_data:
        insurance_data_list.append(', '.join(row))
        
insurance_data_list.pop(0) #removing the headers element      

insurance_data_sublist = []
for data_list in insurance_data_list:
    insurance_data_sublist.append(data_list.split(',')) #rows of data in sublist

#print(insurance_data_sublist)

len_insured_people = len(insurance_data_sublist) #how many insured people in the data
#print(len_insured_people)

#Make a lists of age, sex, bmi, no_of children, smoke, region, charges and then also put in dictionary form:
#List of Age
insurance_age = [int(age_data[0]) for age_data in insurance_data_sublist]
#print(insurance_age)

#List of Sex
insurance_sex = [sex_data[1] for sex_data in insurance_data_sublist]
#print(insurance_sex)

#List of Bmi
insurance_bmi = [float(bmi_data[2]) for bmi_data in insurance_data_sublist]
#print(insurance_bmi)

#List of No_of_children
insurance_children = [int(children_data[3]) for children_data in insurance_data_sublist]
#print(insurance_children)

#List of Smoker
insurance_smoker = [smoker_data[4] for smoker_data in insurance_data_sublist]
#print(insurance_smoker)

#List of Region
insurance_region = [region_data[5] for region_data in insurance_data_sublist]
#print(insurance_region)

#List of Charges
insurance_charges = [charges_data[-1] for charges_data in insurance_data_sublist]
#print(insurance_charges)


#Age Questions
class Age:
    
    def __init__(self, age_list):
        self.age_list = age_list

    def find_average(self): #Method to find the average age with insurance
        average_age = int(sum(self.age_list)/ len(self.age_list))
        return average_age
    
    def count_per_age(self): #Method dictionary of ages = csv to show how many people in ages
        count_age = dict((age, self.age_list.count(age)) for age in self.age_list)
        return count_age

    def age_most_insurance(self): #Method to find the age with the most insurance
        max_count = max(self.count_per_age().values())
        for max_key, max_value in self.count_per_age().items():
            if max_count == max_value:
                return max_key, max_value

    def age_least_insurance(self): #Method to find the age with the least insurance
        min_count = min(self.count_per_age().values())
        for min_key, min_value in self.count_per_age().items():
            if min_count == min_value:
                return min_key, min_value
        
    def young_age(self): #Method to find youngest age of insured
        min_age = min(self.age_list)
        return min_age

    def old_age(self): #Method to find oldest age of insured
        max_age = max(self.age_list)
        return max_age

    
    def No_Insured_Young_People(self): #Method to find how many insured young people
        key_value = dict(sorted(self.count_per_age().items()))
        range_young_age = range(18, 25)
        young_age_dict = {key: key_value[key] for key in key_value.keys() & range_young_age}
        sum_insured_young_age = sum(young_age_dict.values())
        return sum_insured_young_age
        
    def No_Insured_Adult_People(self): #Method to find how many insured adult people
        key_value = dict(sorted(self.count_per_age().items())) 
        range_adult_age = range(25, 65)
        adult_age_dict = {key: key_value[key] for key in key_value.keys() & range_adult_age}
        sum_insured_adult_age = sum(adult_age_dict.values())
        return sum_insured_adult_age

age = Age(insurance_age)

print(f'The average age of people with insurance is {age.find_average()}')
#print(f'The total of people by ages with insurance {age.count_per_age()}') #csv data
max_key, max_value = age.age_most_insurance()
min_key, min_value = age.age_least_insurance()
print(f'The most common age with isurance is {max_key} with a number of {max_value} insured people')
print(f'The least common age with isurance is {min_key} with a number of {min_value} insured people')
print(f'The youngest insured age is {age.young_age()}')
print(f'The oldest insured age is {age.old_age()}')
print(f'The number of young insured people is {age.No_Insured_Young_People()}')
print(f'The number of adult insured people is {age.No_Insured_Adult_People()}')



#Sex Questions:
class Sex:

    def __init__(self, sex):
        self.sex = sex

    def count_female(self): #Method to find the number of insured female
        no_female = self.sex.count('female')
        return no_female

    def count_male(self): #Method to find the number of insured male
        no_male = self.sex.count('male')
        return no_male

#total charges of insured female and male

sex = Sex(insurance_sex)
#This show the counts(female and male) and graph(difference between female and male numbers of insured)
# female_count = sex.count_female()
# male_count = sex.count_male()

# data = [female_count, male_count]
# plt.bar(['female', 'male'], data)
# plt.show()



#bmi
class BMI:

    def __init__(self, bmi):
        self.bmi = bmi

    def count_bmi(self): #dictionary for count of repetitive bmi's
        bmi_match = dict((bmi, self.bmi.count(bmi)) for bmi in self.bmi)
        return bmi_match 
    def bmi_range(self): #dictionary for underweight, normal, overweight and obese bmi
        underweight = {}
        normal = {}
        overweight = {}
        obese = {}
        for key, value in sorted(self.count_bmi().items()):
            if key < 18.5:
                underweight.update({key:value})
            elif 18.5 == key <=24.9:
                normal.update({key:value}) 
            elif 25 <= key <= 29.9:
                overweight.update({key:value}) 
            elif key > 30:
                obese.update({key:value}) 
            
        return underweight, normal, overweight, obese

    def count_bmi_range(self):
        underweight_sum = sum(underweight.values())
        normal_sum = sum(normal.values())
        overweight_sum = sum(overweight.values())
        obese_sum = sum(obese.values())
        
        return underweight_sum, normal_sum, overweight_sum, obese_sum
        
           
           

bmi = BMI(insurance_bmi)
# print(bmi.count_bmi())
underweight, normal, overweight, obese = bmi.bmi_range()
underweight_sum, normal_sum, overweight_sum, obese_sum = bmi.count_bmi_range() #HUH???
# print(f'Total underweight insured people: {underweight_sum}')
# print(f'Total normal insured people: {normal_sum}')
# print(f'Total overweight insured people: {overweight_sum}')
# print(f'Total obese insured people: {obese_sum}')

#chidren
class Children:

    def __init__(self, children):
        self.children = children

    def highest_no_children(self):
        high_no_children = max(self.children)
        return high_no_children

    def count_children(self): #Method to count how many people with 0, 1, 2, 3, 4, 5 children
        count_children_dictionary = dict((child, self.children.count(child)) for child in self.children) #dictionary for count of repetitive number of children
        



child = Children(insurance_children)
print(child.highest_no_children())
print(child.count_children())

#smoker
class Smoker:

    def __init__(self, smoker):
        self.smoker = smoker

    def smoker_count(self): #Method for getting number of people who smoke and not smoke
        smoker_dictionary = dict((count, self.smoker.count(count)) for count in self.smoker)
        value_yes = 0
        value_no = 0
        for key, value in smoker_dictionary.items():
            if key == 'yes':
                value_yes = value
            elif key == 'no':
                value_no = value
        
        return value_yes, value_no


smoker = Smoker(insurance_smoker)
value_yes, value_no = smoker.smoker_count()
print(f'The number of insured people who smoke is {value_yes} and those who doesnt smoke is {value_no}')


#region
class Region:

    def __init__(self, region, insurance_list):
        self.region = region
        self.insurance_list = insurance_list

    def insured_per_region(self): #how many insured people per region
        total_per_region = dict((region, self.region.count(region)) for region in self.region)
        for key, value in total_per_region.items():
            if key == 'northwest':
                value_NW = value
            elif key == 'northeast':
                value_NE = value
            elif key == 'southwest':
                value_SW = value
            elif key == 'southeast':
                value_SE = value
        return value_NW, value_NE, value_SW, value_SE, total_per_region


    def per_region_list(self): #list of data per region
        northwest = []
        northeast = []
        southwest = []
        southeast = []
        for list in self.insurance_list:
            index = 0
            if list[5] == 'northwest':
                self.insurance_list[index] = list
                northwest.append(list)
            elif list[5] == 'northeast':
                self.insurance_list[index] = list
                northeast.append(list)
            elif list[5] == 'southwest':
                self.insurance_list[index] = list
                southwest.append(list)
            elif list[5] == 'southeast':
                self.insurance_list[index] = list
                southeast.append(list)    
        return northwest, northeast, southwest, southeast
    
    def total_female_per_region(self, northwest, northeast, southwest, southeast): #how many female insured people per region
        female_northwest = []
        female_northeast = []
        female_southwest = []
        female_southeast = []
        for list in northwest:
            if list[1] == 'female':
                female_northwest.append(list)
                northwest_fem_total = len(female_northwest)
        for list in northeast:
            if list[1] == 'female':
                female_northeast.append(list)
                northeast_fem_total = len(female_northeast)
        for list in southwest:
            if list[1] == 'female':
                female_southwest.append(list)
                southwest_fem_total = len(female_southwest)
        for list in southeast:
            if list[1] == 'female':
                female_southeast.append(list)
                southeast_fem_total = len(female_southeast) 
        return northwest_fem_total, northeast_fem_total, southwest_fem_total, southeast_fem_total
      
    def total_male_per_region(self, northwest, northeast, southwest, southeast):  #how many male insured people per region
        male_northwest = []
        male_northeast = []
        male_southwest = []
        male_southeast = []
        for list in northwest:
            if list[1] == 'male':
                male_northwest.append(list)
                northwest_mal_total = len(male_northwest)
        for list in northeast:
            if list[1] == 'male':
                male_northeast.append(list)
                northeast_mal_total = len(male_northeast)
        for list in southwest:
            if list[1] == 'male':
                male_southwest.append(list)
                southwest_mal_total = len(male_southwest)
        for list in southeast:
            if list[1] == 'male':
                male_southeast.append(list) 
                southeast_mal_total = len(male_southeast) 
        return northwest_mal_total, northeast_mal_total, southwest_mal_total, southeast_mal_total
      
    def children_northwest(self): #total number of children in southwest range(0, 5)
        children_nul_northwest = []
        children_one_northwest = []
        children_two_northwest = []
        children_three_northwest = []
        children_four_northwest = []
        children_five_northwest = []
        for list in northwest:
            if int(list[3]) == 0:
                children_nul_northwest.append(list)
                northwest_nul_total = len(children_nul_northwest)
            elif int(list[3]) == 1:
                children_one_northwest.append(list)
                northwest_one_total = len(children_one_northwest)
            elif int(list[3]) == 2:
                children_two_northwest.append(list)
                northwest_two_total = len(children_two_northwest)
            elif int(list[3]) == 3:
                children_three_northwest.append(list)
                northwest_three_total = len(children_three_northwest)
            elif int(list[3]) == 4:
                children_four_northwest.append(list)
                northwest_four_total = len(children_four_northwest)
            elif int(list[3]) == 5:
                children_five_northwest.append(list)
                northwest_five_total = len(children_five_northwest)
        
        return northwest_nul_total, northwest_one_total, northwest_two_total,northwest_three_total, northwest_four_total, northwest_five_total
        
    def children_northeast(self): #total number of children in northeast range(0, 5)
        children_nul_northeast = []
        children_one_northeast = []
        children_two_northeast= []
        children_three_northeast = []
        children_four_northeast= []
        children_five_northeast= []
        for list in northeast:
            if int(list[3]) == 0:
                children_nul_northeast.append(list)
                northeast_nul_total = len(children_nul_northeast)
            elif int(list[3]) == 1:
                children_one_northeast.append(list)
                northeast_one_total = len(children_one_northeast)
            elif int(list[3]) == 2:
                children_two_northeast.append(list)
                northeast_two_total = len(children_two_northeast)
            elif int(list[3]) == 3:
                children_three_northeast.append(list)
                northeast_three_total = len(children_three_northeast)
            elif int(list[3]) == 4:
                children_four_northeast.append(list)
                northeastt_four_total = len(children_four_northeast)
            elif int(list[3]) == 5:
                children_five_northeast.append(list)
                northeast_five_total = len(children_five_northeast)
        
        return  northeast_nul_total,  northeast_one_total, northeast_two_total, northeast_three_total, northeastt_four_total, northeast_five_total

    def children_southwest(self):#total number of children in southwest range(0, 5)
        children_nul_southwest = []
        children_one_southwest = []
        children_two_southwest = []
        children_three_southwest = []
        children_four_southwest = []
        children_five_southwest= []
        for list in southwest:
            if int(list[3]) == 0:
                children_nul_southwest.append(list)
                southwest_nul_total = len(children_nul_southwest)
            elif int(list[3]) == 1:
                children_one_southwest.append(list)
                southwest_one_total = len(children_one_southwest)
            elif int(list[3]) == 2:
                children_two_southwest.append(list)
                southwest_two_total = len(children_two_southwest)
            elif int(list[3]) == 3:
                children_three_southwest.append(list)
                southwest_three_total = len(children_three_southwest)
            elif int(list[3]) == 4:
                children_four_southwest.append(list)
                southwest_four_total = len(children_four_southwest)
            elif int(list[3]) == 5:
                children_five_southwest.append(list)
                southwest_five_total = len(children_five_southwest)
        
        return  southwest_nul_total,  southwest_one_total, southwest_two_total, southwest_three_total, southwest_four_total, southwest_five_total

    def children_southeast(self): #total number of children in southeast range(0, 5)
        children_nul_southeast = []
        children_one_southeast = []
        children_two_southeast= []
        children_three_southeast = []
        children_four_southeast= []
        children_five_southeast= []
        for list in southeast:
            if int(list[3]) == 0:
                children_nul_southeast.append(list)
                southeast_nul_total = len(children_nul_southeast)
            elif int(list[3]) == 1:
                children_one_southeast.append(list)
                southeast_one_total = len(children_one_southeast)
            elif int(list[3]) == 2:
                children_two_southeast.append(list)
                southeast_two_total = len(children_two_southeast)
            elif int(list[3]) == 3:
                children_three_southeast.append(list)
                southeast_three_total = len(children_three_southeast)
            elif int(list[3]) == 4:
                children_four_southeast.append(list)
                southeast_four_total = len(children_four_southeast)
            elif int(list[3]) == 5:
                children_five_southeast.append(list)
                southeast_five_total = len(children_five_southeast)
        
        return   southeast_nul_total,  southeast_one_total,  southeast_two_total,  southeast_three_total,  southeast_four_total,  southeast_five_total


    def smoker_per_region(self): #total number of smoker per region
        northwest_smoker = []
        northeast_smoker = []
        southwest_smoker = []
        southeast_smoker = []
        for list in northwest:
            if list[4] == 'yes':
                northwest_smoker.append(list)
                northwest_smo_total = len(northwest_smoker)
        for list in northeast:
            if list[4] == 'yes':
                northeast_smoker.append(list)
                northeast_smo_total = len(northeast_smoker)
        for list in southwest:
            if list[4] == 'yes':
                southwest_smoker.append(list)
                southwest_smo_total = len(southwest_smoker)
        for list in southeast:
            if list[4] == 'yes':
               southeast_smoker.append(list)
               southeast_smo_total = len(southeast_smoker)

        return northwest_smo_total, northeast_smo_total, southwest_smo_total, southeast_smo_total


    def notsmoker_per_region(self): #total number of smoker per region
        northwest_notsmoker = []
        northeast_notsmoker = []
        southwest_notsmoker = []
        southeast_notsmoker = []
        for list in northwest:
            if list[4] == 'no':
                northwest_notsmoker.append(list)
                northwest_notsmo_total = len(northwest_notsmoker)
        for list in northeast:
            if list[4] == 'no':
                northeast_notsmoker.append(list)
                northeast_notsmo_total = len(northeast_notsmoker)
        for list in southwest:
            if list[4] == 'no':
                southwest_notsmoker.append(list)
                southwest_notsmo_total = len(southwest_notsmoker)
        for list in southeast:
            if list[4] == 'no':
               southeast_notsmoker.append(list)
               southeast_notsmo_total = len(southeast_notsmoker)

        return northwest_notsmo_total, northeast_notsmo_total, southwest_notsmo_total, southeast_notsmo_total

    def northwest_bmi(self): #total number of bmi(range) northwest
        northwest_under = []
        northwest_norm = []
        northwest_over = []
        northwest_obese = []

        for list in northwest:
            if float(list[2]) < 18.5:
                northwest_under.append(list)
                northwest_under_total = len(northwest_under)
            elif 18.5 == float(list[2]) <= 24.9:
                northwest_norm.append(list)
                northwest_norm_total = len (northwest_norm)


    def charges_per_region(self): #total charges per region
        for list in northwest:
            pass
        


region = Region(insurance_region, insurance_data_sublist)

value_NW, value_NE, value_SW, value_SE, total_per_region = region.insured_per_region() #total insured people per region
print(f'Dictionary for total per region: {total_per_region}')
print(f'The total number of insured people in northwest is {value_NW}')
print(f'The total number of insured people in northeast is {value_NE}')
print(f'The total number of insured people in southwest is {value_SW}')
print(f'The total number of insured people in southeast is {value_SE}')

northwest, northeast, southwest, southeast = region.per_region_list() #list of data per region

northwest_fem_total, northeast_fem_total, southwest_fem_total, southeast_fem_total = region.total_female_per_region(northwest, northeast, southwest, southeast) #total female per region
northwest_mal_total, northeast_mal_total, southwest_mal_total, southeast_mal_total = region.total_male_per_region(northwest, northeast, southwest, southeast) #total male per region

print(f'The total number of female in northwest is {northwest_fem_total} and male {northwest_mal_total}')
print(f'The total number of female in northeast is {northeast_fem_total} and male {northeast_mal_total}')
print(f'The total number of female in southwest is {southwest_fem_total} and male {southwest_mal_total}')
print(f'The total number of female in southeast is {southeast_fem_total} and male {southeast_mal_total}')

northwest_nul_total, northwest_one_total, northwest_two_total,northwest_three_total, northwest_four_total, northwest_five_total = region.children_northwest() #northwest total number children range(0, 5)
northeast_nul_total,  northeast_one_total, northeast_two_total, northeast_three_total, northeast_four_total, northeast_five_total = region.children_northeast()#northeast total number children range(0, 5)
southwest_nul_total,  southwest_one_total, southwest_two_total, southwest_three_total, southwest_four_total, southwest_five_total = region.children_southwest() # southwest total number children range(0, 5)
southeast_nul_total,  southeast_one_total,  southeast_two_total,  southeast_three_total,  southeast_four_total,  southeast_five_total = region.children_southeast() #southeasttotal number children range(0, 5)

print(f'The total number of 0 children in northwest: {northwest_nul_total}, northeast: {northeast_nul_total}, southwest: {southwest_nul_total}, southeast: {southeast_nul_total}')
print(f'The total number of 1 children in northwest: {northwest_one_total}, northeast: {northeast_one_total}, southwest: {southwest_one_total}, southeast: {southeast_one_total}')
print(f'The total number of 2 children in northwest: {northwest_two_total}, northeast: {northeast_two_total}, southwest: {southwest_two_total}, southeast: {southeast_two_total}')
print(f'The total number of 3 children in northwest: {northwest_three_total}, northeast: {northeast_three_total}, southwest: {southwest_three_total}, southeast: {southeast_three_total}')
print(f'The total number of 4 children in northwest: {northwest_four_total}, northeast: {northeast_four_total}, southwest: {southwest_four_total}, southeast: {southeast_four_total}')
print(f'The total number of 5 children in northwest: {northwest_five_total}, northeast: {northeast_five_total}, southwest: {southwest_five_total}, southeast: {southeast_five_total}')


northwest_smo_total, northeast_smo_total, southwest_smo_total, southeast_smo_total = region.smoker_per_region() #total smoker per region
northwest_notsmo_total, northeast_notsmo_total, southwest_notsmo_total, southeast_notsmo_total = region.notsmoker_per_region() #total not smoker per region
print(f'The total number of smoker in northwest is {northwest_smo_total} and not smoker {northwest_notsmo_total}')
print(f'The total number of smoker in northeast is {northeast_smo_total} and not smoker {northeast_notsmo_total}')
print(f'The total number of smoker in southwest is {southwest_smo_total} and not smoker {southwest_notsmo_total}')
print(f'The total number of smoker in southeast is {southeast_smo_total} and not smoker {southeast_notsmo_total}')











