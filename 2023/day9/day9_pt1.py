
input = 'data/puzzle.txt'
# input = 'data/sample.txt'



def main():
    result_sum = 0
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            nums = list(map(int, line.rstrip().split()))
            for i in range(len(nums)):
                all_zero = True
                for j in range(0, len(nums)-i-1):
                    nums[j] = nums[j+1] - nums[j]
                    if nums[j] != 0:
                        all_zero = False
                if all_zero:
                    result_sum += sum(nums[j:])
                    break
    print(result_sum)
    
    
if __name__ == "__main__":
  main()
