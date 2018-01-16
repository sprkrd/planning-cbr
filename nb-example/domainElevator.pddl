
(define (domain Elevator)
(:requirements :strips :typing :action-costs)
(:types
passenger - object
floor - object)
(:predicates
(origin ?person - passenger ?floor - floor)
(destin ?person - passenger ?floor - floor)
(above ?floor1 - floor ?floor2 - floor)
(boarded ?person - passenger)
(served ?person - passenger)
(lift-at ?floor - floor))
(:functions (total-cost) - number)

(:action board__floor1__passenger01
:parameters ()
:precondition (and (lift-at floor1) (origin passenger01 floor1))
:effect (and (boarded passenger01)  (increase (total-cost) 1))
)



(:action board__floor1__passenger02
:parameters ()
:precondition (and (lift-at floor1) (origin passenger02 floor1))
:effect (and (boarded passenger02)  (increase (total-cost) 1))
)



(:action board__floor1__passenger03
:parameters ()
:precondition (and (lift-at floor1) (origin passenger03 floor1))
:effect (and (boarded passenger03)  (increase (total-cost) 1))
)



(:action board__floor2__passenger01
:parameters ()
:precondition (and (lift-at floor2) (origin passenger01 floor2))
:effect (and (boarded passenger01)  (increase (total-cost) 1))
)



(:action board__floor2__passenger02
:parameters ()
:precondition (and (lift-at floor2) (origin passenger02 floor2))
:effect (and (boarded passenger02)  (increase (total-cost) 1))
)



(:action board__floor2__passenger03
:parameters ()
:precondition (and (lift-at floor2) (origin passenger03 floor2))
:effect (and (boarded passenger03)  (increase (total-cost) 1))
)



(:action board__floor3__passenger01
:parameters ()
:precondition (and (lift-at floor3) (origin passenger01 floor3))
:effect (and (boarded passenger01)  (increase (total-cost) 1))
)



(:action board__floor3__passenger02
:parameters ()
:precondition (and (lift-at floor3) (origin passenger02 floor3))
:effect (and (boarded passenger02)  (increase (total-cost) 1))
)



(:action board__floor3__passenger03
:parameters ()
:precondition (and (lift-at floor3) (origin passenger03 floor3))
:effect (and (boarded passenger03)  (increase (total-cost) 1))
)



(:action board__floor4__passenger01
:parameters ()
:precondition (and (lift-at floor4) (origin passenger01 floor4))
:effect (and (boarded passenger01)  (increase (total-cost) 1))
)



(:action board__floor4__passenger02
:parameters ()
:precondition (and (lift-at floor4) (origin passenger02 floor4))
:effect (and (boarded passenger02)  (increase (total-cost) 1))
)



(:action board__floor4__passenger03
:parameters ()
:precondition (and (lift-at floor4) (origin passenger03 floor4))
:effect (and (boarded passenger03)  (increase (total-cost) 1))
)



(:action depart__floor1__passenger01
:parameters ()
:precondition (and (lift-at floor1) (destin passenger01 floor1) (boarded passenger01))
:effect (and (served passenger01) (not (boarded passenger01)) (increase (total-cost) 1))
)



(:action depart__floor1__passenger02
:parameters ()
:precondition (and (lift-at floor1) (destin passenger02 floor1) (boarded passenger02))
:effect (and (served passenger02) (not (boarded passenger02)) (increase (total-cost) 1))
)



(:action depart__floor1__passenger03
:parameters ()
:precondition (and (lift-at floor1) (destin passenger03 floor1) (boarded passenger03))
:effect (and (served passenger03) (not (boarded passenger03)) (increase (total-cost) 1))
)



(:action depart__floor2__passenger01
:parameters ()
:precondition (and (lift-at floor2) (destin passenger01 floor2) (boarded passenger01))
:effect (and (served passenger01) (not (boarded passenger01)) (increase (total-cost) 1))
)



(:action depart__floor2__passenger02
:parameters ()
:precondition (and (lift-at floor2) (destin passenger02 floor2) (boarded passenger02))
:effect (and (served passenger02) (not (boarded passenger02)) (increase (total-cost) 1))
)



(:action depart__floor2__passenger03
:parameters ()
:precondition (and (lift-at floor2) (destin passenger03 floor2) (boarded passenger03))
:effect (and (served passenger03) (not (boarded passenger03)) (increase (total-cost) 1))
)



(:action depart__floor3__passenger01
:parameters ()
:precondition (and (lift-at floor3) (destin passenger01 floor3) (boarded passenger01))
:effect (and (served passenger01) (not (boarded passenger01)) (increase (total-cost) 1))
)



(:action depart__floor3__passenger02
:parameters ()
:precondition (and (lift-at floor3) (destin passenger02 floor3) (boarded passenger02))
:effect (and (served passenger02) (not (boarded passenger02)) (increase (total-cost) 1))
)



(:action depart__floor3__passenger03
:parameters ()
:precondition (and (lift-at floor3) (destin passenger03 floor3) (boarded passenger03))
:effect (and (served passenger03) (not (boarded passenger03)) (increase (total-cost) 1))
)



(:action depart__floor4__passenger01
:parameters ()
:precondition (and (lift-at floor4) (destin passenger01 floor4) (boarded passenger01))
:effect (and (served passenger01) (not (boarded passenger01)) (increase (total-cost) 1))
)



(:action depart__floor4__passenger02
:parameters ()
:precondition (and (lift-at floor4) (destin passenger02 floor4) (boarded passenger02))
:effect (and (served passenger02) (not (boarded passenger02)) (increase (total-cost) 1))
)



(:action depart__floor4__passenger03
:parameters ()
:precondition (and (lift-at floor4) (destin passenger03 floor4) (boarded passenger03))
:effect (and (served passenger03) (not (boarded passenger03)) (increase (total-cost) 1))
)



(:action drive_down__floor1__floor2
:parameters ()
:precondition (and (lift-at floor1) (above floor2 floor1))
:effect (and (lift-at floor2) (not (lift-at floor1)) (increase (total-cost) 1))
)



(:action drive_down__floor1__floor3
:parameters ()
:precondition (and (lift-at floor1) (above floor3 floor1))
:effect (and (lift-at floor3) (not (lift-at floor1)) (increase (total-cost) 1))
)



(:action drive_down__floor1__floor4
:parameters ()
:precondition (and (lift-at floor1) (above floor4 floor1))
:effect (and (lift-at floor4) (not (lift-at floor1)) (increase (total-cost) 1))
)



(:action drive_down__floor2__floor1
:parameters ()
:precondition (and (lift-at floor2) (above floor1 floor2))
:effect (and (lift-at floor1) (not (lift-at floor2)) (increase (total-cost) 1))
)



(:action drive_down__floor2__floor3
:parameters ()
:precondition (and (lift-at floor2) (above floor3 floor2))
:effect (and (lift-at floor3) (not (lift-at floor2)) (increase (total-cost) 1))
)



(:action drive_down__floor2__floor4
:parameters ()
:precondition (and (lift-at floor2) (above floor4 floor2))
:effect (and (lift-at floor4) (not (lift-at floor2)) (increase (total-cost) 1))
)



(:action drive_down__floor3__floor1
:parameters ()
:precondition (and (lift-at floor3) (above floor1 floor3))
:effect (and (lift-at floor1) (not (lift-at floor3)) (increase (total-cost) 1))
)



(:action drive_down__floor3__floor2
:parameters ()
:precondition (and (lift-at floor3) (above floor2 floor3))
:effect (and (lift-at floor2) (not (lift-at floor3)) (increase (total-cost) 1))
)



(:action drive_down__floor3__floor4
:parameters ()
:precondition (and (lift-at floor3) (above floor4 floor3))
:effect (and (lift-at floor4) (not (lift-at floor3)) (increase (total-cost) 1))
)



(:action drive_down__floor4__floor1
:parameters ()
:precondition (and (lift-at floor4) (above floor1 floor4))
:effect (and (lift-at floor1) (not (lift-at floor4)) (increase (total-cost) 1))
)



(:action drive_down__floor4__floor2
:parameters ()
:precondition (and (lift-at floor4) (above floor2 floor4))
:effect (and (lift-at floor2) (not (lift-at floor4)) (increase (total-cost) 1))
)



(:action drive_down__floor4__floor3
:parameters ()
:precondition (and (lift-at floor4) (above floor3 floor4))
:effect (and (lift-at floor3) (not (lift-at floor4)) (increase (total-cost) 1))
)



(:action drive_up__floor1__floor2
:parameters ()
:precondition (and (lift-at floor1) (above floor1 floor2))
:effect (and (lift-at floor2) (not (lift-at floor1)) (increase (total-cost) 1))
)



(:action drive_up__floor1__floor3
:parameters ()
:precondition (and (lift-at floor1) (above floor1 floor3))
:effect (and (lift-at floor3) (not (lift-at floor1)) (increase (total-cost) 1))
)



(:action drive_up__floor1__floor4
:parameters ()
:precondition (and (lift-at floor1) (above floor1 floor4))
:effect (and (lift-at floor4) (not (lift-at floor1)) (increase (total-cost) 1))
)



(:action drive_up__floor2__floor1
:parameters ()
:precondition (and (lift-at floor2) (above floor2 floor1))
:effect (and (lift-at floor1) (not (lift-at floor2)) (increase (total-cost) 1))
)



(:action drive_up__floor2__floor3
:parameters ()
:precondition (and (lift-at floor2) (above floor2 floor3))
:effect (and (lift-at floor3) (not (lift-at floor2)) (increase (total-cost) 1))
)



(:action drive_up__floor2__floor4
:parameters ()
:precondition (and (lift-at floor2) (above floor2 floor4))
:effect (and (lift-at floor4) (not (lift-at floor2)) (increase (total-cost) 1))
)



(:action drive_up__floor3__floor1
:parameters ()
:precondition (and (lift-at floor3) (above floor3 floor1))
:effect (and (lift-at floor1) (not (lift-at floor3)) (increase (total-cost) 1))
)



(:action drive_up__floor3__floor2
:parameters ()
:precondition (and (lift-at floor3) (above floor3 floor2))
:effect (and (lift-at floor2) (not (lift-at floor3)) (increase (total-cost) 1))
)



(:action drive_up__floor3__floor4
:parameters ()
:precondition (and (lift-at floor3) (above floor3 floor4))
:effect (and (lift-at floor4) (not (lift-at floor3)) (increase (total-cost) 1))
)



(:action drive_up__floor4__floor1
:parameters ()
:precondition (and (lift-at floor4) (above floor4 floor1))
:effect (and (lift-at floor1) (not (lift-at floor4)) (increase (total-cost) 1))
)



(:action drive_up__floor4__floor2
:parameters ()
:precondition (and (lift-at floor4) (above floor4 floor2))
:effect (and (lift-at floor2) (not (lift-at floor4)) (increase (total-cost) 1))
)



(:action drive_up__floor4__floor3
:parameters ()
:precondition (and (lift-at floor4) (above floor4 floor3))
:effect (and (lift-at floor3) (not (lift-at floor4)) (increase (total-cost) 1))
)
)
