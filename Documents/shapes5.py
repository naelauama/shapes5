from graphics import*

winX = int(800)
winY = int(800)
Win = GraphWin("5 Shapes", 800, 800)
Win.setCoords(0, 0, 800, 800)

PTri = Polygon(Point(50,50), Point(100, 150), Point(150,50))
PTri.setFill(color_rgb(249,149,132))
PTri.draw(Win)

Ysquare = Polygon(Point(50,750), Point(150, 750), Point(150,650), Point(50,650))
Ysquare.setFill(color_rgb(255,255,0))
Ysquare.draw(Win)

Trectange = Polygon(Point(610,750), Point(750,750), Point(750,690), Point(610,690))
Trectange.setFill(color_rgb(0,128,128))
Trectange.draw(Win)

Loval = Oval(Point(650, 50), Point(730,150))
Loval.setFill(color_rgb(200,162,200))
Loval.draw(Win)

Bdiamond = Polygon(Point(winX / 2, winY / 2 + 110),
                  Point(winX / 2 + 50, winY / 2),
                  Point(winX / 2, winY / 2 - 110),
                  Point(winX / 2 - 50, winY / 2))
Bdiamond.setFill(color_rgb(100,149,237))
Bdiamond.draw(Win)

Win.getMouse()
Win.close()

