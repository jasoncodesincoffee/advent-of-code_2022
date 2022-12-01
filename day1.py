input = open('day1_input.txt', 'r')
lines = input.readlines()

elf_list = []
total_calories = 0
total_top_calorie_elves = 0

for line in lines:
    calories = line.rstrip("\n")
    if calories == '':
        elf_list.append(total_calories)
        total_calories = 0
    else:
        total_calories += int(calories)

for i in range(3):
    idx_max = max(range(len(elf_list)), key=elf_list.__getitem__)
    max_calorie = max(elf_list)
    print(f'The max calories carried by an elf is {max_calorie} by elf #{idx_max+1}.')

    total_top_calorie_elves += max_calorie
    del elf_list[idx_max]

print(f'The total calories of the top 3 elves is {total_top_calorie_elves}.')