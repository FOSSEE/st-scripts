from find_gcd import gcd

def lcm(a, b): 
    return (a * b) / gcd(a, b) 

if __name__ == '__main__': 
    for line in open('lcmtestcases.txt'): 
        numbers = line.split() 
        x, y = int(numbers[0]), int(numbers[1]) 
        result = int(numbers[2]) 
        if lcm(x, y) != result:  
            print "Failed lcm test for", x, y 
        else: 
            print "Test passed", result 