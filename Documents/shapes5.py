from graphics import*

Win = GraphWin("Blue Triange", 800, 800)
Win.setCoords(0, 0, 800, 800)

Tri = Polygon(Point(100,100), Point(150, 200), Point(200,100))
Tri.setFill(color_rgb(30,30,230))
Tri.draw(Win)

PDiamond = Polygon(Point(400,524), Point(500, 424), Point(400,324), Point(300,424))
PDiamond.setFill(color_rgb(255,105,180))
PDiamond.draw(Win)


Win.getMouse()
Win.close()

