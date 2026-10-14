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


def half_adder(A, B):
    sum_bit =xor_gate(A, B)
    carry_bit =and_gate(A, B)

    return sum_bit,carry_bit
print("\n" + "=" *80)
print("                        BINARY HALF ADDER TRUTH TABLE               ")
print("=" * 80)
print("Input A  |  Input B       |        Sum (XOR)        |      Carry (AND)")
print("-" * 60)

for A in [True, False]:
    for B in [True, False]:
        for s, c in [half_adder(A, B)]:

            binary_B =1 if B else 0
            binary_A =1 if A else 0
            binary_S =1 if s else 0
            binary_C =1 if c else 0

            print(f"   {binary_A}     |        {binary_B}         |        {binary_C}         |          {binary_S}")