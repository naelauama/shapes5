from graphics import*

TriWin = GraphWin("Blue Triange", 300, 300)
TriWin.setCoords(0, 0, 300, 300)

Tri = Polygon(Point(100,100), Point(150, 200), Point(200,100))
Tri.setFill(color_rgb(30,30,230))
Tri.draw(TriWin)

TriWin.getMouse()
TriWin.close()
