from ..planning import Domain, Problem, Operator, all_different
from ..svg_utils import Canvas

from random import choice

 
def random_state(passengers, floors, g): 
    init = []
    goal = []
    origins = {}
    for passenger in passengers:
        floor = choice(floors)
        init.append(("origin", passenger, floor))
        origins[passenger] = floor
        if not g:
            goal.append(("origin", passenger, floor))

    for passenger in passengers:
        floor = choice(floors)
        while floor == origins[passenger]:
            floor = choice(floors)
        init.append(("destin", passenger, floor))
        if not g:
            goal.append(("destin", passenger, floor))

    for j in range (len(floors)-1):
        init.append(("above", floors[j], floors[j+1]))
        if not g:
            goal.append(("above", floors[j], floors[j+1]))
    
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

        margin_left = 5
        margin_right = 5
        margin_bottom = 5
        size = (400, 220) # canvas size
        
        
        number_of_people = 3
        canvas = Canvas(size, margin_left, margin_right, margin_bottom)

        state_preds = state.predicates()

        destinations = [pred[1:] for pred in state_preds if pred[0] == "destin"]
        origins = {pred[1]: pred[2] for pred in state_preds if pred[0] == "origin"}
        served = [pred[1] for pred in state_preds if pred[0] == "served"]
        boarded = [pred[1] for pred in state_preds if pred[0] == "boarded"]
        lift_at = [pred[1] for pred in state_preds if pred[0] == "lift-at"][0]
        lift_floor = int(lift_at[-1])

        people_distribution = {f:0 for f in floors}

        for passenger, destin in destinations:
            if passenger not in boarded:
                if passenger in served:
                    floor = destin
                else:
                    floor = origins[passenger]
                people_distribution[floor] += 1

        # print(people_distribution)
        canvas.draw_building(len(floors), people_distribution)
        canvas.draw_lift(lift_floor, len(boarded), len(floors))
            
        return canvas.svg()

    def generate_problem(self, n, m=3, name="elevator-00", goal=False):
        floors = ["floor"+str(i) for i in range(1,m+1)]
        passengers = ['passenger{:02d}'.format(i) for i in range(1,n+1)]
        
        init, goal = random_state(passengers, floors, goal)

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

