import random
passes = []
values = []

for i in range(5000):
    passint = random.randint(1,8000)
    while passint in passes:
        passint = random.randint(1,8000)
    passes.append(str(passint))
    values.append(str(random.randint(1,100)))
with open("test.csv","w") as file:
    file.write(",".join(passes))
    file.write("\n")
    file.write(",".join(values))
