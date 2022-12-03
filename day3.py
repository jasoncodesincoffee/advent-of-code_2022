from string import ascii_lowercase as alc, ascii_uppercase as auc

priority = []
for i in alc:
    priority.append(i)
for i in auc:
    priority.append(i)

priority_accumulator = 0
group_accumulator = 0
groups_of_3s = []
counter = 0
with open('day3_input.txt', 'r') as file:
    for line in file:
        ruck1 = line[slice(0, len(line)//2)]
        ruck2 = line[slice(len(line)//2, len(line))]
        for character in ruck2:
            idx_found = ruck1.find(character)
            if idx_found != -1:
                priority_idx = priority.index(ruck1[idx_found])
                priority_accumulator += priority_idx + 1
                break
        groups_of_3s.append(line)
        counter += 1
        if counter % 3 == 0:
            for x in groups_of_3s[0]:
                xIdx = groups_of_3s[1].find(x)
                if xIdx != -1:
                    yIdx = groups_of_3s[2].find(x)
                    if yIdx != -1:
                        group_idx = priority.index(groups_of_3s[2][yIdx])
                        group_accumulator += group_idx + 1
                        groups_of_3s = []
                        break

print(f'The sum of the priority is {priority_accumulator}.')
print(f'The sum of the group priority is {group_accumulator}.')