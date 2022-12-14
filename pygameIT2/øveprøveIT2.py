
n = 5
k = 0
navn = ["Robert","Boris","Brad","George","David"]
while k < n-2:
    a = navn[k]
    navn[k] = navn[n-k-1]
    navn[n-k-1]=a
    k+=1
print(navn)
