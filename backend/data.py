data = [1,2,3,4,5,6,7]

def info():
    if len(data):
        print(data[0])
        data.pop(0)
    else:
        data = [1,2,3,4,5,6,7]
        print(data)

def main():
    while True:
        info()
        
main()