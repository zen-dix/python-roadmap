def build_path(base, *folders):
    ans = base
    for f in folders:
        ans+="/"+f
    return ans
print(build_path("~/.config","hypr", "hyprland.conf"))