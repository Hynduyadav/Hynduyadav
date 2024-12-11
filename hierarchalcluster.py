import csv, itertools, math, random
import numpy as np
import scipy.cluster.hierarchy as scihac
import matplotlib.pyplot as plt

def load_data(filename):
    with open(filename) as csvfile:
        pokemon = []

        reader = itertools.islice(csv.DictReader(csvfile), 20)
        
        for row in reader:
            row.pop("Generation")
            row.pop("Legendary")
            row["#"] = int(row["#"])
            row["Total"] = int(row["Total"])
            row["HP"] = int(row["HP"])
            row["Attack"] = int(row["Attack"])
            row["Defense"] = int(row["Defense"])
            row["Sp. Atk"] = int(row["Sp. Atk"])
            row["Sp. Def"] = int(row["Sp. Def"])
            row["Speed"] = int(row["Speed"])
            pokemon.append(row)
            return pokemon
            def calculate_x_y(stats):
               x = stats["Attack"] + stats["Sp. Atk"] + stats["Speed"]
    y = stats["Defense"] + stats["Sp. Def"] + stats["HP"]
    return (x, y)
    def hac(dataset):
      ds = []
      for (x,y) in dataset:
        if math.isfinite(x) and math.isfinite(y):
                      ds.append((x, y))
                      dataset = ds

                      m = len(dataset)
                      clusterCount = 0
                      origPoints = []
                      for (x, y) in dataset:
                        row = {}

                        row["p"] = (x, y)
        row["cluster"] = clusterCount
        row["cSize"] = 1

        clusterCount += 1

        origPoints.append(row)



        orderedDist = []

        for i in range(m):
           for j in range(m):
            if i<j:
              dict = {}

              for row in origPoints:
                for j in range(m):
                   if i<j:
                    dict = {}

                    for row in origPoints:
                        if row["cluster"] == i:
                           dict["p1"] = row["p"]
                           dict["p1origin"] = row["cluster"]
                        if row["cluster"] == j:
                           dict["p2"] = row["p"]
                           dict["p2origin"] = row["cluster"]

                           dict["dist"] = math.dist(dict["p1"], dict["p2"])
                           orderedDist.append(dict)

                           orderedDist = sorted(orderedDist, key = lambda dict: (dict["dist"], origPoints[dict["p1origin"]]["cluster"], origPoints[dict["p2origin"]]["cluster"]))

                           Z = np.zeros((m-1, 4))

                           Zcount = 0

                           while (Zcount < m - 1):

                             dict = orderedDist[0]


                             p1origin = dict["p1origin"]
        p2origin = dict["p2origin"]


        if origPoints[p1origin]["cluster"] == origPoints[p2origin]["cluster"]:
            orderedDist.remove(dict)
            continue


            if origPoints[p1origin]["cluster"] < origPoints[p2origin]["cluster"]:
               Z[Zcount][0] = origPoints[p1origin]["cluster"]
               Z[Zcount][1] = origPoints[p2origin]["cluster"]
        else:
               Z[Zcount][0] = origPoints[p2origin]["cluster"]
               Z[Zcount][1] = origPoints[p1origin]["cluster"]
        Z[Zcount][2] = dict["dist"]
        Z[Zcount][3] = origPoints[p1origin]["cSize"] + origPoints[p2origin]["cSize"]

        for row in origPoints:
            if (row["cluster"] == Z[Zcount][0]) or (row["cluster"] == Z[Zcount][1]):
                row["cluster"] = clusterCount
                row["cSize"] = Z[Zcount][3]


                orderedDist.remove(dict)

                for dict in orderedDist:
                    if origPoints[dict["p1origin"]]["cluster"] > origPoints[dict["p2origin"]]["cluster"]:
                        t = dict["p1origin"]
                dict["p1origin"] = dict["p2origin"]
                dict["p2origin"] = t

                (t1, t2) = dict["p1"]
                dict["p1"] = dict["p2"]
                dict["p2"] = (t1, t2)

                orderedDist = sorted(orderedDist, key = lambda dict: (dict["dist"], origPoints[dict["p1origin"]]["cluster"], origPoints[dict["p2origin"]]["cluster"]))

                clusterCount += 1
        Zcount += 1

        Z = np.asmatrix(Z)
    return Z

    def random_x_y(m):
        arr = []

        for i in range(m):
            x = random.randint(1, 359)
        y = random.randint(1, 359)
        arr.append((x,y))

        return arr



        def imshow_hac(dataset):

          ds = []
    for (x,y) in dataset:
        if math.isfinite(x) and math.isfinite(y):
            ds.append((x, y))
    dataset = ds

    fig = plt.figure()
    ax = fig.add_subplot()
    for (x, y) in dataset:
        ax = plt.scatter(x, y)
    plt.pause(0.1)

    m = len(dataset)

    clusterCount = 0


    origPoints = []


    for (x, y) in dataset:
        row = {}

        row["p"] = (x, y)
        row["cluster"] = clusterCount
        row["cSize"] = 1

        clusterCount += 1

        origPoints.append(row)


        orderedDist = []

        for i in range(m):
            for j in range(m):
                if i<j:
                   dict = {}
                   for row in origPoints:
                    if row["cluster"] == i:
                        dict["p1"] = row["p"]
                        dict["p1origin"] = row["cluster"]
                    if row["cluster"] == j:
                        dict["p2"] = row["p"]
                        dict["p2origin"] = row["cluster"]

                        dict["dist"] = math.dist(dict["p1"], dict["p2"])

                        orderedDist.append(dict)

                        orderedDist = sorted(orderedDist, key = lambda dict: (dict["dist"], origPoints[dict["p1origin"]]["cluster"], origPoints[dict["p2origin"]]["cluster"]))

                        Z = np.zeros((m-1, 4))
                        Zcount = 0

                        while (Zcount < m - 1):

                            dict = orderedDist[0]

                            p1origin = dict["p1origin"]
                            p2origin = dict["p2origin"]

                            if origPoints[p1origin]["cluster"] == origPoints[p2origin]["cluster"]:
                                orderedDist.remove(dict)
            continue


            if origPoints[p1origin]["cluster"] < origPoints[p2origin]["cluster"]:
             Z[Zcount][0] = origPoints[p1origin]["cluster"]
            Z[Zcount][1] = origPoints[p2origin]["cluster"]
        else:
            Z[Zcount][0] = origPoints[p2origin]["cluster"]
            Z[Zcount][1] = origPoints[p1origin]["cluster"]
        Z[Zcount][2] = dict["dist"]
        Z[Zcount][3] = origPoints[p1origin]["cSize"] + origPoints[p2origin]["cSize"]


        for row in origPoints:
            if (row["cluster"] == Z[Zcount][0]) or (row["cluster"] == Z[Zcount][1]):
                row["cluster"] = clusterCount
                row["cSize"] = Z[Zcount][3]

                (x1, y1) = origPoints[p1origin]["p"]
        (x2, y2) = origPoints[p2origin]["p"]
        ax = plt.plot((x1, x2), (y1, y2))
        plt.pause(0.1)

        orderedDist.remove(dict)

        for dict in orderedDist:
            if origPoints[dict["p1origin"]]["cluster"] > origPoints[dict["p2origin"]]["cluster"]:
                t = dict["p1origin"]
                dict["p1origin"] = dict["p2origin"]
                dict["p2origin"] = t

                (t1, t2) = dict["p1"]
                dict["p1"] = dict["p2"]
                dict["p2"] = (t1, t2)

                orderedDist = sorted(orderedDist, key = lambda dict: (dict["dist"], origPoints[dict["p1origin"]]["cluster"], origPoints[dict["p2origin"]]["cluster"]))


                clusterCount += 1
                Zcount += 1

                plt.show()

                Z = np.asmatrix(Z)
    return Z

    
def main():

    pokemon = load_data("Pokemon.csv")






    arr = random_x_y(50)


    print("\n\n my hac:\n")
    print(imshow_hac(arr))


    print("\n\nscihac:\n")
    print(scihac.linkage(arr))

    if __name__=="__main__": 
      main()










                    




