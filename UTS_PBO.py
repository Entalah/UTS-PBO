#no 1
job = "Ujian Tengah Semester pbo"

#1
for a in job:
    print(a, end="")
print("\n")

#2 
#3
#4
for a in job:
    if a == "a":
        print("a", end="")
    if a == "e":
        print("e", end="") 

print("\n")
#no 2

for i in range(6):
    for j in range(6, i - 1, -1):
        print(j, end=" ")
    for k in range(i):
        print("*", end=" ")
    print()