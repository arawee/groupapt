from matplotlib import pyplot as plt # import libraries
import pandas as pd # import libraries
import netCDF4 # import libraries

fp='./L3_data/S5P_NRTI_L3__O3_____20220517T125128_20220517T125628_23794_02_020300_20220517T133136.nc' # your file name with the eventual path
nc = netCDF4.Dataset(fp) # reading the nc file and creating Dataset

data = [[""]*(len(nc["latitude"])+1) for i in range(len(nc["longitude"])+1)]

print(len(nc["longitude"]))
for i in range(len(nc["longitude"])):
    data[i+1][0] = str(nc["longitude"][i])[0:5]

for i in range(len(nc["latitude"])):
    data[0][i+1] = str(nc["latitude"][i])[0:5]

#print(nc["O3_column_number_density"][1][i][j])

for i in range(len(data[0])-1):
    for j in range(len(data)-1): 
        data[j+1][i+1] = str(nc["O3_column_number_density"][0][i][j])[0:5]
        #data[i+1][j+1] = nc["O3_column_number_density"][0][0]
    
for i in range(len(data[0])):
    for j in range(len(data)): 
        print(data[j][i], end="\t")
    print("\n")


#for latin in nc["latitude"]:
    #data.append()
    #print(latin)

#print(data)

""" print(nc["latitude"][0])
print(nc["longitude"][0])
print(nc["latitude"][-1])
print(nc["longitude"][-1])
for i in range(len(nc["O3_column_number_density"][0])):
    print(nc["O3_column_number_density"][0])
    print("Latitude:", nc["latitude"][-1])
    print("Longitude:", nc["longitude"][-1]) """

""" in this dataset each component will be 
in the form nt,nz,ny,nx i.e. all the variables will be flipped. """
#plt.imshow(nc['O3_column_number_density'][1,:,0,:]) 

""" imshow is a 2D plot function
according to what I have said before this will plot the second
iteration of the vertical slize with y = 0, one of the vertical
boundaries of your model. """
#plt.show() # this shows the plot