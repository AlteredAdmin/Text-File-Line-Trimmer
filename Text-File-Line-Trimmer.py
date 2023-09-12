def format_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if len(line) > 120:
            words = line.split()
            line = ""
            for word in words:
                if len(line) + len(word) <= 120:
                    line += word + " "
                else:
                    formatted_lines.append(line)
                    line = word + " "
            formatted_lines.append(line)
        else:
            formatted_lines.append(line)
    with open(filename, "w") as file:
        file.write("\n".join(formatted_lines))

format_file("textfile.txt")
