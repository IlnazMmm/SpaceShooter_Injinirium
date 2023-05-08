class Avalanche:
    def __init__(self):
        self.string = input()
        self.left_count = int(input())
        self.left_nums = []
        for i in range(self.left_count):
            self.left_nums.append(int(input()))
        self.right_count = int(input())
        self.right_nums = []
        for i in range(self.right_count):
            self.right_nums.append(int(input()))

    def solution(self):
        left = 0
        for i in range(self.left_count):
            if self.left_nums[i] % 2 == 0:
               if self.left_nums[i] >= len(self.string):
                   left+=1
        right = 0
        for i in range(self.right_count):
            if self.right_nums[i] % 2 == 0:
                if self.right_nums[i] >= len(self.string):
                    right += 1
        print(len(self.string))
        if left > right:
            print(f'На севере больше на {left - right}')
        elif right > left:
            print(f'На юге больше на {right - left}')
        elif left == right:
            print(f'Поровну')

task1 = Avalanche()
task1.solution()