
def lloyds(k, n, points):
    centers = [points[i] for i in range(0, k)]
    converged = 10000

    while (converged > 0):
        new_centers = converge(k, n, points, centers)

        d = []
        for i in range(0, k):
            s = 0
            for j in range(0, n):
                temp = ((new_centers[i][j] - centers[i][j]) ** 2)
                s += temp
            d.append(s)
        converged = sum(d)

        centers = new_centers
    
    return centers

def converge(k, n, points, centers):
    indices = []
    new_centers = []

    for p in points:
        best = 10000
        index = -1

        for i in range(0, k):
            s = 0
            for j in range(0, n):
                temp = ((p[j] - centers[i][j]) ** 2)
                s += temp

            if (s < best):
                best = s
                index = i
        
        indices.append(index)
    
    for i in range(0, k):
        p = [0] * n
        count = 0

        for j in range(0, len(points)):
            if (i == indices[j]):
                count += 1

                for k in range(0, n):
                    p[k] += points[j][k]
        
        temp = []
        for c in p:
            s = (c / max(1, count))
            temp.append(s)

        new_centers.append(temp)

    return new_centers



reader = open("input.txt", "r")
writer = open("output.txt", "w")

temp = reader.readline().strip().split()
k = int(temp[0])
n = int(temp[1])

points = []
for l in reader:
    points.append([float(c) for c in l.strip().split()])

centers = lloyds(k, n, points)

count = len(centers)
for p in centers:
    writer.write(' '.join(str('{:.3f}'.format(c)) for c in p))

    count -= 1
    if (count != 0):
        writer.write('\n')

reader.close()
writer.close()
