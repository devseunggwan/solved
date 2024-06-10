def banding(bandage, time):
    t, x, y = bandage
    
    if not time:
        return 0
        
    return (y * (time // t)) + (x * time)

def solution(bandage, health, attacks):
    max_health = health
    is_bending = 0
    
    for i in range(len(attacks)):
        time, dmg = attacks[i]
        
        if i > 0:
            health += banding(bandage, time - attacks[i-1][0] - 1)
            health = max_health if health > max_health else health
            
        health -= dmg

        if health <= 0:
            return -1
        
    return health