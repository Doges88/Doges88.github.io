import sys
import os
import time


def editor(file):
    try:
        lines = open(file, 'r').read().split("\n")
    except FileNotFoundError:
        with open(file, 'w+') as file:
            file.write("")
            lines = file.read().split("\n")
            file.close()
    line_amount = 0
    line_index = 0
    new_lines = [line+"\n" for line in lines]
    for line in lines:
        line_index+=1
        line_amount+=1
        if line_index < 10:
            print(f"{line_index}   | {line}")
        elif line_index < 100 and line_index > 9:
            print(f"{line_index}  | {line}")
        elif line_index < 1000 and line_index > 99:
            print(f"{line_index} | {line}")
        elif line_index < 10000 and line_index > 999:
            print(f"{line_index}| {line}")
    line_index+=1
    while True:
        
        if line_index < 10:
            new_line = input(f"{line_index}   |")
        elif line_index < 100 and line_index > 9:
            new_line = input(f"{line_index}  |")
        elif line_index < 1000 and line_index > 99:
            new_line = input(f"{line_index} |")
        elif line_index < 10000 and line_index > 999:
            new_line = input(f"{line_index}|")
        if new_line == ":exit":
            sys.exit()
        elif new_line.startswith(":save "):
            save_file = new_line.removeprefix(":save ")
            with open(save_file, "w") as file:
                file.write("".join(new_lines))
                file.close()
                print(f"File saved as {save_file}")
                time.sleep(1)
            line_index=0
            os.system("cls")
            for line in new_lines:
                line_index+=1
                line_amount+=1
                line = line.strip("\n")
                if line_index < 10:
                    print(f"{line_index}   | {line}")
                elif line_index < 100 and line_index > 9:
                    print(f"{line_index}  | {line}")
                elif line_index < 1000 and line_index > 99:
                    print(f"{line_index} | {line}")
                elif line_index < 10000 and line_index > 999:
                    print(f"{line_index}| {line}")
            line_index+=1
            
        elif new_line.startswith(":edit "):
            try:
                args = new_line.removeprefix(":edit ").split("||")
            except:
                print("Wrong syntax")
            # :edit 1||print("Lol")
            # 77
            try:
                index = int(args[0])
                content = args[1]
                new_lines.pop(index-1)
                new_lines.insert(index-1, content+"\n")
                line_index = 0
                line_amount = 0
                os.system("cls")
                for line in new_lines:
                    line_index+=1
                    line_amount+=1
                    line = line.strip("\n")
                    if line_index < 10:
                        print(f"{line_index}   | {line}")
                    elif line_index < 100 and line_index > 9:
                        print(f"{line_index}  | {line}")
                    elif line_index < 1000 and line_index > 99:
                        print(f"{line_index} | {line}")
                    elif line_index < 10000 and line_index > 999:
                        print(f"{line_index}| {line}")
                line_index+=1
            except:
                print("Wrong arguments were supplied")
        elif new_line.startswith(":del "):
            line_number = new_line.removeprefix(":del ")
            try:               
                new_lines.pop(int(line_number)-1)
                os.system("cls")
                line_index=0
                for line in new_lines:
                    line_index+=1
                    line_amount+=1
                    line = line.strip("\n")
                    if line_index < 10:
                        print(f"{line_index}   | {line}")
                    elif line_index < 100 and line_index > 9:
                        print(f"{line_index}  | {line}")
                    elif line_index < 1000 and line_index > 99:
                        print(f"{line_index} | {line}")
                    elif line_index < 10000 and line_index > 999:
                        print(f"{line_index}| {line}")
                line_index+=1
            except:
                print("Wrong arguments were supplied")
        elif new_line == ":delall":
            line_index=0
            new_lines = [""]
            os.system("cls")
            for line in new_lines:
                line_index+=1
                line_amount+=1
                line = line.strip("\n")
                if line_index < 10:
                    print(f"{line_index}   | {line}")
                elif line_index < 100 and line_index > 9:
                    print(f"{line_index}  | {line}")
                elif line_index < 1000 and line_index > 99:
                    print(f"{line_index} | {line}")
                elif line_index < 10000 and line_index > 999:
                    print(f"{line_index}| {line}")
            line_index+=1
        elif new_line.startswith(":delmul "):
            number_of_lines = int(new_line.removeprefix(":delmul "))
            print(line_index)
            
            for index in range(1,number_of_lines+1):
                print(index)
                new_lines.pop(line_index-1-index)
            line_index=0
            os.system("cls")
            for line in new_lines:
                line_index+=1
                line_amount+=1
                line = line.strip("\n")
                if line_index < 10:
                    print(f"{line_index}   | {line}")
                elif line_index < 100 and line_index > 9:
                    print(f"{line_index}  | {line}")
                elif line_index < 1000 and line_index > 99:
                    print(f"{line_index} | {line}")
                elif line_index < 10000 and line_index > 999:
                    print(f"{line_index}| {line}")
            line_index+=1
                

        else:
            new_lines.append(str(new_line)+"\n")
            line_index+=1


editor(sys.argv[1])