# Remove duplicates and sort after adding new DNS servers
import shutil

shutil.copyfile("providers.txt", "providers.txt.bak")

lines = []
with open("providers.txt") as f:
    lines = f.readlines()
    # Remove empty lines
    lines = [line for line in lines if line.strip()]
    # Remove duplicates
    # lines = list(set(lines))

split_lines = [line for line in lines if line.startswith("#")]
sections = []
current_section = set()
new_lines = list()

if len(split_lines) < 1:
    new_lines = lines
else:
    for line in lines:
        if not line.startswith("#"):
            current_section.update([line])
        else:
            if sections:
                new_lines.append(sections)
            current_section_list = list(current_section)
            current_section_list.sort()
            new_lines.extend(current_section)
            sections = line
            current_section = set()

    # push the last section
    new_lines.append(sections)
    current_section_list = list(current_section)
    current_section_list.sort()
    new_lines.extend(current_section)


for i in range(len(new_lines)):
    if new_lines[i].startswith("#"):
        new_lines[i] = "\n" + new_lines[i] + "\n"

result = "".join(new_lines)


with open("providers.txt", "w") as f:
    f.writelines(new_lines)
