from ..planning import Domain, Problem, Operator, all_different
from ..svg_utils import Canvas

from random import choice


def size_constraint(sigma):
    what = sigma["?what"]
    from_ = sigma["?from"]
    to = sigma["?to"]
    size_what = int(what[-2:])
    valid_from = from_.startswith("peg") or size_what < int(from_[-2:])
    valid_to = to.startswith("peg") or size_what < int(to[-2:])
    return valid_from and valid_to


def random_state(disks, pegs):
    state = []
    top = {peg:peg for peg in pegs}
    for disk in reversed(disks):
        peg = choice(pegs)
        below = top[peg]
        state.append(("on", disk, below))
        top[peg] = disk
    for peg in pegs:
        state.append(("clear", top[peg]))
    return state


def deterministic_state(disks, pegs, p):
    state = []
    below = p
    for disk in reversed(disks):
        state.append(("on", disk, below))
        below = disk
    state.append(("clear", below))
    for peg in pegs:
        if peg != p:
            state.append(("clear", peg))
    return state


class HanoiDomain(Domain):

    MOVE_OP = Operator(
            name="move",
            parameters=[("?what","disk"), ("?from","object"), ("?to","object")],
            pre=[("clear", "?what"), ("clear", "?to"), ("on", "?what", "?from")],
            add=[("clear", "?from"), ("on", "?what", "?to")],
            del_=[("clear", "?to"), ("on", "?what", "?from")],
            constraints=[all_different, size_constraint],
    )
    
    def __init__(self):
        super().__init__(
                name="Hanoi",
                operators=[HanoiDomain.MOVE_OP],
                predicates=[("clear", "?what"),
                    ("on", ("?above", "disk"), ("?below", "object"))],
                types={"disk":"object", "peg":"object"}
        )

    def draw(self, problem, state):
        pegs = [o for o,t in problem.objects() if "peg" in t]
        stacks = {}
        for pred in state:
            if pred[0] == "on":
                above = pred[1]
                below = pred[2]
                stacks[below] = above
        margin_left = 5
        margin_right = 5
        margin_bottom = 5
        size = (500, 200) # canvas size
        L = 100 - margin_left - margin_right
        l = L/(len(pegs)+1)
        peg_size = (1, 80)
        peg_x = [i*l for i in range(1,len(pegs)+1)]
        peg_y = peg_size[1]/2
        disk_height = 4
        disk_min_width = peg_size[0]*1.618
        canvas = Canvas(size, margin_left, margin_right, margin_bottom)
        canvas.draw_plane(0)
        for x in peg_x:
            canvas.draw_rect((x, peg_y), peg_size)
        for i,x in enumerate(peg_x):
            p = "peg" + str(i+1)
            height = 0
            d = stacks.get(p, None)
            while d is not None:
                disk_size = int(d[-2:])
                disk_width = disk_min_width + (disk_size-1)*1.618
                disk_center = (x, (height+0.5)*disk_height)
                canvas.draw_rect(disk_center, (disk_width, disk_height))
                d = stacks.get(d, None)
                height += 1
        return canvas.svg()

    def generate_problem(self, n, m=3, random=False, name="hanoi-00"):
        pegs = ["peg"+str(i) for i in range(1,m+1)]
        disks = ['disk{:02d}'.format(i) for i in range(1,n+1)]
        if random:
            init = random_state(disks, pegs)
            goal = random_state(disks, pegs)
        else:
            init = deterministic_state(disks, pegs, "peg1")
            goal = deterministic_state(disks, pegs, "peg"+str(m))
        return Problem(
                name=name,
                domain=self,
                objects=[(p,"peg") for p in pegs]+[(d,"disk") for d in disks],
                init=init,
                goal=goal,
        )


if __name__ == "__main__":
    # quick test
    domain = HanoiDomain()
    print(domain)
    problem = domain.generate_problem(4, random=True, name="random")
    print(problem)
    problem = domain.generate_problem(4, random=False, name="deterministic")
    print(problem)
    print(problem.init()._repr_svg_())

