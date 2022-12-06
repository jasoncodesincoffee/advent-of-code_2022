input = open('day6_input.txt', 'r')
line = input.readline()
packet_marker_length = 4
message_marker_length = 14

for i in range(len(line)):
    marker = line[i:i+packet_marker_length]
    marker_list = []
    marker_list[:0] = marker
    dupe_search = set(marker_list)
    if len(dupe_search) == packet_marker_length:
        print(f'The number of characters that need to be processed is {i+packet_marker_length}.')
        break

############################################

for i in range(len(line)):
    marker = line[i:i+message_marker_length]
    marker_list = []
    marker_list[:0] = marker
    dupe_search = set(marker_list)
    if len(dupe_search) == message_marker_length:
        print(f'The number of characters that need to be processed is {i+message_marker_length}.')
        break