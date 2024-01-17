class SentinelLinearSearch(object):
    """Sentinel Linear Search"""

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)

    def find(self, target_value):
        """search for target_value using sentinel linear search"""
        n = self.size
        last_element = self.array[n - 1]
        self.array[n - 1] = target_value
        counter = 0
        while self.array[counter] != target_value:
            counter += 1
        self.array[n - 1] = last_element
        if counter <= n - 1 or counter == target_value:
            return True
        else:
            return False
