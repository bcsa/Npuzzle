import argparse


class Node:
    def __init__(self, adat, szint, fertek):
        self.adat = adat
        self.szint = szint
        self.fertek = fertek

    def childgen(self):
        x, y = self.urespozicio(self.adat, '_')

        val_list = [[x, y - 1],
                    [x, y + 1],
                    [x - 1, y],
                    [x + 1, y]]
        children = []
        for i in val_list:
            child = self.mozgatas(self.adat, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.szint + 1, 0)
                children.append(child_node)
        return children

    def mozgatas(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.adat) and y2 >= 0 and y2 < len(self.adat):
            temp_puz = []
            temp_puz = self.masolas(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def masolas(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def urespozicio(self, puz, x):
        for i in range(0, len(self.adat)):
            for j in range(0, len(self.adat)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def fszamitas(self, start, goal):
        return self.hszamitas(start.adat, goal) + start.szint

    def hszamitas(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def doit(self, args):
        start = []
        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]

        if args.input:
            fin = open(args.input, "r")
            size = int(fin.readline())
            for i in range(size):
                line = fin.readline()
                line = line.strip()
                line = line.split(" ")
                start.append([])
                for szam in line:
                    start[i].append(szam)
        elif args.rand:
            self.n = args.rand[0]
            steps = args.rand[1]
        else:
            for i in range(3):
                temp = input().split(" ")
                start.append(temp)

        start = Node(start, 0, 0)
        start.fertek = self.fszamitas(start, goal)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            if args.solseq:
                print("")
                for i in cur.adat:
                    for j in i:
                        print(j, end=" ")
                    print("")
            if (self.hszamitas(cur.adat, goal) == 0):
                if args.pcost:
                    print(cur.szint)
                break
            for i in cur.childgen():
                i.fertek = self.fszamitas(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
        self.open.sort(key=lambda x: x.fertek, reverse=False)


parser = argparse.ArgumentParser(description="Astar")
parser.add_argument("-input", type=str)
parser.add_argument("-solseq", action='store_true')
parser.add_argument("-pcost", action='store_true')
parser.add_argument("-nvisited", action='store_true')
#parser.add_argument("-H", type=int)
parser.add_argument("-rand", nargs=2, type=int)
arguments = parser.parse_args()

puz = Puzzle(3)
puz.doit(arguments)