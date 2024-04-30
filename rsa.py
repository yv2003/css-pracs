import math

# d = (k * totiont(n) + 1) / e where k is any variable such that d is an integer
# to find whether d is an integer, mod it with 1
def find_d(e, t) -> int:
    k = 1
    while True:
        temp = (k * t + 1) / e
        # print(temp)
        if temp % 1 == 0:
            return temp
        k += 1


def find_e(t) -> int:
    for i in range(2, t):
        if math.gcd(i, t) == 1:
            return i
    return t

p = int(input("Enter p : "))
q = int(input("Enter q : "))
m = int(input("Enter message m : "))

n = p * q

totiont = (p-1) * (q-1)

print("totiont :", totiont)

e = find_e(totiont)

print("e :", e)

d = find_d(e, totiont)

print("d :", d)

# (m ** e) % n
encrypted_msg = (m**e) % n
print("encrypted_msg :", encrypted_msg)

decryped_message = (encrypted_msg**d) % n
print("decryped_message :", decryped_message)
