
import random
#the following is generative model :
image_staircase=[]
image_no_staircase=[]


# for i in range(10):
#     image_staircase.append(round(random.random(),2))
for i in range(10):
    image_staircase.append(abs(round(random.uniform(0.5,1),2)))

# for i in range(10):
#     image_no_staircase.append(round(random.random(),2))


for i in range(10):
    image_no_staircase.append(abs(round(random.uniform(0,0.5),2)))

print(image_staircase)
print(image_no_staircase)
initial_prior=0.5
staircase=0
for i in range(10):
    if i==0:
        staircase=initial_prior 
    staircase=(image_staircase[i]*staircase)/(image_staircase[i]*staircase+image_no_staircase[i]*(1-staircase))
    print(staircase)