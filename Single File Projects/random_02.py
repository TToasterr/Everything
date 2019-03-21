from countries import USA, Japan

while True:
        if Japan.isAtWar(USA):
                Japan.supriseAttack(USA.pearlHarbor)
                USA.fightBack(USA.atomicBomb, Japan.Hiroshima)

                if Japan.isAtWar(USA):
                        USA.fightBack(USA.atomicBomb, Japan.Nagasaki)

                Japan.isAtWar(USA) = False
                Japan.return(Japan.anime)
                USA.return(USA.weebs)
