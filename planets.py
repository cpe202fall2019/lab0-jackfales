# Name: Jack Fales
# Lab: 0

def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   marsWeight = weight * 0.38
   jupiterWeight = weight * 2.34
   print("\nOn Mars you would weigh {1} pounds.\nOn Jupiter you would weigh {2} pounds.".format(weight, marsWeight, jupiterWeight)) 
   
   
   
if __name__ == '__main__':
   weight_on_planets()
