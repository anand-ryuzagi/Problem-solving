def doIntersections(a,b):
  set1 = set()
  set2 = set()
  for i in a:
    set1.add(i)
  for j in b:
    set2.add(j)
            
  return len(set1&set2)
#   return len(set1.intersection(set2))
     
if __name__ == "__main__":
  arr1 = [1,2,3,4,5]
  arr2 = [1,5]
  print(doIntersections(arr1,arr2))
