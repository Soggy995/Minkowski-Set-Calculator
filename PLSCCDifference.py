import numpy as np

def parallelogram(z):
    l1 = z[0]
    l2 = z[1]
    lst = []
    lst.append(np.array(l1[0])-np.array(l2[0]))
    lst.append(np.array(l1[0])-np.array(l2[1]))
    lst.append(np.array(l1[1])-np.array(l2[1]))
    lst.append(np.array(l1[1])-np.array(l2[0]))
    return lst



# def inputter (x,y,z,a,b,c):
# segments = [] 
#     co1 = [x,y,z]
#     co2 = [a,b,c]
#     bear = [co1, co2]
#     segments.append(bear)
#     return bear
# print(inputter(3,7,9,6,2,5))
segments = [[[13,0,0],[7,-4,0]], [[7,-4,0], [2,-2,0]], [[2,-2,0], [4,-6,0]], [[4,-6,0], [0,-12,0]], [[0,-12,0], [-4,-6,0]], [[-4,-6,0], [-2,-2,0]], [[-2,-2,0], [-7,-4,0]], [[-7,-4,0], [13,0,0]], [[13,0,0], [-7,4,0]], [[-7,4,0], [-2,2,0]], [[-2,-2,0], [-4,6,0]], [[-4,6,0], [0,12,0]], [[0,12,0], [4,6,0]], [[4,6,0], [2,2,0]], [[2,2,0], [7,4,0]], [[7,4,0], [13,0,0]]]          
pairs = []
for x in segments:
    for y in segments:
        if x!=y:
            pairs.append([x,y])
parallelograms =[]
for z in pairs:
    p = parallelogram(z)
    parallelograms.append(p)
#    print(p)
    
for gram in parallelograms:
    easyprint = [tuple(g) for g in gram]
    s = str(easyprint)
    print("Polygon(" + s[1:len(s)-1] + ")")
# for par in parallelograms:
#     print(par)
# print(parallelogram([[[3,7,9],[6,2,5]],[[1,4,8],[10,3,7]]]))