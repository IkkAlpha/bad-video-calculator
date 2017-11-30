from maths import newton_root

current_length = 0
p = [] # Set of points which the video speeds up at.
z = 0 # Desired length of the video.
c = 0 # The constant to multiply by.

def parse_timestamp(string):
    splitted = list(map(lambda x: float(x), string.split(":")))
    return (splitted[0] * 60) + splitted[1]
    
current_length = parse_timestamp(input("What is the current length of the video? (Use a timestamp): "))
z = parse_timestamp(input("What is the desired length of the video? (Use a timestamp): "))

count = 1
while True:
    add = input("What is a point in the video that speeds up ({})? (timestamp or 'exit' to quit): ".format(count))
    
    if add == "exit":
        break
    
    else:
        p.append(parse_timestamp(add))
        count += 1

p.append(current_length)
        
polynomial = [[p[0] - z, 0]]

for k in range(1, len(p)):
    polynomial.append( [p[k] - p[k-1], k] )
    
polynomial = polynomial[::-1]

answer = newton_root(polynomial)
    
print("You need to multiply it by {}, or {}% to get a length of {} seconds.".format(round(answer*100)/100, round(answer*10000)/100, z))