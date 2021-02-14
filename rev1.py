import numpy
import math

axis = 'x'
degrees = 0
vector_x = 0
vector_y = 0
vector_z = 0


print("Welcome to George's Inverse Transform Calculator!")
print("This program will calculate a transform and inverse transform given")
print("a rotation axis, degrees of rotation, and offset origin vector.")

# get rotation axis
print("1) Please enter the rotation axis: (x), (y), or (z) and press enter.")
axis = input()

# make sure rotation axis is valid (we don't like typos)
while (True): 
      if (axis.lower() == 'x' or axis.lower() == 'y' or axis.lower() == 'z'): 
            break       
      axis = input("Error: invalid input. Please enter (x), (y), or (z) and press enter.")

# get degrees of rotation
print("Please enter degrees of rotation and press enter.")
degrees = input()
degrees_rad = int(degrees) * math.pi / 180 # convert degrees to radians

# get offset vector x
print("Please enter the x component of the offset vector and press enter.")
vector_x = input()

# get offset vector y
print("Please enter the x component of the offset vector and press enter.")
vector_y = input()

# get offset vector z
print("Please enter the x component of the offset vector and press enter.")
vector_z = input()

# load array with offset vector and filler data
transform_matrix = numpy.array([ [0,0,0,vector_x],[0,0,0,vector_y],[0,0,0,vector_z],[0,0,0,1] ]) 

if(axis.lower()=='x'): # x-rotation matrix data
      transform_matrix[0][0] = 1
      transform_matrix[0][1] = 0
      transform_matrix[0][2] = 0
      
      transform_matrix[1][0] = 0
      transform_matrix[1][1] = numpy.cos(degrees_rad)
      transform_matrix[1][2] = -1*numpy.sin(degrees_rad)
      
      transform_matrix[2][0] = 0
      transform_matrix[2][1] = numpy.sin(degrees_rad)
      transform_matrix[2][2] = numpy.cos(degrees_rad)

if(axis.lower()=='y'): # x-rotation matrix data
      transform_matrix[0][0] = numpy.cos(degrees_rad)
      transform_matrix[0][1] = 0
      transform_matrix[0][2] = numpy.sin(degrees_rad)
      
      transform_matrix[1][0] = 0
      transform_matrix[1][1] = 1
      transform_matrix[1][2] = 0
      
      transform_matrix[2][0] = -1*numpy.sin(degrees_rad)
      transform_matrix[2][1] = 0
      transform_matrix[2][2] = numpy.cos(degrees_rad)    
      
if(axis.lower()=='z'): # x-rotation matrix data
      transform_matrix[0][0] = numpy.cos(degrees_rad)
      transform_matrix[0][1] = -1*numpy.sin(degrees_rad)
      transform_matrix[0][2] = 0
      
      transform_matrix[1][0] = numpy.sin(degrees_rad)
      transform_matrix[1][1] = numpy.cos(degrees_rad) 
      transform_matrix[1][2] = 0
      
      transform_matrix[2][0] = 0
      transform_matrix[2][1] = 0
      transform_matrix[2][2] = 1 



print('The transform is')
print(transform_matrix)
print('The inverse transform is')
print(transform_matrix.T)

      
      