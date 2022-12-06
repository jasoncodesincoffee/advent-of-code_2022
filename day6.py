input = open('day6_input.txt', 'r')
line = input.readline()
packet_marker_length = 4
message_marker_length = 14

def code_breaker(string, marker_length):
    for i in range(len(string)):
        marker = string[i:i + marker_length]
        marker_list = []
        marker_list[:0] = marker
        dupe_search = set(marker_list)
        if len(dupe_search) == marker_length:
            print(f'The number of characters that need to be processed is {i + marker_length}.')
            break


code_breaker(line, packet_marker_length)
code_breaker(line, message_marker_length)