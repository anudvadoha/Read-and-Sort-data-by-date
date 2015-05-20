from operator import itemgetter

final_array_contents = []
#for line in open("test_1.log"):
for line in open("t_registers_pcie_015.log"):
    columns = line.split(' ')
    intermediate_split =[]
    for element in columns:
	    #print(element)
	    element = element.split('\t')
	    intermediate_split = intermediate_split + element;
	    #print(element)
    #print(' ')
    #print("THIS IS intermediate_split")
    #print(" ")
    #print(intermediate_split)
    final_array_contents.append(intermediate_split)
    
print("CONTENTS IN A LIST BEFORE SORT: \n")
print(final_array_contents)
print("\n")

def column(matrix, i):
    return [row[i] for row in matrix]

print("DAY:")
print(column(final_array_contents,0))
print("MONTH:")
print(column(final_array_contents,1))
print("DATE:")
print(column(final_array_contents,2))
print("TIME:")
print(column(final_array_contents,3))
print("YEAR:")
print(column(final_array_contents,4))
print("MGIT ID:")
print(column(final_array_contents,5))
print("STATUS:")
print(column(final_array_contents,6))
print("USER:")
print(column(final_array_contents,7))
print("SIM")
print(column(final_array_contents,8))
print("PROJECT:")
print(column(final_array_contents,9))
print("REG_ADDR")
print(column(final_array_contents,10))
print("SVLOG:")
print(column(final_array_contents,11))
print("LSFOUT:")
print(column(final_array_contents,12))


for element in final_array_contents:
    #print("Month =",element[1])
    if(element[1]=="Jan"):
        date = 0
	
    if(element[1]=="Feb"):
	    date = 31*24*60*60
	
    if(element[1]=="Mar"):
	    date = (31+30)*24*60*60 
	
    if(element[1]=="Apr"):
	    date = (31+30+31)*24*60*60
	
    if(element[1]=="May"):
	    date = (31+30+31+30)*24*60*60
	
    if(element[1]=="Jun"):
	    date = (31+30+31+30+31)*24*60*60
		
    if(element[1]=="Jul"):
	    date = (31+30+31+30+31+30)*24*60*60

    if(element[1]=="Aug"):
	    date = (31+30+31+30+31+30+31)*24*60*60

    if(element[1]=="Sep"):
	    date = (31+30+31+30+31+30+31+31)*24*60*60

    if(element[1]=="Oct"):
	    date = (31+30+31+30+31+30+31+31+30)*24*60*60

    if(element[1]=="Nov"):
	    date = (31+30+31+30+31+30+31+31+30+31)*24*60*60

    if(element[1]=="Dec"):
	    date = (31+30+31+30+31+30+31+31+30+31+30)*24*60*60		

    #print(element[2])
    #print(date)
    date = date + (int(element[2])-1)*24*60*60
    #print(element[4])
    date = date + ( int(element[4])*365 + (int(element[4])//4 ) * 24*60*60)
    time = element[3].split(':')
    date = date + int(time[0]) + int(time[1])+ int(time[2])
    #print(date)
    element.append(date)

new_sorted_list = sorted(final_array_contents,key =itemgetter(-1))	
print("New sorted List : \n")
print(new_sorted_list)

latest_time = 0;
for element in new_sorted_list:
    if(element[6]== "PASSED"):
        #print(element[-1])
        if(element[-1] > latest_time):
            latest_time = element[-1]
            #print("LATEST_TIME IS: ",latest_time)
			
for element in new_sorted_list:
    if(latest_time in element):
        print("Details for the lastest PASS run")
        print("Date: "+element[1]+" "+element[2]+" "+element[3]+" "+element[4]+" "+element[5])

