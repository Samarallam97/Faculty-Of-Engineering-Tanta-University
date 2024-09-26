###################################################
############## moving objects #####################
###################################################
class Camera:
    def __init__(self, ex, ey, ez, cx, cy, cz):
        self.ex = ex
        self.ey = ey
        self.ez = ez
        self.cx = cx
        self.cy = cy
        self.cz = cz


class PLAYER:
    def __init__(self, x, y, z, live):
        self.x = x
        self.y = y
        self.z = z
        self.live = live


class DRAWSTRING:
    def __init__(self, x, y, z, text):
        self.x = x
        self.y = y
        self.z = z
        self.text = text
