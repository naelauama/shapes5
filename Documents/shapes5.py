from graphics import*

Win = GraphWin("Blue Triange", 800, 800)
Win.setCoords(0, 0, 800, 800)

Tri = Polygon(Point(50,50), Point(100, 150), Point(150,50))
Tri.setFill(color_rgb(30,30,230))
Tri.draw(Win)

Ysquare = Polygon(Point(50,750), Point(150, 750), Point(150,650), Point(50,650))
Ysquare.setFill(color_rgb(255,255,0))
Ysquare.draw(Win)


Win.getMouse()
Win.close()

