class data:
    def __init__(self, value, index, count=0):
        self.value= value
        self.index= index
        self.count= count
        
def sortbyfreqind(arr):
    if arr is None or len(arr) < 2:
        return
    
    hm= {}
    
    #for each array element insert into the dictionary
    #its frequency and index of its first occurence in the array
    
    for i in range(len(arr)):
        hm.setdefault(arr[i], data(arr[i], i)).count += 1
        
    values= [*hm.values()]
    
    '''
       Sort the values based on a custom comparator
       
       1. If two elements have different frequencies then the one with high frequency should come first
       2. If two elements have same frequencies then the one which has less index should come first
    '''
    
    values.sort(key= lambda x: (-x.count, x.index))
    
    k=0
    for Data in values:
        for j in range(Data.count):
            arr[k]= Data.value
            k += 1
            
if __name__ == '__main__':
    arr= [1,2,3,4,5,6,7,8,9,3,1,1,1,2,2]
    print("Original: ", arr)
    sortbyfreqind(arr)
    print("Sorted: ", arr)