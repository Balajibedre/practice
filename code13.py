new list
xs = [1,"x",3.1415]
ys = list(xs)

indexing

xs = [1,2,3]
xs[0] # 1
xs[1] # 2
xs[-1] # 3
xs[-2] # 2

length of list

xs = [1,2,1,2]
length = len(xs)
# length = 4

append

xs = [1,1]
ys = [3,3]
xs.append(2)
# xs = [1,1,2]
xs.append(ys)
# xs = [1,1,2,[3,3]]
