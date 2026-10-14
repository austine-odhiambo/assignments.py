def and_gate(A, B):
    return A and B

def or_gate(A, B):
    return A or B

def not_gate(A):
    return not A

def nand_gate(A, B):
    return not(A and B)

def nor_gate(A, B):
    return not(A or B)

def xor_gate(A,B):
    return A !=B

def xnor_gate(A, B):
    return A == B

print("=" * 60)
print("              THE 7 LOGIC GATES TRUTH TABLES         ")
print("-"  *  60)

print("\n[ 1. NOT GATE ]")
print("A      | Output")
print("-" * 15)
for A in [ 0,  1]:
    print(f"{str(A):<5}  |  {int(not_gate(A))}")

gates_to_test = [
    ("AND",and_gate),
    ("OR",or_gate),
    ("NAND",nand_gate),
    ("NOR",nor_gate),
    ("XOR",xor_gate),
    ("XNOR",xnor_gate)
]  

for name,gate_function in gates_to_test:
    print(f"\n[ {name} GATE ]")
    print("A     |   B   | Output")
    print("-" * 22)
    for A in [ 0,  1]:
        for B in [ 0,  1]:
            result = gate_function(0, 1) if (A, B) == (0, 1) else gate_function(A, B)
            print(f"{str(A):<5} | {str(B):<5} | {int(result)}")


