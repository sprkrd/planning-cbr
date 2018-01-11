from .hanoi import HanoiDomain
from .blocks import BlocksDomain
from .elevator import ElevatorDomain

domains = {
        "Hanoi": HanoiDomain(),
        "Blocks": BlocksDomain(),
        "Elevator": ElevatorDomain(),
}

