def implication(p, q):
    return not p or q
print("p q a")
for p in [True, False]:
    for q in[True, False]:
        a = implication(p, q)
        print(p, q, a)
