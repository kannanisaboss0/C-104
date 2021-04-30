#---------------------------------------------------------------StatisticalCalculatour.py---------------------------------------------------------------#
'''
Importing modules:
-Counter from collections
-plotly.express as pe
-pandas as pd
-csv
-statistics(for test purposes)
'''
from collections import Counter
import plotly.express as pe
import pandas as pd
import csv
import statistics

#Introducotry code and user inputs
print("Welcome to StatisticalCalculatour.py.")
print("This program empowers you to find the mode,median and mean of a given set of data along with visual representation.")
print("It must also be considered that the weight valuesare rounded off to the fifth decimal for simplicity and ease of understanding.")


#Displaying all available units
list_predefined_values=["Available Units:","Pounds","Kilograms","Stones"]
for unit in list_predefined_values:
    print(unit)
unit_input=input("Please enter the unit of the values to be displayed from any one of the above:")


#Opening the file and reading the data
with open("File.csv") as f:
    data_read=csv.reader(f)
    data_list=list(data_read)  
data_list.pop(0)    
weight_list=[]  


#Analyisng wether the input generated exists within the stipulated units
if(unit_input=="Stones" or unit_input=="Kilograms" or unit_input=="Pounds"):
    for item in range(len(data_list)):
        weight=data_list[item][2]
        weight=float(weight)
        #Checking the specefic unit prescribed
        #Case-1
        if(unit_input=="Stones"):
            weight=weight/14
        #Case-2
        elif(unit_input=="Kilograms"):
            weight=weight/2.205
        #Case-3    
        elif(unit_input=="Pounds"):
            weight=weight*1
        weight_list.append(weight) 
    weight_list_length=len(weight_list)


#Findng the mean value
    print("Processing mean...")
    sum_mean=0
    for value in weight_list:
        sum_mean=value+sum_mean
    mean=sum_mean/weight_list_length
    #Rounding off the printed values to the fifth decimal   
    print("Mean Value: "+str(round(mean,2))+" "+str(unit_input))


#Finding the median value
    print("Processing median...")
    weight_list.sort()
    weight_list_sorted_length=len(weight_list)
    if(weight_list_sorted_length%2==0):
        print("The number of entries in the list is even: "+str(weight_list_sorted_length))
        median_even_1=float(weight_list[weight_list_sorted_length//2])
        median_even_2=float(weight_list[(weight_list_sorted_length//2)-1])
        median_even_final=(median_even_1+median_even_2)/2
        #Rounding off the printed values to the fifth decimal
        print("Median Value: "+str(round(median_even_final,5))+" "+str(unit_input))
    elif(weight_list_sorted_length%2!=0):
        print("The number of entries in the list is odd "+str(weight_list_sorted_length))
        median_odd=float(weight_list[weight_list_sorted_length//2])
        #Rounding off the printed values to the fifth decimal
        print("Median Value: "+str(round(median_odd,5))+" "+str(unit_input))


#Findng the mode value
    print("Processing mode...")
    print("Calculating mode generally takes a longer time.")
    mode_1=[]
    counter_list=Counter(weight_list)
    counter_list_items=counter_list.items()
    counter_list_values=counter_list.values()
    counter_list_dictionary=dict(counter_list_items)
    for a,v in counter_list_dictionary.items():
        if(a): 
            if(v==max(counter_list.values())):
                mode_1.append(v)
                mode_1.append(a)
    #Rounding off the printed values to the fifth decimal            
    print("Mode Value:-")
    print("Weight Value: "+str(round(mode_1[1],5))+" "+str(unit_input))
    print("Frequency of occurence: "+str(round(mode_1[0],5))+" times")
    print("Rendering graph...")
    #Generating a scatter-plot graph to represent the data
    #The graph is produced on a highly unstable web-browser, which oftentimes crashes.Ergo, google colab is a recommended editor
    read_dataframe=pd.read_csv("File.csv")
    graph_new=pe.scatter(read_dataframe,y="Index",x="Weight",color="Weight",size="Weight")
    graph_new.show()    
    print("Thank You for using StatisticalCalculatour.py.")    
else:
    print("Request Terminated.")
    print("Invalid Unit")
    print("Thank You for using StatisticalCalculatour.py.")
#---------------------------------------------------------------StatisticalCalculatour.py---------------------------------------------------------------#






    

    