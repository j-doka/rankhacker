class Sort: 
    def __init__(self, array):
        self.array = array
    

    def insertionSort(array):
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
            
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            
            array[j + 1] = key
        return array
    
