# methond to convert time
def convert_string_into_seconds(element):
    acc = 0
    hours = int(element[0:2])
    if hours != "00":
        acc = hours * 60
    acc += (int(element[3:5]) * 60)
    acc += int(element[6:8])
    return acc


# methond to return average time in seconds
def calculate_average_duration_in_seconds():
    with open("files/input_file.txt") as read_file:
        lines = read_file.readlines()
    total_seconds = 0
    for line in lines:
        seconds = convert_string_into_seconds(line)
        total_seconds += seconds
    return total_seconds / len(lines)


# convert seconds into hh:mm:ss format abd return result
def convert_into_output_string():
    seconds = calculate_average_duration_in_seconds()
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


print(convert_into_output_string())
