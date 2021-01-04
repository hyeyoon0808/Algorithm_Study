height = []
fake = []
for i in range(9):
    n = int(input())
    height.append(n)
for i in range(9):
    for j in range(9):
        if i != j:
            if height[i] + height[j] == sum(height)-100:
                fake.append(height[i])
                fake.append(height[j])
fake = list(set(fake))
height.remove(fake[0])
height.remove(fake[1])
height.sort()
print(height)
