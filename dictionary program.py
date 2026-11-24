a = {
    "name":"vinay",#name:key,"vinay":value
    "age":21,
    "institute":"kodnest"

}
#for accessing
print(a["name"])#if we want we can acess age , institute instead of name
#for updating value
a["age"]=20
#for getting length of dict we use
print(len(a))
#for checking key existed or not
print("name" in a)#it only checks keys only it not works for values
print(a.values())#for getting all values if we use keys() we get keys if we use items() we get both
#using in for loops
for i,j in a.items():#if we want only keys or values we can use keys , values instead of items but want to take only i only
    print(i,j)#here i refers to keys and j refers to values
print(a.get("city","bengaluru"))#if we want to search for a item that doesn't exist if we use normal method it gives error if we use this if that doesn't exist also we get default value
#city(normal value),bengaluru default value
#pop we use it for removing value
b=a.pop("age")#we use variable b to store poped value but it can only store value not key@output:21
#for updating value in dict
a.update({
    "age":20,
    "city":"bengaluru"
})#if age exist in normal dict if we use update it prints updated value

#for creating nested dict 
students = {
    "s1": {
        "name": "Vinay",
        "marks": 85
    },
    "s2": {
        "name": "Rahul",
        "marks": 90
    }
}

print(students["s2"]["marks"])#for creating nested dict 
# setdefault() → add only if key doesn't exist
# update()     → update existing key / add new key
student = {
    "name": "Vinay",
    "age": 22
}

student.setdefault("age", 30)

print(student)#@output:22 cause  value already exist 
#clear() used for clearing all data@
student.clear()
#dict comprehension
squares = {x: x * x for x in range(1, 5)}#{key: value for item in sequence}
even = {x: x * x for x in range(1, 6) if x % 2 == 0}#@even or odd program
#comprehension with condition
print(even)