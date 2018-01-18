
(define (domain Blocks)
(:requirements :strips :typing :action-costs)
(:types
block - object
slot - object)
(:predicates
(on ?what - block ?from - object)
(holding ?what - block)
(handempty)
(clear ?to - object))
(:functions (total-cost) - number)

(:action pick__block01__slot1
:parameters ()
:precondition (and (clear block01) (on block01 slot1) (handempty))
:effect (and (clear slot1) (holding block01) (not (clear block01)) (not (on block01 slot1)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block01__slot2
:parameters ()
:precondition (and (clear block01) (on block01 slot2) (handempty))
:effect (and (clear slot2) (holding block01) (not (clear block01)) (not (on block01 slot2)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block01__slot3
:parameters ()
:precondition (and (clear block01) (on block01 slot3) (handempty))
:effect (and (clear slot3) (holding block01) (not (clear block01)) (not (on block01 slot3)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block01__block02
:parameters ()
:precondition (and (clear block01) (on block01 block02) (handempty))
:effect (and (clear block02) (holding block01) (not (clear block01)) (not (on block01 block02)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block01__block03
:parameters ()
:precondition (and (clear block01) (on block01 block03) (handempty))
:effect (and (clear block03) (holding block01) (not (clear block01)) (not (on block01 block03)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block02__slot1
:parameters ()
:precondition (and (clear block02) (on block02 slot1) (handempty))
:effect (and (clear slot1) (holding block02) (not (clear block02)) (not (on block02 slot1)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block02__slot2
:parameters ()
:precondition (and (clear block02) (on block02 slot2) (handempty))
:effect (and (clear slot2) (holding block02) (not (clear block02)) (not (on block02 slot2)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block02__slot3
:parameters ()
:precondition (and (clear block02) (on block02 slot3) (handempty))
:effect (and (clear slot3) (holding block02) (not (clear block02)) (not (on block02 slot3)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block02__block01
:parameters ()
:precondition (and (clear block02) (on block02 block01) (handempty))
:effect (and (clear block01) (holding block02) (not (clear block02)) (not (on block02 block01)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block02__block03
:parameters ()
:precondition (and (clear block02) (on block02 block03) (handempty))
:effect (and (clear block03) (holding block02) (not (clear block02)) (not (on block02 block03)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block03__slot1
:parameters ()
:precondition (and (clear block03) (on block03 slot1) (handempty))
:effect (and (clear slot1) (holding block03) (not (clear block03)) (not (on block03 slot1)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block03__slot2
:parameters ()
:precondition (and (clear block03) (on block03 slot2) (handempty))
:effect (and (clear slot2) (holding block03) (not (clear block03)) (not (on block03 slot2)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block03__slot3
:parameters ()
:precondition (and (clear block03) (on block03 slot3) (handempty))
:effect (and (clear slot3) (holding block03) (not (clear block03)) (not (on block03 slot3)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block03__block01
:parameters ()
:precondition (and (clear block03) (on block03 block01) (handempty))
:effect (and (clear block01) (holding block03) (not (clear block03)) (not (on block03 block01)) (not (handempty)) (increase (total-cost) 1))
)



(:action pick__block03__block02
:parameters ()
:precondition (and (clear block03) (on block03 block02) (handempty))
:effect (and (clear block02) (holding block03) (not (clear block03)) (not (on block03 block02)) (not (handempty)) (increase (total-cost) 1))
)



(:action put__block01__slot1
:parameters ()
:precondition (and (holding block01) (clear slot1))
:effect (and (clear block01) (on block01 slot1) (handempty) (not (holding block01)) (not (clear slot1)) (increase (total-cost) 1))
)



(:action put__block01__slot2
:parameters ()
:precondition (and (holding block01) (clear slot2))
:effect (and (clear block01) (on block01 slot2) (handempty) (not (holding block01)) (not (clear slot2)) (increase (total-cost) 1))
)



(:action put__block01__slot3
:parameters ()
:precondition (and (holding block01) (clear slot3))
:effect (and (clear block01) (on block01 slot3) (handempty) (not (holding block01)) (not (clear slot3)) (increase (total-cost) 1))
)



(:action put__block01__block02
:parameters ()
:precondition (and (holding block01) (clear block02))
:effect (and (clear block01) (on block01 block02) (handempty) (not (holding block01)) (not (clear block02)) (increase (total-cost) 1))
)



(:action put__block01__block03
:parameters ()
:precondition (and (holding block01) (clear block03))
:effect (and (clear block01) (on block01 block03) (handempty) (not (holding block01)) (not (clear block03)) (increase (total-cost) 1))
)



(:action put__block02__slot1
:parameters ()
:precondition (and (holding block02) (clear slot1))
:effect (and (clear block02) (on block02 slot1) (handempty) (not (holding block02)) (not (clear slot1)) (increase (total-cost) 1))
)



(:action put__block02__slot2
:parameters ()
:precondition (and (holding block02) (clear slot2))
:effect (and (clear block02) (on block02 slot2) (handempty) (not (holding block02)) (not (clear slot2)) (increase (total-cost) 1))
)



(:action put__block02__slot3
:parameters ()
:precondition (and (holding block02) (clear slot3))
:effect (and (clear block02) (on block02 slot3) (handempty) (not (holding block02)) (not (clear slot3)) (increase (total-cost) 1))
)



(:action put__block02__block01
:parameters ()
:precondition (and (holding block02) (clear block01))
:effect (and (clear block02) (on block02 block01) (handempty) (not (holding block02)) (not (clear block01)) (increase (total-cost) 1))
)



(:action put__block02__block03
:parameters ()
:precondition (and (holding block02) (clear block03))
:effect (and (clear block02) (on block02 block03) (handempty) (not (holding block02)) (not (clear block03)) (increase (total-cost) 1))
)



(:action put__block03__slot1
:parameters ()
:precondition (and (holding block03) (clear slot1))
:effect (and (clear block03) (on block03 slot1) (handempty) (not (holding block03)) (not (clear slot1)) (increase (total-cost) 1))
)



(:action put__block03__slot2
:parameters ()
:precondition (and (holding block03) (clear slot2))
:effect (and (clear block03) (on block03 slot2) (handempty) (not (holding block03)) (not (clear slot2)) (increase (total-cost) 1))
)



(:action put__block03__slot3
:parameters ()
:precondition (and (holding block03) (clear slot3))
:effect (and (clear block03) (on block03 slot3) (handempty) (not (holding block03)) (not (clear slot3)) (increase (total-cost) 1))
)



(:action put__block03__block01
:parameters ()
:precondition (and (holding block03) (clear block01))
:effect (and (clear block03) (on block03 block01) (handempty) (not (holding block03)) (not (clear block01)) (increase (total-cost) 1))
)



(:action put__block03__block02
:parameters ()
:precondition (and (holding block03) (clear block02))
:effect (and (clear block03) (on block03 block02) (handempty) (not (holding block03)) (not (clear block02)) (increase (total-cost) 1))
)
)
