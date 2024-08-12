st = {1, 2, 3, 4, 1, 2, 3, 4}
print(st)
st.add(6)
st.discard(20)
print(st)



st1 = {1, 2, 3, 4, 5, 6}
st2 = {1, 3, 4, 7, 9, 0}
st3 = st1.union(st2)
print(st3)
st4 = st1.intersection(st2)
print(st4)
print(st1)
st1.intersection_update(st2)
print(st1)
print(st1.issubset(st2))


