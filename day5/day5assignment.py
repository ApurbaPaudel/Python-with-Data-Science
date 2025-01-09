#1 Create a dictionary with the following key-value pairs:(name,age,city)
intro={
    'name':'Apurba',
    'age': 23,
    'city': 'Pokhara'
}
print(intro)

#2 Given the dictionary, access and print the values associated with the keys 'name' and 'job'.
person={
    'Name':'Bob',
    'age':30,
    'city':'los angeles',
    'job': 'Doctor'

}
print(person['Name'])
print(person['job'])

#3 Given the dictionary person add a new key value pair job, then update the value of the age to 29
person={
    'name':'John',
    'age':28,
    'city':'Chicago'}
b={'job':'teacher'}
person.update(b)
print(person)
c={'age':29}
person.update(c)
print(person)

#4 Create a nested dictionary to store the details of two people and access one dictionary keys and value
p= {
    'p1':{
        'name':'james',
        'age': 20
    },
    'p2':{
        'name':'Sky',
        'age':30
    }

    }
print(p['p1'])

#5 Given two dictionaries, find the common keys between the two
dict1={'a':1,
       'b':2,
       'c':3}
dict2={'b':4,
       'c':5,
       'd':6}
c=dict1.keys() & dict2.keys()
print(c)

#6 Given the dictionary person, remove the key value pair with the key city
person={'name':'Sarah',
        'age':35,
        'city':'Miami',
        'job':'Lawyer'}
person.pop('city')
print(person)



