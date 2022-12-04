complete_overlap_accumulator = 0
any_overlap_accumulator = 0

def calc_complete_overlap(e1, e2):
    if int(e1[0]) >= int(e2[0]):
        if int(e1[1]) <= int(e2[1]):
            return True
    return False


def calc_any_overlap(e1, e2):
    if int(e2[0]) <= int(e1[0]) <= int(e2[1]):
        return True
    if int(e2[0]) <= int(e1[1]) <= int(e2[1]):
        return True
    return False


with open('day4_input.txt', 'r') as file:
    for line in file:
        elf_pair = line.split(',')
        elf1 = elf_pair[0].split('-')
        elf2 = elf_pair[1].split('-')
        e1to2 = calc_complete_overlap(elf1, elf2)
        if e1to2:
            complete_overlap_accumulator += 1
        else:
            e2to1 = calc_complete_overlap(elf2, elf1)
            if e2to1:
                complete_overlap_accumulator += 1

        e1to2 = calc_any_overlap(elf1, elf2)
        if e1to2:
            any_overlap_accumulator += 1
        else:
            e2to1 = calc_any_overlap(elf2, elf1)
            if e2to1:
                any_overlap_accumulator += 1

print(f'The total number of complete overlap is {complete_overlap_accumulator}.')
print(f'The total number of any overlap is {any_overlap_accumulator}.')