def main():
    #create two variables and print them
    a, b = 0, "one"
    print(type(a), a, type(b), b)
    #create two more variables
    one, two = 4,7
    #if/elif control structure
    if one < two:
        print("one is less than two")
    elif one > two:
        print("one is greater than two")
    else:
        print("one is equal to two")

    #call function twice
    func(1,10)
    func(4,20)

    #call class twice
    pet1 = housePet()
    pet1.whatPetType()
    pet1.whatPetSound()

#define function that accepts two arguments
def func(start, stop):
    for i in range(start, stop):
        print(i, end=' ')
    print()

#define a simple class
class housePet:
    #variables
      petType = "Dog"
      petSound = "Bark"

    #function to print pet type
def whatPetType(self):
      print(self.petType)

    #function to print sound made by pet
def whatPetSound(self):
      print(self.petSound)
      if __name__ == "__main__": main()