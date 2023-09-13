import os

with os.scandir('D:\Recordings') as entries:
    for entry in entries:
        old_name = entry.path

        curr_path = entry.path.split('\\')
        folder = f"{curr_path[0]}\\{curr_path[1]}\\"

        name_list = entry.name.split('_')
        new_name = f"{name_list[0]}_{name_list[2]}_{name_list[1]}_{name_list[3]}"

        os.rename(entry.path, folder+new_name)

