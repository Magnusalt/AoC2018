import re
import statistics as st


class MovingPoint:
    def __init__(self, x, y, xv, yv):
        self.X = x
        self.Y = y
        self.Xv = xv
        self.Yv = yv

    def stepForward(self):
        self.X += self.Xv
        self.Y += self.Yv

    def stepBackwards(self):
        self.X -= self.Xv
        self.Y -= self.Yv


class PointMap:
    def __init__(self, points):
        self.Points = points
        self.timeSpent = 0

    def stepForward(self):
        for p in self.Points:
            p.stepForward()
        self.timeSpent += 1

    def stepBackwards(self):
        for p in self.Points:
            p.stepBackwards()
        self.timeSpent -= 1

    def getAllX(self):
        return list(map(lambda p: p.X, self.Points))

    def getAllY(self):
        return list(map(lambda p: p.Y, self.Points))

    def getStdDevY(self):
        return st.stdev(map(lambda p: p.Y, self.Points))

    def getMaxMin(self):
        return (max(map(lambda p: p.X, self.Points)), min(map(lambda p: p.X, self.Points)), max(map(lambda p: p.Y, self.Points)), min(map(lambda p: p.Y, self.Points)))


def main():
    with open("10.txt", "r") as f:
        regex = re.compile("<(.+?)>")
        regex_matches = map(regex.findall, f.readlines())
        points = []
        for m in regex_matches:
            (x, y) = map(int, m[0].split(","))
            (xv, yv) = map(int, m[1].split(","))
            points.append(MovingPoint(x, y, xv, yv))
        pm = PointMap(points)

        sd1 = pm.getStdDevY()
        pm.stepForward()
        sd2 = pm.getStdDevY()
        while sd2 < sd1:
            pm.stepForward()
            sd1 = sd2
            sd2 = pm.getStdDevY()

        pm.stepBackwards()

        print(pm.timeSpent)


main()
