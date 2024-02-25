
class BubbleSort(object):

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def sort(self):
        """bubble array elements into a list of ascending order"""
        swapped = False
        for i in range(self.length - 1):
            for j in range(0, self.length - i - 1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j + 1], self.array
            if not swapped:
                return
