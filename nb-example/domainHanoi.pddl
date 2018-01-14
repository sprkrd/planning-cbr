
(define (domain Hanoi)
(:requirements :strips :typing :action-costs)
(:types
disk - object
peg - object)
(:predicates
(clear ?what)
(on ?above - disk ?below - object))
(:functions (total-cost) - number)

(:action move__disk01__peg1__peg2
:parameters ()
:precondition (and (clear disk01) (clear peg2) (on disk01 peg1))
:effect (and (clear peg1) (on disk01 peg2) (not (clear peg2)) (not (on disk01 peg1)) (increase (total-cost) 1))
)



(:action move__disk01__peg1__peg3
:parameters ()
:precondition (and (clear disk01) (clear peg3) (on disk01 peg1))
:effect (and (clear peg1) (on disk01 peg3) (not (clear peg3)) (not (on disk01 peg1)) (increase (total-cost) 1))
)



(:action move__disk01__peg1__disk02
:parameters ()
:precondition (and (clear disk01) (clear disk02) (on disk01 peg1))
:effect (and (clear peg1) (on disk01 disk02) (not (clear disk02)) (not (on disk01 peg1)) (increase (total-cost) 1))
)



(:action move__disk01__peg1__disk03
:parameters ()
:precondition (and (clear disk01) (clear disk03) (on disk01 peg1))
:effect (and (clear peg1) (on disk01 disk03) (not (clear disk03)) (not (on disk01 peg1)) (increase (total-cost) 1))
)



(:action move__disk01__peg2__peg1
:parameters ()
:precondition (and (clear disk01) (clear peg1) (on disk01 peg2))
:effect (and (clear peg2) (on disk01 peg1) (not (clear peg1)) (not (on disk01 peg2)) (increase (total-cost) 1))
)



(:action move__disk01__peg2__peg3
:parameters ()
:precondition (and (clear disk01) (clear peg3) (on disk01 peg2))
:effect (and (clear peg2) (on disk01 peg3) (not (clear peg3)) (not (on disk01 peg2)) (increase (total-cost) 1))
)



(:action move__disk01__peg2__disk02
:parameters ()
:precondition (and (clear disk01) (clear disk02) (on disk01 peg2))
:effect (and (clear peg2) (on disk01 disk02) (not (clear disk02)) (not (on disk01 peg2)) (increase (total-cost) 1))
)



(:action move__disk01__peg2__disk03
:parameters ()
:precondition (and (clear disk01) (clear disk03) (on disk01 peg2))
:effect (and (clear peg2) (on disk01 disk03) (not (clear disk03)) (not (on disk01 peg2)) (increase (total-cost) 1))
)



(:action move__disk01__peg3__peg1
:parameters ()
:precondition (and (clear disk01) (clear peg1) (on disk01 peg3))
:effect (and (clear peg3) (on disk01 peg1) (not (clear peg1)) (not (on disk01 peg3)) (increase (total-cost) 1))
)



(:action move__disk01__peg3__peg2
:parameters ()
:precondition (and (clear disk01) (clear peg2) (on disk01 peg3))
:effect (and (clear peg3) (on disk01 peg2) (not (clear peg2)) (not (on disk01 peg3)) (increase (total-cost) 1))
)



(:action move__disk01__peg3__disk02
:parameters ()
:precondition (and (clear disk01) (clear disk02) (on disk01 peg3))
:effect (and (clear peg3) (on disk01 disk02) (not (clear disk02)) (not (on disk01 peg3)) (increase (total-cost) 1))
)



(:action move__disk01__peg3__disk03
:parameters ()
:precondition (and (clear disk01) (clear disk03) (on disk01 peg3))
:effect (and (clear peg3) (on disk01 disk03) (not (clear disk03)) (not (on disk01 peg3)) (increase (total-cost) 1))
)



(:action move__disk01__disk02__peg1
:parameters ()
:precondition (and (clear disk01) (clear peg1) (on disk01 disk02))
:effect (and (clear disk02) (on disk01 peg1) (not (clear peg1)) (not (on disk01 disk02)) (increase (total-cost) 1))
)



(:action move__disk01__disk02__peg2
:parameters ()
:precondition (and (clear disk01) (clear peg2) (on disk01 disk02))
:effect (and (clear disk02) (on disk01 peg2) (not (clear peg2)) (not (on disk01 disk02)) (increase (total-cost) 1))
)



(:action move__disk01__disk02__peg3
:parameters ()
:precondition (and (clear disk01) (clear peg3) (on disk01 disk02))
:effect (and (clear disk02) (on disk01 peg3) (not (clear peg3)) (not (on disk01 disk02)) (increase (total-cost) 1))
)



(:action move__disk01__disk02__disk03
:parameters ()
:precondition (and (clear disk01) (clear disk03) (on disk01 disk02))
:effect (and (clear disk02) (on disk01 disk03) (not (clear disk03)) (not (on disk01 disk02)) (increase (total-cost) 1))
)



(:action move__disk01__disk03__peg1
:parameters ()
:precondition (and (clear disk01) (clear peg1) (on disk01 disk03))
:effect (and (clear disk03) (on disk01 peg1) (not (clear peg1)) (not (on disk01 disk03)) (increase (total-cost) 1))
)



(:action move__disk01__disk03__peg2
:parameters ()
:precondition (and (clear disk01) (clear peg2) (on disk01 disk03))
:effect (and (clear disk03) (on disk01 peg2) (not (clear peg2)) (not (on disk01 disk03)) (increase (total-cost) 1))
)



(:action move__disk01__disk03__peg3
:parameters ()
:precondition (and (clear disk01) (clear peg3) (on disk01 disk03))
:effect (and (clear disk03) (on disk01 peg3) (not (clear peg3)) (not (on disk01 disk03)) (increase (total-cost) 1))
)



(:action move__disk01__disk03__disk02
:parameters ()
:precondition (and (clear disk01) (clear disk02) (on disk01 disk03))
:effect (and (clear disk03) (on disk01 disk02) (not (clear disk02)) (not (on disk01 disk03)) (increase (total-cost) 1))
)



(:action move__disk02__peg1__peg2
:parameters ()
:precondition (and (clear disk02) (clear peg2) (on disk02 peg1))
:effect (and (clear peg1) (on disk02 peg2) (not (clear peg2)) (not (on disk02 peg1)) (increase (total-cost) 1))
)



(:action move__disk02__peg1__peg3
:parameters ()
:precondition (and (clear disk02) (clear peg3) (on disk02 peg1))
:effect (and (clear peg1) (on disk02 peg3) (not (clear peg3)) (not (on disk02 peg1)) (increase (total-cost) 1))
)



(:action move__disk02__peg1__disk03
:parameters ()
:precondition (and (clear disk02) (clear disk03) (on disk02 peg1))
:effect (and (clear peg1) (on disk02 disk03) (not (clear disk03)) (not (on disk02 peg1)) (increase (total-cost) 1))
)



(:action move__disk02__peg2__peg1
:parameters ()
:precondition (and (clear disk02) (clear peg1) (on disk02 peg2))
:effect (and (clear peg2) (on disk02 peg1) (not (clear peg1)) (not (on disk02 peg2)) (increase (total-cost) 1))
)



(:action move__disk02__peg2__peg3
:parameters ()
:precondition (and (clear disk02) (clear peg3) (on disk02 peg2))
:effect (and (clear peg2) (on disk02 peg3) (not (clear peg3)) (not (on disk02 peg2)) (increase (total-cost) 1))
)



(:action move__disk02__peg2__disk03
:parameters ()
:precondition (and (clear disk02) (clear disk03) (on disk02 peg2))
:effect (and (clear peg2) (on disk02 disk03) (not (clear disk03)) (not (on disk02 peg2)) (increase (total-cost) 1))
)



(:action move__disk02__peg3__peg1
:parameters ()
:precondition (and (clear disk02) (clear peg1) (on disk02 peg3))
:effect (and (clear peg3) (on disk02 peg1) (not (clear peg1)) (not (on disk02 peg3)) (increase (total-cost) 1))
)



(:action move__disk02__peg3__peg2
:parameters ()
:precondition (and (clear disk02) (clear peg2) (on disk02 peg3))
:effect (and (clear peg3) (on disk02 peg2) (not (clear peg2)) (not (on disk02 peg3)) (increase (total-cost) 1))
)



(:action move__disk02__peg3__disk03
:parameters ()
:precondition (and (clear disk02) (clear disk03) (on disk02 peg3))
:effect (and (clear peg3) (on disk02 disk03) (not (clear disk03)) (not (on disk02 peg3)) (increase (total-cost) 1))
)



(:action move__disk02__disk03__peg1
:parameters ()
:precondition (and (clear disk02) (clear peg1) (on disk02 disk03))
:effect (and (clear disk03) (on disk02 peg1) (not (clear peg1)) (not (on disk02 disk03)) (increase (total-cost) 1))
)



(:action move__disk02__disk03__peg2
:parameters ()
:precondition (and (clear disk02) (clear peg2) (on disk02 disk03))
:effect (and (clear disk03) (on disk02 peg2) (not (clear peg2)) (not (on disk02 disk03)) (increase (total-cost) 1))
)



(:action move__disk02__disk03__peg3
:parameters ()
:precondition (and (clear disk02) (clear peg3) (on disk02 disk03))
:effect (and (clear disk03) (on disk02 peg3) (not (clear peg3)) (not (on disk02 disk03)) (increase (total-cost) 1))
)



(:action move__disk03__peg1__peg2
:parameters ()
:precondition (and (clear disk03) (clear peg2) (on disk03 peg1))
:effect (and (clear peg1) (on disk03 peg2) (not (clear peg2)) (not (on disk03 peg1)) (increase (total-cost) 1))
)



(:action move__disk03__peg1__peg3
:parameters ()
:precondition (and (clear disk03) (clear peg3) (on disk03 peg1))
:effect (and (clear peg1) (on disk03 peg3) (not (clear peg3)) (not (on disk03 peg1)) (increase (total-cost) 1))
)



(:action move__disk03__peg2__peg1
:parameters ()
:precondition (and (clear disk03) (clear peg1) (on disk03 peg2))
:effect (and (clear peg2) (on disk03 peg1) (not (clear peg1)) (not (on disk03 peg2)) (increase (total-cost) 1))
)



(:action move__disk03__peg2__peg3
:parameters ()
:precondition (and (clear disk03) (clear peg3) (on disk03 peg2))
:effect (and (clear peg2) (on disk03 peg3) (not (clear peg3)) (not (on disk03 peg2)) (increase (total-cost) 1))
)



(:action move__disk03__peg3__peg1
:parameters ()
:precondition (and (clear disk03) (clear peg1) (on disk03 peg3))
:effect (and (clear peg3) (on disk03 peg1) (not (clear peg1)) (not (on disk03 peg3)) (increase (total-cost) 1))
)



(:action move__disk03__peg3__peg2
:parameters ()
:precondition (and (clear disk03) (clear peg2) (on disk03 peg3))
:effect (and (clear peg3) (on disk03 peg2) (not (clear peg2)) (not (on disk03 peg3)) (increase (total-cost) 1))
)
)
