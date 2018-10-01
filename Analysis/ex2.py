# Truth table loop

for p in[True, False]:
    print(p, not(p))

print("\n")


for p in [True, False]:
    for q in[True, False]:
        print(p, q,(p and q))

print("\n")

for p in [True, False]:
    for q in[True, False]:
        print(p, q,(p or q))

print("\n")
for p in [True, False]:
    for q in[True, False]:
        print(p, q, not(p and not(q) or (not p and q)))

print("\n")
for p in [True, False]:
    for q in[True, False]:
        print(p, q, not(p and not(q) or (not(p) and q)))


print("\n")
for p in [True, False]:
    for q in[True, False]:
        print(p, q, not(p and not(q) or (not p and q)))

print("\n")

for p in [True, False]:
    for q in[True, False]:
        for r in[True, False]:
            print(p, q, r, not(p or q or r))

print("\n")

for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            print(p, q, r, (not(p) and not(q) and not(r)))

print("\n")


if ((not(p) and not(q) and not(r)) == (not(p or q or r))):
    print("this is equal")
else:
    print("this is false")

print("\n" + "\n")

for p in [True, False]:
    for q in [True, False]:
        print(p, q,not(not(p) or q))

print("\n")

for p in [True, False]:
    for q in [True, False]:
        print(p, q,(not(p) or not(q)))

print("\n" + "\n")

P = False
q = False
r = False


print("\n" + "\n")