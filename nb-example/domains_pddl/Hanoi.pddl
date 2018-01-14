
(define (domain Hanoi)
(:requirements :strips :typing :action-costs)
(:types
peg - object
disk - object)
(:predicates
(clear ?what)
(smaller ?o0 - disk ?o1 - object)
(on ?above - disk ?below - object))
(:functions (total-cost) - number)

(:action move
:parameters (?what - disk ?from - object ?to - object)
:precondition (and (clear ?what) (clear ?to) (on ?what ?from) (smaller ?what ?to))
:effect (and (clear ?from) (on ?what ?to) (not (clear ?to)) (not (on ?what ?from)) (increase (total-cost) 1))
)
)
