def function(x):
    return x * (x + 2) - 1

intervalBegin = float(input("Enter beginning of interval: "))
intervalEnd = float(input("Enter end of interval: "))
precision = float(input("Enter precision of method: "))

cHK = True

if(function(intervalBegin) * function(intervalEnd) > 0):
    print("Function has same signs at ends of interval")
    cHK = False

while(abs(intervalBegin - intervalEnd) > precision):
    middle = (intervalBegin + intervalEnd) / 2

    print("X: ", middle)

    if(function(intervalBegin) * function(middle) < 0):
        intervalEnd = middle
    else:
        intervalBegin = middle