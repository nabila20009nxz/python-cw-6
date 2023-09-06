person={
    "name":"nabila" ,
    "age":"14",
    "hobbies":["running","sleeping","coding"]
} 
print(person.get ("name"))
print(person.get("age"))
person["age"]=15
person["country"]="yemen"
print(person)
print(len(person))
person["hobbies"]="eating"
def check_hobbies(person):
  if len( person["hobbies"])>=3:
    print("wow you are amazing") 
check_hobbies(person)