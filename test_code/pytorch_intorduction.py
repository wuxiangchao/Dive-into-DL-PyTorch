from matplotlib import pyplot as plt

class Solution(object):
    def __init__(self):
        print("Test")
    
    def Test(self):
        try:
            print("This is Test")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    s = Solution()
    s.Test()