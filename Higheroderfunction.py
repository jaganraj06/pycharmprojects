#higheroderfunction
#takes function as parameter or returnfunction
def Hotel():
    print("Food")

def Sweet():
    print("Ashoka")
    print("Gulabjamun")

def spicy():
    print("samosa")
    print("masalvada")

def eat(func):
    func()
    return Hotel
func = eat(spicy)
func1 = eat(Sweet)
func()
spicy()



