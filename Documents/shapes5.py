from graphics import*

Win = GraphWin("Blue Triange", 800, 800)
Win.setCoords(0, 0, 800, 800)

Tri = Polygon(Point(50,50), Point(100, 150), Point(150,50))
Tri.setFill(color_rgb(30,30,230))
Tri.draw(Win)

Ysquare = Polygon(Point(50,750), Point(150, 750), Point(150,650), Point(50,650))
Ysquare.setFill(color_rgb(255,255,0))
Ysquare.draw(Win)

Trectange = Polygon(Point(610,750), Point(750,750), Point(750,690), Point(610,690))
Trectange.setFill(color_rgb(0,128,128))
Trectange.draw(Win)

Win.getMouse()
Win.close()

