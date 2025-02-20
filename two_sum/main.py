class Solution:
    def __init__(self, array, target):
        self.array = array
        self.target = target
    
    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, array):
        if not array:
            raise ValueError("Missing 'array' values")
        
        if not isinstance(array, list):
            array = array.strip().split(",")
        
        if len(array) < 2:
            raise ValueError("The array must contain at least two values.")    
        
        int_list = []
        try:
            int_list = [int(value) for value in array]
        except ValueError:
            raise ValueError(f"Invalid input: '{value}' is not an integer.")
        self._array = int_list
    
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
        if not target:
            raise ValueError("Missing 'target' values")
        try:
            int(target)  
        except ValueError:
            raise ValueError(f"Invalid input: '{value}' is not an integer.")
        self._target = int(target)
    
    def get_solution(self):
        nums = self.array
        for i in range(len(nums)):
            for i2 in range(i + 1, len(nums)):
                sum = nums[i] + nums[i2]
                if sum == self.target:
                    return [i, i2]
        return None

def main():
    list = [1, 2, 4, 9, 4]
    print(Solution(list, 8).get_solution())

if __name__ == "__main__":
    main()