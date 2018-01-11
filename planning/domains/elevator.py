from ..planning import Domain, Problem, Operator, all_different
from ..svg_utils import Canvas

from random import choice

 
def random_state(passengers, floors): 
    init = []
    goal = []
    for passenger in reversed(passengers):
        floor = choice(floors)
        init.append(("origin", passenger, floor))

    for passenger in reversed(passengers):
        floor = choice(floors)
        init.append(("destin", passenger, floor))

    for j in range (len(floors)-1):
        init.append(("above", floors[j], floors[j+1]))
    
    for passenger in passengers:
        goal.append(("served", passenger))
    
    floor = choice(floors)
    init.append(("lift-at", floor))
    return init, goal


class ElevatorDomain(Domain):
# [("predicate", ("?parameter1", "type"/None)), ("?parameter2", "type"/None))]

    BOARD_OP = Operator(
            name="board",
            parameters=[("?f","floor"), ("?p","passenger")],
            pre=[("lift-at", "?f"), ("origin", "?p", "?f")],
            add=[("boarded", "?p")],
            del_=[],
            constraints=[all_different],
    )
    
    DEPART_OP = Operator(
            name="depart",
            parameters=[("?f","floor"), ("?p","passenger")],
            pre=[("lift-at", "?f"), ("destin", "?p", "?f"), ("boarded", "?p")],
            add=[("served", "?p")],
            del_=[("boarded", "?p")],
            constraints=[all_different],
    )

    DRIVE_UP_OP = Operator(
            name="drive_up",
            parameters=[("?f1","floor"), ("?f2","floor")],
            pre=[("lift-at", "?f1"), ("above", "?f1", "?f2")],
            add=[("lift-at", "?f2")],
            del_=[("lift-at", "?f1")],
            constraints=[all_different],
    )

    DRIVE_DOWN_OP = Operator(
            name="drive_down",
            parameters=[("?f1","floor"), ("?f2","floor")],
            pre=[("lift-at", "?f1"), ("above", "?f2", "?f1")],
            add=[("lift-at", "?f2")],
            del_=[("lift-at", "?f1")],
            constraints=[all_different],
    )


    
    def __init__(self):
        super().__init__(
                name="Elevator",
                operators=[ElevatorDomain.BOARD_OP, ElevatorDomain.DEPART_OP, \
                 ElevatorDomain.DRIVE_DOWN_OP, ElevatorDomain.DRIVE_UP_OP],
                predicates=[("origin", ("?person", "passenger"), ("?floor", "floor")), \
                 ("destin", ("?person", "passenger"), ("?floor", "floor")), \
                 ("above", ("?floor1", "floor"), ("?floor2", "floor")), \
                 ("boarded", ("?person", "passenger")), \
                 ("served", ("?person", "passenger")),
                 ("lift-at", ("?floor", "floor"))],
                types={"passenger":"object", "floor":"object"}
        )

    def draw(self, problem, state):
        floors = [o for o,t in problem.objects() if "floor" in t]
        stacks = {}
        holding = None
        for pred in state:
            if pred[0] == "on":
                above = pred[1]
                below = pred[2]
                stacks[below] = above
            elif pred[0] == "holding":
                holding = pred[1]

        margin_left = 5
        margin_right = 5
        margin_bottom = 5
        size = (600, 300) # canvas size
        L = 100 - margin_left - margin_right
        l = L/(len(floors)+1)
        floor_size = (1, 80)
        floor_x = [i*l for i in range(1,len(floors)+1)]
        passenger_height = l * 4/5
        passenger_width = passenger_height
        canvas = Canvas(size, margin_left, margin_right, margin_bottom)
        canvas.draw_plane(0)
        canvas.draw_robot(holding, (passenger_width, passenger_height))

        for i,x in enumerate(floor_x):
            p = "floor" + str(i+1)
            height = 0
            d = stacks.get(p, None)
            while d is not None:
                passenger_size = int(d[-2:])
                passenger_center = (x, (height+0.5)*passenger_height)
                #canvas.draw_rect(passenger_center, (passenger_width, passenger_height))
                #canvas.write_text(d, passenger_center)
                canvas.draw_rect_with_text(passenger_center, (passenger_width, passenger_height), d)
                d = stacks.get(d, None)
                height += 1
        return canvas.svg()

    def generate_problem(self, n, m=3, name="elevator-00"):
        floors = ["floor"+str(i) for i in range(1,m+1)]
        passengers = ['passenger{:02d}'.format(i) for i in range(1,n+1)]
        
        init, goal = random_state(passengers, floors)

        return Problem(
                name=name,
                domain=self,
                objects=[(p,"floor") for p in floors]+[(d,"passenger") for d in passengers],
                init=init,
                goal=goal,
        )


if __name__ == "__main__":
    # quick test
    domain = ElevatorDomain()
    print(domain)
    problem = domain.generate_problem(4, name="random")
    print(problem)

