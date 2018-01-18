
(define (problem elevator-00)
(:domain Elevator)
(:objects floor1 - floor floor2 - floor floor3 - floor floor4 - floor passenger01 - passenger passenger02 - passenger passenger03 - passenger)
(:init
(= (total-cost) 0)
(destin passenger01 floor1)
(lift-at floor4)
(above floor1 floor2)
(destin passenger03 floor1)
(destin passenger02 floor3)
(above floor3 floor4)
(above floor2 floor3)
(origin passenger01 floor2)
(origin passenger02 floor1)
(origin passenger03 floor2))
(:goal (and (destin passenger01 floor1)
(above floor1 floor2)
(destin passenger03 floor1)
(destin passenger02 floor3)
(served passenger03)
(served passenger02)
(served passenger01)
(above floor3 floor4)
(above floor2 floor3)
(origin passenger01 floor2)
(origin passenger02 floor1)
(origin passenger03 floor2)))
(:metric minimize (total-cost)))