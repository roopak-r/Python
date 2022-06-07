#spanis english dictionary
def create_dictionary():
    spanish=dict()
    spanish['hello']='hola'
    spanish['yes']='si'
    spanish['one']='uno'
    spanish['two']='dos'
    spanish['three']='tres'
    spanish['red']='rojo'
    spanish['black']='negro'
    spanish['green']='verde'
    spanish['blue']='azui'
    return spanish
print("Welcome to spanish english dictionary")
dictionary=create_dictionary()
W=input("Enter an english word:")
if W in dictionary:
    print("Spanish translation is:",dictionary[W])
else:
    print("Word not found")
