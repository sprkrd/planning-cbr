
(define (problem hanoi-00)
(:domain Hanoi)
(:objects peg1 - peg peg2 - peg peg3 - peg disk01 - disk disk02 - disk disk03 - disk)
(:init
(= (total-cost) 0)
(smaller disk01 disk02)
(smaller disk01 peg1)
(smaller disk03 peg1)
(smaller disk01 peg3)
(smaller disk01 disk03)
(smaller disk01 peg2)
(smaller disk03 peg2)
(smaller disk03 peg3)
(on disk02 disk03)
(on disk01 disk02)
(clear peg2)
(smaller disk02 peg3)
(clear peg3)
(smaller disk02 peg1)
(clear disk01)
(smaller disk02 peg2)
(smaller disk02 disk03)
(on disk03 peg1))
(:goal (and (on disk02 disk03)
(clear peg1)
(clear peg2)
(on disk01 disk02)
(clear disk01)
(on disk03 peg3)))
(:metric minimize (total-cost)))
