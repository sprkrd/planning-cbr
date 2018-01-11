from ..planning import Domain, Problem, Operator, all_different
from ..svg_utils import Canvas

from random import choice

 
def random_state(blocks, slots, forced=True): 
    state = []
    top = {slot:slot for slot in slots}
    for block in reversed(blocks):
        slot = choice(slots)
        below = top[slot]
        if forced or below.startswith("block"):
            state.append(("on", block, below))
        top[slot] = block
    for slot in slots:
        state.append(("clear", top[slot]))
    state.append(("handempty",))
    return state


class BlocksDomain(Domain):

    PICK_OP = Operator(
            name="pick",
            parameters=[("?what","block"), ("?from","object")],
            pre=[("clear", "?what"), ("on", "?what", "?from"), ("handempty",)],
            add=[("clear", "?from"), ("holding", "?what")],
            del_=[("clear", "?what"), ("on", "?what", "?from"), ("handempty",)],
            constraints=[all_different],
    )
    
    PUT_OP = Operator(
            name="put",
            parameters=[("?what","block"), ("?to","object")],
            pre=[("holding", "?what"), ("clear", "?to")],
            add=[("clear", "?what"), ("on", "?what", "?to"), ("handempty",)],
            del_=[("holding", "?what"), ("clear", "?to")],
            constraints=[all_different],
    )

    
    def __init__(self):
        super().__init__(
                name="Blocks",
                operators=[BlocksDomain.PICK_OP, BlocksDomain.PUT_OP],
                predicates=[("on", ("?what", "block"), ("?from", "object")), \
                 ("holding", ("?what", "block")), \
                 ("handempty",), \
                 ("clear", ("?to", "object"))],
                types={"block":"object", "slot":"object"}
        )

    def draw(self, problem, state):
        slots = [o for o,t in problem.objects() if "slot" in t]
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
        l = L/(len(slots)+1)
        slot_size = (1, 80)
        slot_x = [i*l for i in range(1,len(slots)+1)]
        block_height = l * 4/5
        block_width = block_height
        canvas = Canvas(size, margin_left, margin_right, margin_bottom)
        canvas.draw_plane(0)
        canvas.draw_robot(holding, (block_width, block_height))

        for i,x in enumerate(slot_x):
            p = "slot" + str(i+1)
            height = 0
            d = stacks.get(p, None)
            while d is not None:
                block_size = int(d[-2:])
                block_center = (x, (height+0.5)*block_height)
                #canvas.draw_rect(block_center, (block_width, block_height))
                #canvas.write_text(d, block_center)
                canvas.draw_rect_with_text(block_center, (block_width, block_height), d)
                d = stacks.get(d, None)
                height += 1
        return canvas.svg()

    def generate_problem(self, n, m=3, name="blocks-00", forced_goal=True):
        slots = ["slot"+str(i) for i in range(1,m+1)]
        blocks = ['block{:02d}'.format(i) for i in range(1,n+1)]
        
        init = random_state(blocks, slots)
        goal = random_state(blocks, slots, forced=forced_goal)

        return Problem(
                name=name,
                domain=self,
                objects=[(p,"slot") for p in slots]+[(d,"block") for d in blocks],
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

