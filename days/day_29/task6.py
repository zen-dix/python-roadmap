def write_config(filepath, header, *lines):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"=== {header} ===\n")
            for line in lines:
                file.write(f"{line}\n")
    except FileExistsError:
        print("The file path does not exist")
write_config("settings.conf", "Window Rules", "windowrule = float, ^(kitty)$", "windowrule = center, ^(kitty)$")