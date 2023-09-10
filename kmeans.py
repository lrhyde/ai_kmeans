k = 6
import csv, random, math
file = open('sixclass.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    r = row
    tup = (math.log(float(r[0]), 20), math.log(float(r[1])), math.log(float(r[2])), float(r[3]), r[4])
    rows.append(tup)
population = rows
print(rows)
means = random.sample(population, k)
clusters = [[] for i in range(k)]
def error(mean, point):
    e = math.pow(mean[0]-point[0], 2) + math.pow(mean[1]-point[1], 2) + math.pow(mean[2]-point[2], 2) + math.pow(mean[3]-point[3], 2)
    return e
def whichcluster(means, point):
    l = []
    for i in range(len(means)):
        l.append(error(means[i], point))
    return l.index(min(l))
for star in population:
    c = whichcluster(means, star)
    clusters[c].append(star)
pastclusters = clusters
clusters = [[] for i in range(k)]
def mean(cluster):
    onemean = []
    twomean = []
    threemean = []
    fourmean = []
    for i in range(len(cluster)):
        onemean.append(cluster[i][0])
        twomean.append(cluster[i][1])
        threemean.append(cluster[i][2])
        fourmean.append(cluster[i][3])
    return(sum(onemean)/len(onemean), sum(twomean)/len(twomean), sum(threemean)/len(threemean), sum(fourmean)/len(fourmean))
while(not pastclusters==clusters):
    #calculate mean of past clusters
    #loop through stars and assign them to clusters
    #repeat
    means = []
    for cluster in pastclusters:
        means.append(mean(cluster))       
    for star in population:
        c = whichcluster(means, star)
        clusters[c].append(star)
    if(pastclusters == clusters):
        break
    pastclusters = clusters
    clusters = [[] for i in range(k)]
print("MEANS:")
for i in range(k):
    print(means[i])
print("RESULTS:")
for i in range(len(clusters)):
    print("CLUSTER " + str(i+1) + ":", end=" ")
    for j in range(len(clusters[i])):
        print(clusters[i][j][4], end=" ")
    print()