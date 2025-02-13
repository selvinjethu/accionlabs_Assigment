class ArrayIntersection:
    def __init__(self, arr1, arr2):
        """Initialize with two arrays."""
        if not isinstance(arr1, list) or not isinstance(arr2, list):
            raise ValueError("Both inputs must be lists.")
        self.arr1 = arr1
        self.arr2 = arr2

    def find_common(self):
        """Finds and returns the sorted intersection of the two arrays."""
        try:
            return sorted(set(self.arr1) & set(self.arr2))
        except Exception as e:
            print(f"Error occurred: {e}")
            return []

if __name__ == "__main__":
    try:
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [3, 4, 5, 6, 7]
        intersect = ArrayIntersection(arr1, arr2)
        print("Common Elements:", intersect.find_common())
    except ValueError as e:
        print(f"Invalid Input: {e}")
