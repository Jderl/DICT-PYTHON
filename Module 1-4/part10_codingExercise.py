#1
def information(name, age, favColor, favMovie, mobile, motto):
    print(" Name: ", name,'\n',
          "Age: ", age,"\n",
          "Favorite Color: ", favColor,"\n",
          "Favorite Movie: ", favMovie,'\n',
          "Mobile number: ", mobile, '\n',
          "Motto in Life: ", motto)
    
    
name = input ("Enter a name: ")
age  = int (input("Enter your age : "))
favColor = input ("Enter your favorite color : ")
favMovie = input("Enter your favorite movie : ")
mobile = int (input("Input mobile number : "))
motto = input("Enter your motto: ")

information(name, age, favColor, favMovie, mobile, motto)