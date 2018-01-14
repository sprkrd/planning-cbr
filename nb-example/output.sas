begin_version
3
end_version
begin_metric
1
end_metric
10
begin_variable
var0
-1
2
Atom clear(slot1)
<none of those>
end_variable
begin_variable
var1
-1
2
Atom clear(slot2)
<none of those>
end_variable
begin_variable
var2
-1
2
Atom clear(block03)
NegatedAtom clear(block03)
end_variable
begin_variable
var3
-1
6
Atom holding(block03)
Atom on(block03, block01)
Atom on(block03, block02)
Atom on(block03, slot1)
Atom on(block03, slot2)
Atom on(block03, slot3)
end_variable
begin_variable
var4
-1
2
Atom clear(slot3)
<none of those>
end_variable
begin_variable
var5
-1
6
Atom holding(block01)
Atom on(block01, block02)
Atom on(block01, block03)
Atom on(block01, slot1)
Atom on(block01, slot2)
Atom on(block01, slot3)
end_variable
begin_variable
var6
-1
6
Atom holding(block02)
Atom on(block02, block01)
Atom on(block02, block03)
Atom on(block02, slot1)
Atom on(block02, slot2)
Atom on(block02, slot3)
end_variable
begin_variable
var7
-1
2
Atom clear(block01)
NegatedAtom clear(block01)
end_variable
begin_variable
var8
-1
2
Atom clear(block02)
NegatedAtom clear(block02)
end_variable
begin_variable
var9
-1
2
Atom handempty()
NegatedAtom handempty()
end_variable
7
begin_mutex_group
4
7 0
5 0
6 1
3 1
end_mutex_group
begin_mutex_group
4
8 0
5 1
6 0
3 2
end_mutex_group
begin_mutex_group
4
2 0
5 2
6 2
3 0
end_mutex_group
begin_mutex_group
4
0 0
5 3
6 3
3 3
end_mutex_group
begin_mutex_group
4
1 0
5 4
6 4
3 4
end_mutex_group
begin_mutex_group
4
4 0
5 5
6 5
3 5
end_mutex_group
begin_mutex_group
4
9 0
5 0
6 0
3 0
end_mutex_group
begin_state
0
1
1
5
1
4
2
0
0
0
end_state
begin_goal
7
3 4
4 0
5 3
6 2
7 0
8 0
9 0
end_goal
30
begin_operator
pick__block01__block02 
0
4
0 7 0 1
0 8 -1 0
0 9 0 1
0 5 1 0
1
end_operator
begin_operator
pick__block01__block03 
0
4
0 7 0 1
0 2 -1 0
0 9 0 1
0 5 2 0
1
end_operator
begin_operator
pick__block01__slot1 
0
4
0 7 0 1
0 0 -1 0
0 9 0 1
0 5 3 0
1
end_operator
begin_operator
pick__block01__slot2 
0
4
0 7 0 1
0 1 -1 0
0 9 0 1
0 5 4 0
1
end_operator
begin_operator
pick__block01__slot3 
0
4
0 7 0 1
0 4 -1 0
0 9 0 1
0 5 5 0
1
end_operator
begin_operator
pick__block02__block01 
0
4
0 7 -1 0
0 8 0 1
0 9 0 1
0 6 1 0
1
end_operator
begin_operator
pick__block02__block03 
0
4
0 8 0 1
0 2 -1 0
0 9 0 1
0 6 2 0
1
end_operator
begin_operator
pick__block02__slot1 
0
4
0 8 0 1
0 0 -1 0
0 9 0 1
0 6 3 0
1
end_operator
begin_operator
pick__block02__slot2 
0
4
0 8 0 1
0 1 -1 0
0 9 0 1
0 6 4 0
1
end_operator
begin_operator
pick__block02__slot3 
0
4
0 8 0 1
0 4 -1 0
0 9 0 1
0 6 5 0
1
end_operator
begin_operator
pick__block03__block01 
0
4
0 7 -1 0
0 2 0 1
0 9 0 1
0 3 1 0
1
end_operator
begin_operator
pick__block03__block02 
0
4
0 8 -1 0
0 2 0 1
0 9 0 1
0 3 2 0
1
end_operator
begin_operator
pick__block03__slot1 
0
4
0 2 0 1
0 0 -1 0
0 9 0 1
0 3 3 0
1
end_operator
begin_operator
pick__block03__slot2 
0
4
0 2 0 1
0 1 -1 0
0 9 0 1
0 3 4 0
1
end_operator
begin_operator
pick__block03__slot3 
0
4
0 2 0 1
0 4 -1 0
0 9 0 1
0 3 5 0
1
end_operator
begin_operator
put__block01__block02 
0
4
0 7 -1 0
0 8 0 1
0 9 -1 0
0 5 0 1
1
end_operator
begin_operator
put__block01__block03 
0
4
0 7 -1 0
0 2 0 1
0 9 -1 0
0 5 0 2
1
end_operator
begin_operator
put__block01__slot1 
0
4
0 7 -1 0
0 0 0 1
0 9 -1 0
0 5 0 3
1
end_operator
begin_operator
put__block01__slot2 
0
4
0 7 -1 0
0 1 0 1
0 9 -1 0
0 5 0 4
1
end_operator
begin_operator
put__block01__slot3 
0
4
0 7 -1 0
0 4 0 1
0 9 -1 0
0 5 0 5
1
end_operator
begin_operator
put__block02__block01 
0
4
0 7 0 1
0 8 -1 0
0 9 -1 0
0 6 0 1
1
end_operator
begin_operator
put__block02__block03 
0
4
0 8 -1 0
0 2 0 1
0 9 -1 0
0 6 0 2
1
end_operator
begin_operator
put__block02__slot1 
0
4
0 8 -1 0
0 0 0 1
0 9 -1 0
0 6 0 3
1
end_operator
begin_operator
put__block02__slot2 
0
4
0 8 -1 0
0 1 0 1
0 9 -1 0
0 6 0 4
1
end_operator
begin_operator
put__block02__slot3 
0
4
0 8 -1 0
0 4 0 1
0 9 -1 0
0 6 0 5
1
end_operator
begin_operator
put__block03__block01 
0
4
0 7 0 1
0 2 -1 0
0 9 -1 0
0 3 0 1
1
end_operator
begin_operator
put__block03__block02 
0
4
0 8 0 1
0 2 -1 0
0 9 -1 0
0 3 0 2
1
end_operator
begin_operator
put__block03__slot1 
0
4
0 2 -1 0
0 0 0 1
0 9 -1 0
0 3 0 3
1
end_operator
begin_operator
put__block03__slot2 
0
4
0 2 -1 0
0 1 0 1
0 9 -1 0
0 3 0 4
1
end_operator
begin_operator
put__block03__slot3 
0
4
0 2 -1 0
0 4 0 1
0 9 -1 0
0 3 0 5
1
end_operator
0
