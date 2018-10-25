#RPG.rb

#All of the following are out of 10
#Monster Chances
$monsterChance = 4
$specialMonsterChance = 3

#NPC Chances
$npcChance = 3

#Item Chances
$commonChance = 8
$rareChance = 4
$spookyChance = 2
$owoChance = 0

$lvl = 0

$mhp = 0
$mmhp = Array[50, 50, 75, 75, 100, 125, 150, 175, 200]
$mmd = Array[25, 25, 50, 50, 75, 100, 125, 150, 175]
$hp = 75
$levelstats = Array[
  [0, 75, 25 ],
  [1, 75, 50 ],
  [2, 100,50 ],
  [3, 100,75 ],
  [4, 125,75 ]
]

class Player
  def initialize(inv, equipped, questing, quest, x, y)
    @inv = inv
    @equipped = equipped
    @questing = questing
    @quest = quest
    @x = x
    @y = y
  end

  def printStats
    puts "Main Equipped:        #{@equipped[0]}"
    puts "Secondary Equipped:   #{@equipped[1]}"
    puts ""
    if @questing != 0
      puts "Current Quest:        #{@quest[0]}"
      if @quest[1] != 0
        puts "Item Needed:          #{@quest[1]}"
      end
    end
  end

class Item
  def initialize(name, type, rarity)
    @name = name
    @type = type
    @rarity = rarity
  end

  def printItemName
    puts @name
  end

  def printItem
    puts @name
    puts @type
    puts @rarity
  end
end

  def printInv
    puts @inv
  end
end

def bigboi
  for i in 0..50
    puts ""
  end
end

inv = Array[]
equipped = Array["",""]
quest = Array["",""]

$player = Player.new(inv, equipped, 0, quest, 0, 0)

def fight(specialBoi)
  $mhp = rand($mmhp[$lvl] + 1)
  for i in 0..$levelstats.length-1
    if $levelstats[i][0] == $lvl
      $mphp = $levelstats[i][1]
      $mpd = $levelstats[i][2]
    end
  end

  def printFight
    puts "MONSTER:"
    puts "HP:         #{$mhp}"
    puts "Max HP:     #{$mmhp[$lvl]}"
    puts "Max Damage: #{$mmd[$lvl]}"
    puts ""
    puts "YOU:"
    puts "HP:         #{$hp}"
    puts "Max HP:     #{$mphp}"
    puts "Max Damage: #{$mpd}"
    puts ""
  end

  if specialBoi == 1
    puts "This monster will give you a quest item!"
    puts ""
  end

  def battle(msg)
    puts msg
    inp = gets.chomp
    mpd = $mpd
    mmd = $mmd[$lvl]

    if inp == "attack"
      pd = rand(mpd + 1)
      $mhp -= pd
      if $mhp <= 0
        bigboi
        puts "You won!"
        main
      end
      md = rand(mmd + 1)
      $hp -= md
      if $hp <= 0
        bigboi
        puts "You died!"
      else
        bigboi
        printFight
        battle("You attacked the monster for #{pd} damage. It hit back for #{md}.")
      end

    else if inp == "Use Item"
      bigboi
      player.printInv
      puts "Which item would you like to select?"
      item = gets.chomp
    end
  end

  printFight
  battle("You are in a battle! What would you like to do? (Attack, Escape, Use Item)")
end

def main
  puts ""
  puts "What would you like to do?"
  doin = gets.chomp

  if doin == "help"
    bigboi
    puts "Command: move, stats, inv"
    main
  end

  if doin == "stats"
    bigboi
    $player.printStats
    main
  end

  if doin == "move"
    chance1 = rand(11)
    if chance1 <= $monsterChance
      chance2 = rand(11)
      if chance2 <= $specialMonsterChance
        specialBoi = 1
      else
        specialBoi = 0
      end
      bigboi
      fight(specialBoi)
    else
      bigboi
      main
    end

  else
    bigboi
    puts "Thats not a command."
    main
  end

  if doin == "jok big homo"
    bigboi
    puts "Yeah pretty much"
  end
end

bigboi
main
