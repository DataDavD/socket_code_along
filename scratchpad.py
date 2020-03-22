request_search = {
    "morpheus": "Follow the white rabbit. \U0001f430",
    "ring": "In the caves beneath the Misty Mountains. \U0001f48d",
    "\U0001f436": "\U0001f43e Playing ball! \U0001f3d0",
}
query = 'morpheu2222s'
answer = request_search.get(query) or f'No match for "{query}".'

# playing around with namedtuples

from collections import namedtuple


Person = namedtuple('Person', ['name', 'age'])

print('type', 'of', 'person')
print(type(Person))
print()

print('__class__', 'of', 'person')
print(Person.__class__)
print()
print('__class__.__name__', 'of', 'person')
print(Person.__class__.__name__)
print()

dd = Person('david', 42)

print('__clas__', 'of', 'dd')
print(dd.__class__)
print()

print('__clas__.__name__', 'of', 'dd')
print(dd.__class__.__name__)
print()