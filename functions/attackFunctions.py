
def attackMovement(attackList, attackRect):
    if attackList:
        for attackRect in attackList:
            attackRect.x -= 5

            screen.blit(bullet, attackRect)

        attackList = [attack for attack in attackList if attack.x > -100]
        return attackList
    else:
        return []

