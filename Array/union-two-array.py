#union of two array

def doUnion(self,a,b):
  set1 = set()
  for i in a:
    set1.add(i)
  for j in b:
    set1.add(j)
            
  return len(set1)
     
if __name__ == "__main__":
  arr1 = [1,2,3,4]
  arr2 = [1,5]
  doUnion(arr1,arr2)
