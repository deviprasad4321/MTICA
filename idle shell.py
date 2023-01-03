Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: D:/pythonpractice11/day12/series06.py ================
5

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

================ RESTART: D:/pythonpractice11/day12/series06.py ================
-8

================ RESTART: D:/pythonpractice11/day12/series06.py ================
-8
INVALID

=================== RESTART: D:/pythonpractice11/day12/set.py ==================
{'orange', 'Yellow', 'Blue', 'Black', 'Green', 'Red'}

=================== RESTART: D:/pythonpractice11/day12/set.py ==================
{'Blue', 'Red', 'Green', 'Black', 'orange', 'Yellow'}
{4}

=================== RESTART: D:/pythonpractice11/day12/set.py ==================
{'Red', 'Black', 'Green', 'orange', 'Blue', 'Yellow'}
{4}
{1, 2, 3, 4, 5, 70, 6, 7, 8, 10, 9, 20, 30, 50, 60}

=================== RESTART: D:/pythonpractice11/day12/set.py ==================
{'Yellow', 'Red', 'Black', 'Green', 'orange', 'Blue'}
{4}
{1, 2, 3, 4, 5, 70, 6, 7, 8, 10, 9, 20, 30, 50, 60}
{1, 2, 3, 5, 6, 7, 8, 9, 70, 10, 50, 20, 60, 30}

=================== RESTART: D:/pythonpractice11/day12/set.py ==================
{'Red', 'orange', 'Blue', 'Yellow', 'Green', 'Black'}
{4}
{1, 2, 3, 4, 5, 70, 6, 7, 8, 10, 9, 20, 30, 50, 60}
{1, 2, 3, 5, 6, 7, 8, 9, 70, 10, 50, 20, 60, 30}
{70, 10, 50, 20, 60, 30}



=================== RESTART: D:/pythonpractice11/day12/set.py ==================
{'Black', 'Red', 'Blue', 'orange', 'Yellow', 'Green'}
{4}
{1, 2, 3, 4, 5, 70, 6, 7, 8, 10, 9, 20, 30, 50, 60}
{1, 2, 3, 5, 6, 7, 8, 9, 70, 10, 50, 20, 60, 30}
{70, 10, 50, 20, 60, 30}
{4}

=========================== RESTART: D:/pythonpractice11/day12/set.py ===========================
{'Blue', 'orange', 'Yellow', 'Green', 'Red', 'Black'}
{4}
{1, 2, 3, 4, 5, 70, 6, 7, 8, 10, 9, 20, 30, 50, 60}
{1, 2, 3, 5, 6, 7, 8, 9, 70, 10, 50, 20, 60, 30}
{70, 10, 50, 20, 60, 30}
{4}

=========================== RESTART: D:/pythonpractice11/day12/set.py ===========================
{'orange', 'Black', 'Red', 'Blue', 'Yellow', 'Green'}
{4}
{1, 2, 3, 4, 5, 70, 6, 7, 8, 10, 9, 20, 30, 50, 60}
{1, 2, 3, 5, 6, 7, 8, 9, 70, 10, 50, 20, 60, 30}
{70, 10, 50, 20, 60, 30}
{4}
{50, 40}
a={1,2}
a
{1, 2}
#symmetric difference
#pynative.com
set1={40,10,50,20,30}
set2={30,40,50,60,70}
set1.(symmetric_difference(set2))
SyntaxError: invalid syntax
print(set1.symmetric_difference(set2))
{20, 70, 10, 60}
if set1.isdisjoint(set2):
    print("no common items")
else:
    print("two sets have items in common")
    print(set1.intersection(set2))

    
two sets have items in common
{40, 50, 30}
set1={40,50,20,30}
set2={30,40,50,60,70}
if set1.isdisjoint(set2):
    print("no common items")
else:
    print("two sets have items in common")
    print(set1.intersection(set2))

    
two sets have items in common
{40, 50, 30}
set1={40,10,50,20,30}
set2={30,40,50,60,70}
set1.symmetric_difference_update(set2)
set1
{20, 70, 10, 60}
set1={40,10,50,20,30}
set2={30,40,50,60,70}

set1.intersection_update(set2)
set1
{40, 50, 30}
set1.sort()

help('list')
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

help(set)
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

