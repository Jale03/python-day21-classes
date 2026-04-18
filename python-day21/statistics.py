class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)

        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2]
            mid2 = sorted_data[n // 2 - 1]
            return (mid1 + mid2) / 2
