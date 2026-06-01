def spawn_wave(enemy_type, base_hp, *coords):
    ans = []
    for pos in coords:
        ans.append({"type": enemy_type, "hp": base_hp, "pos": pos})
    return ans
print(spawn_wave("Skeleton", 150, (10, 20), (50, 60), (100, 15)))