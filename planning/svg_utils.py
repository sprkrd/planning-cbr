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


    def draw_rect_with_text(self, center, size, text, color="white", stroke="black"):
        dwg = self._dwg
        cx,cy = self._transform_point(center)
        sx,sy = size
        top_corner = (cx-sx/2, cy+sy/2)
        dwg.add(dwg.rect(perc(cx-sx/2, cy-sy/2), perc(sx, sy), stroke=stroke, fill=color))
        dwg.add(dwg.text(text, insert=perc(cx-sx*35/100, cy+sy*2/9), fill=stroke))

    def draw_robot(self, holding, size, robot_color="blue", stroke="black"):
        dwg = self._dwg
        cx, cy = 100, 95
        sx, sy = size[0]+1, size[1]+1
        begin = (1/10*cx, cy)
        end = (1/10*cx, cy - 5)
        self.draw_line(begin, end, stroke=robot_color) # Vertical line in the middle
        begin = (1/10*cx - sx/2, cy - 5 )
        end = (1/10*cx - sx/2, cy - 10)
        self.draw_line(begin, end, stroke=robot_color) # Vertical line in the left
        begin = (1/10*cx + sx/2, cy - 5)
        end = (1/10*cx + sx/2, cy - 10)
        self.draw_line(begin, end, stroke=robot_color) # Vertical line in the right
        begin = (1/10*cx - sx/2, cy - 5)
        end = (1/10*cx + sx/2, cy - 5)
        self.draw_line(begin, end, stroke=robot_color) # Horizontal line

        if holding:
            center = (1/10*cx, cy -  sy/2 - 6)
            self.draw_rect_with_text(center, size, holding)

    def draw_people(self, center_of_floor, number_of_people):
        dwg = self._dwg
        dwg.add(dwg.circle(center=center_of_floor, r=2, fill="black"))
        dwg.add(dwg.text(number_of_people, insert=perc(center_of_floor[0]+5, center_of_floor[1])))

    def draw_building(self, floors, size):
        dwg = self._dwg
        

    def svg(self):
        return self._dwg.tostring()

    def _repr_svg_(self):
        return self.svg()


def perc(*t):
    return tuple(map(lambda x: str(x)+"%", t))

