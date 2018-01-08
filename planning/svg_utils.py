import svgwrite


class Canvas:

    def __init__(self, size, margin_left=5, margin_right=5, margin_bottom=5):
        self._size = size
        self._margin_left = margin_left
        self._margin_right = margin_right
        self._margin_bottom = margin_bottom
        self._dwg = svgwrite.Drawing(size=(size))

    def _transform_point(self, point):
        return (self._margin_left+point[0], 100-self._margin_bottom-point[1])

    def draw_plane(self, height, stroke="black"):
        dwg = self._dwg
        begin = (0, height)
        end = (100-self._margin_left-self._margin_right, height)
        self.draw_line(begin, end, stroke)

    def draw_line(self, begin, end, stroke="black"):
        dwg = self._dwg
        begin = self._transform_point(begin)
        end = self._transform_point(end)
        dwg.add(dwg.line(perc(*begin), perc(*end), stroke=stroke))

    def draw_rect(self, center, size, color="white", stroke="black"):
        dwg = self._dwg
        cx,cy = self._transform_point(center)
        sx,sy = size
        top_corner = (cx-sx/2, cy+sy/2)
        dwg.add(dwg.rect(perc(cx-sx/2, cy-sy/2), perc(sx, sy), stroke=stroke, fill=color))

    def svg(self):
        return self._dwg.tostring()

    def _repr_svg_(self):
        return self.svg()


def perc(*t):
    return tuple(map(lambda x: str(x)+"%", t))

