import ex1
import ex2
import ex3
import ex4
import ex5


print("="*30)
print("exercise 1")
print("="*30)
a = ["2", "2", "2", "2", "2", "2"]
b = ["4", "22", "25", "22", "0", "22"]
op = ["-", "+", "*", "/", "/", "0"]
for i in range(len(op)):
    ex1.terminal_algo(a[i], op[i], b[i])

print("="*30)
print("exercise 2")
print("="*30)
nums = ["0", "2344", "u", "2555.3", "-2555"]
for i in nums:
    ex2.ex2(i)

print("="*30)
print("exercise 3")
print("="*30)
nums = ["0", "-2344", "5443.3", "-2555.3", "2535", "2535.0", "2535"]
print(f"{'input':10} : {'output':10}")
for i in nums:
    result = ex3.ex3(i)
    print(f"{i:10} : {result}")


print("="*30)
print("exercise 4")
print("="*30)
nums = [3, 7, 10, 20]
print(f"{'seq':>20} : {'sum':>20}")
for i in nums:
    result = ex4.ex4(1, i, 0)
    print(f"\nsum of {i} sequence elements is: {result}")

print("="*30)
print("exercise 5")
print("="*30)
result = ex5.ex5(32, 127)
print(result)




