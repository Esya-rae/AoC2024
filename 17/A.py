def combo_operand(operand):
    global A, B, C
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C


def adv(operand):
    global A, B, C
    val = combo_operand(operand)
    div = 2 ** val
    A = A // div


def bxl(operand):
    global A, B, C
    B = B ^ operand


def bst(operand):
    global A, B, C
    val = combo_operand(operand)
    val %= 8
    B = val


def bxc(operand):
    global A, B, C
    B = B ^ C


def out(operand):
    global A, B, C, new_program
    val = combo_operand(operand) % 8
    new_program.append(val)


def bdv(operand):
    global A, B, C
    val = combo_operand(operand)
    div = 2 ** val
    B = A // div


def cdv(operand):
    global A, B, C
    val = combo_operand(operand)
    div = 2 ** val
    C = A // div




f = open('input.txt', 'r')
lines = f.read().splitlines()

A = int(lines[0].strip().split()[-1])
B = int(lines[1].strip().split()[-1])
C = int(lines[2].strip().split()[-1])
program = list(map(int, lines[4].strip().split()[-1].split(',')))
new_program = []
print(A, B, C)
print(program)
print(len(program))

for A in range(8 ** 16, 8**17):
    B = 0
    C = 0
    new_program = []
    i = 0
    flag = True
    while i < len(program) - 1 and len(new_program) < len(program):
        if program[i] == 3:
            if A != 0:
                i = program[i + 1]
            else:
                i += 2
        else:
            if program[i] == 0:
                adv(program[i + 1])
            elif program[i] == 1:
                bxl(program[i + 1])
            elif program[i] == 2:
                bst(program[i + 1])
            elif program[i] == 4:
                bxc(program[i + 1])
            elif program[i] == 5:
                out(program[i + 1])
            elif program[i] == 6:
                bdv(program[i + 1])
            elif program[i] == 7:
                cdv(program[i + 1])
            i += 2
        if len(new_program) > 0 and new_program[-1] != program[len(new_program) - 1]:
            flag = False
            break
    assert not flag or len(new_program) == len(program)

    if flag:
        print(A, new_program)
        break
print()
print(A, B, C)