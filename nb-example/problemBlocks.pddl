
(define (problem blocks-00)
(:domain Blocks)
(:objects slot1 - slot slot2 - slot slot3 - slot block01 - block block02 - block block03 - block)
(:init
(= (total-cost) 0)
(clear block01)
(on block01 slot2)
(on block03 slot1)
(on block02 slot3)
(clear block03)
(clear block02)
(handempty))
(:goal (and (clear block01)
(on block02 slot3)
(on block03 slot2)
(clear slot1)
(handempty)
(clear block02)
(on block01 block03)))
(:metric minimize (total-cost)))
