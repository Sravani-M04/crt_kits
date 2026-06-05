#p1 add & update
lang={'java','python','c','c++','sql'}
print(lang)
lang.add("ruby")
print(lang)
ui={'html','angular','css'}
lang.update(ui)
print(lang)

#p2 deleting using discard or remove
set={'apple','banana','cherry'}
set.discard('banana')
print(set)

set={'apple','banana','cherry'}
set.discard('banana')
print(set)

#p3 inter, diff, union,issubset,issuperst
set1={'tom and jerry','oggy & cockroches','doremon','motu patlu','shinchan'}
set2={'oggy & cockroches','little krishna','heidi','shinchan'}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))

