max_size = int(input())
queue_size = int(input())

lookup = {}
names = []

for i in range(queue_size):
    name = input()
    time = int(input())
    
    lookup[name] = time
    names.append(name)

cache = {}
def getOrder(array,name):
    if name in cache:
        return cache[name]
    
        
    

array = getOrder(array,names[0])
