import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.read().splitlines()
        num = int(lines[0])
        res= [0] * num
        for i in range(num):
            nums = lines[i+1].split()
            res[i] = int(nums[0]) + int(nums[1])
    
    f = open('./dataset/Ex1_output.txt', 'w')
    for line in res:
        f.write(str(line) + '\n')
    f.close()


