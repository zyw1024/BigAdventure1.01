import pygame
import numpy
# from numpy.random import randint as rand
import random
import maze as mz


class Settings:
    """A class to store all settings for BigAdventure"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        # #Horizontal screen
        # self.screen_width = 1280
        # self.screen_height = 600

        #Vertical screen
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (54, 38, 32)
        self.img_change_interval = 10

        #BGM
        # self.bgm_level1 = pygame.mixer.Sound("materials/sounds/00000004B465 66号公路 主题进攻.ogg")
        # self.bgm_level2 = pygame.mixer.Sound("materials/sounds/00000004B36C 多拉多主题.ogg")
        # self.bgm_level3 = pygame.mixer.Sound("materials/sounds/000000040984 沃斯卡亚工业区主题.ogg")
        # self.bgm_level4 = pygame.mixer.Sound("materials/sounds/000000043135 谜之音乐.ogg")
        self.bgm = []
        self.bgm.append("materials/sounds/bgm/花村游戏机音乐1.ogg")
        self.bgm.append("materials/sounds/bgm/花村游戏机音乐2.ogg")
        self.bgm.append( "materials/sounds/bgm/花村游戏机音乐3.ogg")
        self.bgm.append("materials/sounds/bgm/万圣节音乐.ogg")

        #Victory sound effect
        self.victory_sound = pygame.mixer.Sound("materials/sounds/victory/000000060214 夏季运动会进球.ogg")

        #Defeat sound effect
        self.defeat_sound = []
        self.defeat_sound.append(pygame.mixer.Sound("materials/sounds/defeat/000000040961 运载目标抵达检查点（防守方）.ogg"))

        #Treassures sound effect
        self.ruby_sound = pygame.mixer.Sound("materials/sounds/other sound effect/复古游戏捡到东西.ogg")
        self.sapphire_sound = pygame.mixer.Sound("materials/sounds/other sound effect/复古游戏捡到东西2.ogg")
        self.some_coins_sound = pygame.mixer.Sound("materials/sounds/other sound effect/单一硬币声.ogg")
        self.lots_of_coins_sound = pygame.mixer.Sound("materials/sounds/other sound effect/小袋金币声.ogg")
        self.massive_coins_sound = pygame.mixer.Sound("materials/sounds/other sound effect/大量金币声.ogg")

        #Bullets sound effect
        self.player_normal_attack_sound = pygame.mixer.Sound("materials/sounds/bullet_sounds/清脆枪声7.ogg")
        # self.player_coin_attack_sound = pygame.mixer.Sound("materials/sounds/other sound effect/收银声.ogg")
        self.player_coin_attack_sound = pygame.mixer.Sound("materials/sounds/other sound effect/高抛硬币.ogg")
        self.player_skull_attack_sound = pygame.mixer.Sound("materials/sounds/other sound effect/阴笑声.ogg")

        #NPC sound effect
        self.fortune_cat_sound = pygame.mixer.Sound("materials/sounds/other sound effect/猫叫.wav")
        # self.Death_sound = pygame.mixer.Sound("materials/sounds/other sound effect/0000000606AA 阴笑（深沉）.ogg")
        self.Death_sound = pygame.mixer.Sound("materials/sounds/other sound effect/阴笑声.ogg")
        self.deal_done_sound = pygame.mixer.Sound("materials/sounds/other sound effect/收银声.ogg")
        self.welcome_sound_normal = pygame.mixer.Sound("materials/sounds/other sound effect/女孩说欢迎光临.wav")
        self.welcome_sound_happy = pygame.mixer.Sound("materials/sounds/other sound effect/俏皮的欢迎光临.wav")

        #Rank settings
        self.skeleton_soldier_rank = 1
        self.unicorn_rank = 2
        self.blue_dragon_rank = 3
        self.black_dragon_rank = 4

        # Health settings
        self.player_health = 2000
        self.skeleton_soldier_health = 400
        self.unicorn_health = 500
        self.blue_dragon_health = 800
        self.black_dragon_health = 1600

        #Energy settings
        self.player_energy = 50
        self.mission_complete_energy_bonus = 15

        #Speed settings
        #player and monster's speed
        self.player_speed_factor = 1.8
        # self.skeleton_soldier_speed_factor = 2.0
        self.skeleton_soldier_speed_factor = 1.6
        self.unicorn_speed_factor = 1.5
        self.blue_dragon_speed_factor = 1.4
        self.black_dragon_speed_factor = 1.3
        #Bullet's speed
        self.bluebullet_speed_factor = 6
        self.fireball_speed_factor = 5
        self.lightning_ball_speed_factor = 4.5
        self.black_fireball_speed_factor = 4
        self.ground_needle_speed_factor = 4
        self.redbullet_speed_factor = 6
        self.coin_bullet_speed_factor = 4
        self.skull_bullet_speed_factor = 4

        #Probe's speed
        self.probe_speed_factor = 30

        #Attack preparing basic time(ATKPRBT).
        # The monster will attack base on ATKPRT which is generated from this stantard and some random factor
        self.skeleton_soldier_ATKPRBT = 3
        self.unicorn_ATKPRBT = 10
        self.blue_dragon_ATKPRBT = 15
        self.black_dragon_ATKPRBT = 10

        self.player_shoot_interval = 10

        #Using format "tick % ATKPRT < lower_threshold" to control attack interval
        self.lower_threshold = 0.2

        self.discover_prt = 30


        #ATK
        self.player_atk = 130
        self.skeleton_soldier_atk = 70
        self.unicorn_atk = 110
        self.blue_dragon_atk = 160
        self.black_dragon_atk = 300

        #Bullet damage multiple
        self.skull_bullet_multiple = 3
        self.coin_bullet_multiple = 1.5

        #Attack consumption
        self.player_normal_attack_consumption = 1

        #Player skill lock
        self.is_coin_attack_valid = False
        self.is_skull_attack_valid = False

        #rest time
        self.rest_time = 100

        #Treasures' abilities
        self.ruby_raw_health_supply = 100
        self.ruby_round_health_supply = 200
        self.ruby_dragon_health_supply = 350
        self.sapphire_raw_energy_supply = 30
        self.sapphire_round_energy_supply = 50
        self.sapphire_dragon_energy_supply = 100


        #Coins number in coins stacks
        self.some_coins_num = 26
        self.lots_of_coins_num = 46
        self.massive_coins_num = 66

        #Goods
        self.HP_50coins = 250
        self.HP_100coins = 550
        self.MP_50coins = 150
        self.MP_100coins = 330

        # Maze Settings
        # self.maze_width = 5
        # self.maze_height = 5
        self.maze_width = 3
        self.maze_height = 3
        self.orig_wall_stone = {}
        self.orig_road_stone = {}
        self.orig_wall_stone.update({1: pygame.image.load("materials/images/backgrounds/ice/ice_wall1.png")})
        self.orig_wall_stone.update({3: pygame.image.load("materials/images/backgrounds/ice/ice_wall2.png")})
        self.orig_wall_stone.update({17: pygame.image.load("materials/images/backgrounds/ice/ice_wall2.png")})
        self.orig_road_stone.update({1: pygame.image.load("materials/images/backgrounds/ice/ice_road1.png")})
        self.orig_road_stone.update({2: pygame.image.load("materials/images/backgrounds/ice/ice_road2.png")})
        self.orig_road_stone.update({3: pygame.image.load("materials/images/backgrounds/ice/ice_road3.png")})
        self.orig_road_stone.update({5: pygame.image.load("materials/images/backgrounds/ice/ice_road4.png")})

        #Player's original image
        self.orig_player_left = {}
        self.orig_player_left.update({0: pygame.image.load('materials/images/roles/bear_left/bear_left0.png')})
        self.orig_player_left.update({1: pygame.image.load('materials/images/roles/bear_left/bear_left1.png')})
        self.orig_player_left.update({2: pygame.image.load('materials/images/roles/bear_left/bear_left2.png')})
        self.orig_player_left.update({3: pygame.image.load('materials/images/roles/bear_left/bear_left3.png')})
        self.orig_player_left.update({4: pygame.image.load('materials/images/roles/bear_left/bear_left4.png')})
        self.orig_player_left.update({5: pygame.image.load('materials/images/roles/bear_left/bear_left5.png')})
        self.orig_player_right = {}
        self.orig_player_right.update({0: pygame.image.load('materials/images/roles/bear_right/bear_right0.png')})
        self.orig_player_right.update({1: pygame.image.load('materials/images/roles/bear_right/bear_right1.png')})
        self.orig_player_right.update({2: pygame.image.load('materials/images/roles/bear_right/bear_right2.png')})
        self.orig_player_right.update({3: pygame.image.load('materials/images/roles/bear_right/bear_right3.png')})
        self.orig_player_right.update({4: pygame.image.load('materials/images/roles/bear_right/bear_right4.png')})
        self.orig_player_right.update({5: pygame.image.load('materials/images/roles/bear_right/bear_right5.png')})
        self.player_index = 0
        self.orig_player_death = {}
        self.orig_player_death.update({0: pygame.image.load("materials/images/roles/bear_death/bear_death0.png")})
        self.orig_player_death.update({1: pygame.image.load("materials/images/roles/bear_death/bear_death1.png")})
        self.orig_player_death.update({2: pygame.image.load("materials/images/roles/bear_death/bear_death2.png")})
        self.orig_player_death.update({3: pygame.image.load("materials/images/roles/bear_death/bear_death3.png")})
        self.orig_player_death.update({4: pygame.image.load("materials/images/roles/bear_death/bear_death4.png")})
        self.orig_player_death.update({5: pygame.image.load("materials/images/roles/bear_death/bear_death5.png")})
        self.orig_player_death.update({6: pygame.image.load("materials/images/roles/bear_death/bear_death6.png")})
        self.orig_player_death.update({7: pygame.image.load("materials/images/roles/bear_death/bear_death7.png")})
        self.player_death_index = 0

        #Skeleton soldier's original image
        self.orig_skeleton_soldier_left = {}
        self.orig_skeleton_soldier_left.update({0: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_left0.png")})
        self.orig_skeleton_soldier_left.update({1: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_left1.png")})
        self.orig_skeleton_soldier_left.update({2: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_left2.png")})
        self.orig_skeleton_soldier_left.update({3: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_left3.png")})
        self.orig_skeleton_soldier_left.update({4: pygame.image.load("materials/images/monsters/skeleton_soldie_slash/skeleton_soldier_left_slash0.png")})
        self.orig_skeleton_soldier_left.update({5: pygame.image.load("materials/images/monsters/skeleton_soldie_slash/skeleton_soldier_left_slash1.png")})
        self.orig_skeleton_soldier_right = {}
        self.orig_skeleton_soldier_right.update({0: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_right0.png")})
        self.orig_skeleton_soldier_right.update({1: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_right1.png")})
        self.orig_skeleton_soldier_right.update({2: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_right2.png")})
        self.orig_skeleton_soldier_right.update({3: pygame.image.load("materials/images/monsters/skeleton_soldier/skeleton_soldier_right3.png")})
        self.orig_skeleton_soldier_right.update({4: pygame.image.load("materials/images/monsters/skeleton_soldie_slash/skeleton_soldier_right_slash0.png")})
        self.orig_skeleton_soldier_right.update({5: pygame.image.load("materials/images/monsters/skeleton_soldie_slash/skeleton_soldier_right_slash1.png")})
        self.skeleton_soldier_index = 0

        #Unicorn original image
        self.orig_unicorn_left = {}
        self.orig_unicorn_left.update({0: pygame.image.load("materials/images/monsters/unicorn/unicorn_left0.png")})
        self.orig_unicorn_left.update({1: pygame.image.load("materials/images/monsters/unicorn/unicorn_left1.png")})
        self.orig_unicorn_left.update({2: pygame.image.load("materials/images/monsters/unicorn/unicorn_left2.png")})
        self.orig_unicorn_left.update({3: pygame.image.load("materials/images/monsters/unicorn/unicorn_left3.png")})
        self.orig_unicorn_left.update({4: pygame.image.load("materials/images/monsters/unicorn/unicorn_left4.png")})
        self.orig_unicorn_right = {}
        self.orig_unicorn_right.update({0: pygame.image.load("materials/images/monsters/unicorn/unicorn_right0.png")})
        self.orig_unicorn_right.update({1: pygame.image.load("materials/images/monsters/unicorn/unicorn_right1.png")})
        self.orig_unicorn_right.update({2: pygame.image.load("materials/images/monsters/unicorn/unicorn_right2.png")})
        self.orig_unicorn_right.update({3: pygame.image.load("materials/images/monsters/unicorn/unicorn_right3.png")})
        self.orig_unicorn_right.update({4: pygame.image.load("materials/images/monsters/unicorn/unicorn_right4.png")})

        #Blue dragon original image
        self.orig_blue_dragon_left = {}
        self.orig_blue_dragon_left.update({0: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_left0.png")})
        self.orig_blue_dragon_left.update({1: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_left1.png")})
        self.orig_blue_dragon_left.update({2: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_left2.png")})
        self.orig_blue_dragon_left.update({3: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_left3.png")})
        self.orig_blue_dragon_left.update({4: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_left4.png")})
        self.orig_blue_dragon_left.update({5: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_left5.png")})
        self.orig_blue_dragon_right = {}
        self.orig_blue_dragon_right.update({0: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_right0.png")})
        self.orig_blue_dragon_right.update({1: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_right1.png")})
        self.orig_blue_dragon_right.update({2: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_right2.png")})
        self.orig_blue_dragon_right.update({3: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_right3.png")})
        self.orig_blue_dragon_right.update({4: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_right4.png")})
        self.orig_blue_dragon_right.update({5: pygame.image.load("materials/images/monsters/blue_dragon/blue_dragon_right5.png")})

        #Black dragon original image
        self.orig_black_dragon_left = {}
        self.orig_black_dragon_left.update({0: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_left0.png")})
        self.orig_black_dragon_left.update({1: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_left1.png")})
        self.orig_black_dragon_left.update({2: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_left2.png")})
        self.orig_black_dragon_left.update({3: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_left3.png")})
        self.orig_black_dragon_left.update({4: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_left4.png")})
        self.orig_black_dragon_left.update({5: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_left5.png")})
        self.orig_black_dragon_right = {}
        self.orig_black_dragon_right.update({0: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_right0.png")})
        self.orig_black_dragon_right.update({1: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_right1.png")})
        self.orig_black_dragon_right.update({2: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_right2.png")})
        self.orig_black_dragon_right.update({3: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_right3.png")})
        self.orig_black_dragon_right.update({4: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_right4.png")})
        self.orig_black_dragon_right.update({5: pygame.image.load("materials/images/monsters/black_dragon/black_dragon_right5.png")})

        #Non_Player_Character images
        #Fortune cat images
        self.orig_fortune_cat_img = {}
        self.orig_fortune_cat_img.update({0: pygame.image.load("materials/images/npc/fortune_cat/fortune_cat0.png")})
        self.orig_fortune_cat_img.update({1: pygame.image.load("materials/images/npc/fortune_cat/fortune_cat1.png")})
        self.orig_fortune_cat_img.update({2: pygame.image.load("materials/images/npc/fortune_cat/fortune_cat2.png")})
        self.orig_fortune_cat_img.update({3: pygame.image.load("materials/images/npc/fortune_cat/fortune_cat3.png")})
        self.orig_fortune_cat_img.update({4: pygame.image.load("materials/images/npc/fortune_cat/fortune_cat4.png")})
        self.orig_fortune_cat_img.update({5: pygame.image.load("materials/images/npc/fortune_cat/fortune_cat5.png")})

        #Death images
        self.orig_Death_img = {}
        self.orig_Death_img.update({0: pygame.image.load("materials/images/npc/Death/Death0.png")})
        self.orig_Death_img.update({1: pygame.image.load("materials/images/npc/Death/Death1.png")})
        self.orig_Death_img.update({2: pygame.image.load("materials/images/npc/Death/Death2.png")})
        self.orig_Death_img.update({3: pygame.image.load("materials/images/npc/Death/Death3.png")})
        self.orig_Death_img.update({4: pygame.image.load("materials/images/npc/Death/Death4.png")})
        self.orig_Death_img.update({5: pygame.image.load("materials/images/npc/Death/Death5.png")})
        self.orig_Death_img.update({6: pygame.image.load("materials/images/npc/Death/Death6.png")})
        self.orig_Death_img.update({7: pygame.image.load("materials/images/npc/Death/Death7.png")})
        self.orig_Death_img.update({8: pygame.image.load("materials/images/npc/Death/Death8.png")})

        #Little girl images
        self.orig_little_girl_img = {}
        self.orig_little_girl_img.update({0: pygame.image.load("materials/images/npc/little_girl/little_girl0.png")})
        self.orig_little_girl_img.update({1: pygame.image.load("materials/images/npc/little_girl/little_girl1.png")})
        self.orig_little_girl_img.update({2: pygame.image.load("materials/images/npc/little_girl/little_girl2.png")})
        self.orig_little_girl_img.update({3: pygame.image.load("materials/images/npc/little_girl/little_girl3.png")})
        self.orig_little_girl_img.update({4: pygame.image.load("materials/images/npc/little_girl/little_girl4.png")})
        self.orig_little_girl_img.update({5: pygame.image.load("materials/images/npc/little_girl/little_girl5.png")})
        self.orig_little_girl_img.update({6: pygame.image.load("materials/images/npc/little_girl/little_girl6.png")})


        #Boom images
        self.orig_boom ={}
        self.orig_boom.update({0: pygame.image.load("materials/images/booms/boom_0.png")})
        self.orig_boom.update({1: pygame.image.load("materials/images/booms/boom_1.png")})
        self.orig_boom.update({2: pygame.image.load("materials/images/booms/boom_2.png")})
        self.orig_boom.update({3: pygame.image.load("materials/images/booms/boom_3.png")})
        self.orig_boom.update({4: pygame.image.load("materials/images/booms/boom_4.png")})
        self.orig_boom.update({5: pygame.image.load("materials/images/booms/boom_5.png")})
        self.skeleton_soldier_boom_index = 0

        #Bullet images
        self.orig_bluebullet = pygame.image.load("materials/images/bullets/normal/bluebullet.png")
        self.orig_redbullet = pygame.image.load("materials/images/bullets/normal/redbullet.png")
        self.orig_coin_bullet = pygame.image.load("materials/images/bullets/special/coin_bullet.png")
        self.orig_skull_bullet = pygame.image.load("materials/images/bullets/special/skull_bullet.png")
        self.orig_fireball = pygame.image.load("materials/images/bullets/normal/fireball.png")
        self.orig_lightning_ball = pygame.image.load("materials/images/bullets/normal/lightning_ball.png")
        self.orig_black_fireball = pygame.image.load("materials/images/bullets/boss_skills/black_fireball/black_fireball.png")
        self.orig_ground_needles = {}
        self.orig_ground_needles.update({0: pygame.image.load("materials/images/bullets/boss_skills/ground_needle/ground_needle0.png")})
        self.orig_ground_needles.update({1: pygame.image.load("materials/images/bullets/boss_skills/ground_needle/ground_needle1.png")})
        self.orig_ground_needles.update({2: pygame.image.load("materials/images/bullets/boss_skills/ground_needle/ground_needle2.png")})
        self.orig_ground_needles.update({3: pygame.image.load("materials/images/bullets/boss_skills/ground_needle/ground_needle3.png")})
        self.orig_ground_needles.update({4: pygame.image.load("materials/images/bullets/boss_skills/ground_needle/ground_needle4.png")})
        self.orig_ground_needles.update({5: pygame.image.load("materials/images/bullets/boss_skills/ground_needle/ground_needle5.png")})


        #Treasure images
        self.orig_ruby_raw = pygame.image.load("materials/images/treasures/ruby_raw.png")
        self.orig_ruby_round = pygame.image.load("materials/images/treasures/ruby_round.png")
        self.orig_ruby_dragon = pygame.image.load("materials/images/treasures/ruby_dragon.png")
        self.orig_sapphire_raw = pygame.image.load("materials/images/treasures/sapphire_raw.png")
        self.orig_sapphire_round = pygame.image.load("materials/images/treasures/sapphire_round.png")
        self.orig_sapphire_dragon = pygame.image.load("materials/images/treasures/sapphire_dragon.png")

        #Coins images
        self.orig_some_coins = pygame.image.load("materials/images/coins/coins1.png")
        self.orig_lots_of_coins = pygame.image.load("materials/images/coins/coins2.png")
        self.orig_massive_coins = pygame.image.load("materials/images/coins/coins3.png")


        #Start and end images
        self.orig_start_img = pygame.image.load("materials/images/backgrounds/stairsup.gif")
        self.orig_end_img = pygame.image.load("materials/images/backgrounds/starsdown.gif")


        # self.orig_player_right.set_colorkey((255, 255, 255))
        self.maze_block_width = None
        self.maze_block_height = None
        self.player = None
        self.player_left = {}
        self.player_right = {}
        self.player_death = {}
        self.player_left = self.orig_player_left
        self.player_right = self.orig_player_right
        self.player_pre_health = None
        self.player_pre_energy = None
        self.player_pre_coins = None
        self.player_width = None
        self.player_height = None
        self.skeleton_soldier_width = None
        self.skeleton_soldier_height = None
        self.bluebullet_width = None
        self.bluebullet_height = None
        self.maze = None
        self.startx = None
        self.starty = None
        self.monster_born_coordinate = []
        self.npc_born_coordinate = None
        self.bg = None
        self.walls = []
        self.roads = []
        self.start = None
        self.end = None
        self.gamedone = False
        self.level = 1
        # self.level = 3

        #Monster born possibility
        self.skeleton_soldier_possibility = 0.4
        self.unicorn_possibility = 0.3
        self.blue_dragon_possibility = 0.2
        self.black_dragon_possibility = 0.1

        # Possibility of drop treasure
        self.p_drop_red = 0.2
        self.p_drop_blue = 0.3
        self.p_drop_coins = 0.5

        self.p_drop_rank1 = 0.4
        self.p_drop_rank2 = 0.5
        self.p_drop_rank3 = 0.6
        self.p_drop_rank4 = 1

        self.p_drop_rarity1_under_rank1 = 1
        self.p_drop_rarity2_under_rank1 = 0
        self.p_drop_rarity3_under_rank1 = 0

        self.p_drop_rarity1_under_rank2 = 0.8
        self.p_drop_rarity2_under_rank2 = 0.2
        self.p_drop_rarity3_under_rank2 = 0

        self.p_drop_rarity1_under_rank3 = 0
        self.p_drop_rarity2_under_rank3 = 0.8
        self.p_drop_rarity3_under_rank3 = 0.2

        self.p_drop_rarity1_under_rank4 = 0
        self.p_drop_rarity2_under_rank4 = 0
        self.p_drop_rarity3_under_rank4 = 1

        self.loadnewsettings()





    def loadnewsettings(self):
        self.maze_width += 2
        self.maze_height += 2
        self.maze_block_width = self.screen_width / self.maze_width
        self.maze_block_height = self.screen_height / self.maze_height


        #Player and monsters' size
        self.player_width = self.maze_block_width * 0.3
        self.player_height = self.maze_block_height * 0.4
        self.skeleton_soldier_width = self.maze_block_width/3
        self.skeleton_soldier_height = self.maze_block_height/3

        self.unicorn_width = self.maze_block_width / 2
        self.unicorn_height = self.maze_block_height / 2

        self.blue_dragon_width = self.maze_block_width * 3 / 5
        self.blue_dragon_height = self.maze_block_width * 3 / 5

        self.black_dragon_width = self.maze_block_width * 3 / 5
        self.black_dragon_height = self.maze_block_width * 3 / 5

        #NPCs' size
        #Fortune cat's size
        self.fortune_cat_width = self.maze_block_width * 0.8
        self.fortune_cat_height = self.maze_block_height * 0.8

        #Death's size
        self.Death_width = self.maze_block_width * 0.8
        self.Death_height = self.maze_block_height * 0.8

        #Little girl's size
        self.little_girl_width = self.maze_block_width * 0.8
        self.little_girl_height = self.maze_block_height * 0.8

        #Bullets' size
        self.bluebullet_width = self.maze_block_width / 5
        self.bluebullet_height = self.maze_block_height / 5
        self.redbullet_width = self.maze_block_width / 4
        self.redbullet_height = self.maze_block_height / 4
        self.coin_bullet_width = self.maze_block_width / 4
        self.coin_bullet_height = self.maze_block_width / 4
        self.skull_bullet_width = self.maze_block_width / 4
        self.skull_bullet_height = self.maze_block_width / 4
        self.fireball_width = self.maze_block_width / 3
        self.fireball_height = self.maze_block_height / 3
        self.lightning_ball_width = self.maze_block_width / 4
        self.lightning_ball_height  = self.maze_block_height / 4
        self.black_fireball_width = self.maze_block_width / 4
        self.black_fireball_height = self.maze_block_height / 4
        self.ground_needle_width = self.maze_block_width / 4
        self.ground_needle_height = self.maze_block_height / 4

        #Treasures' size
        #ruby
        self.ruby_raw_width = self.maze_block_width / 4
        self.ruby_raw_height = self.maze_block_height / 4
        self.ruby_round_width = self.maze_block_width /4
        self.ruby_round_height = self.maze_block_height / 4
        self.ruby_dragon_width = self.maze_block_width / 4
        self.ruby_dragon_height = self.maze_block_height / 4
        #sapphire
        self.sapphire_raw_width = self.maze_block_width / 4
        self.sapphire_raw_height = self.maze_block_height / 4
        self.sapphire_round_width = self.maze_block_width / 4
        self.sapphire_round_height = self.maze_block_height / 4
        self.sapphire_dragon_width = self.maze_block_width / 4
        self.sapphire_dragon_height = self.maze_block_height / 4

        #Coins' size
        self.some_coins_width = self.maze_block_width / 3
        self.some_coins_height = self.maze_block_width / 3
        self.lots_of_coins_width = self.maze_block_width / 3
        self.lots_of_coins_height = self.maze_block_height / 3
        self.massive_coins_width = self.maze_block_width / 2
        self.massive_coins_height = self.maze_block_height / 2



        self.wall_stone = {}
        self.road_stone = {}
        self.player_left = {}
        self.player_right = {}
        self.player_death = {}
        self.skeleton_soldier_left = {}
        self.skeleton_soldier_right = {}
        self.skeleton_soldier_boom = {}
        self.unicorn_left = {}
        self.unicorn_right = {}
        self.unicorn_boom = {}
        self.blue_dragon_left = {}
        self.blue_dragon_right = {}
        self.blue_dragon_boom = {}
        self.black_dragon_left = {}
        self.black_dragon_right = {}
        self.black_dragon_boom = {}
        self.ground_needles = {}
        self.fortune_cat_img = {}
        self.Death_img = {}
        self.little_girl_img = {}

        #Update wall image size
        for k,v in self.orig_wall_stone.items():
            self.wall_stone.update({k: pygame.transform.scale(v, (int(self.maze_block_width), int(self.maze_block_height)))})

        #Update road image size
        for k, v in self.orig_road_stone.items():
            self.road_stone.update({k: pygame.transform.scale(v, (int(self.maze_block_width), int(self.maze_block_height)))})

        #Update player image size
        for k, v in self.orig_player_left.items():
            self.player_left.update({k: pygame.transform.scale(v, (int(self.player_width), int(self.player_height)))})
        for k, v in self.orig_player_right.items():
            self.player_right.update({k: pygame.transform.scale(v, (int(self.player_width), int(self.player_height)))})
        for k, v in self.orig_player_death.items():
            self.player_death.update({k: pygame.transform.scale(v, (int(self.player_width), int(self.player_height)))})

        #Update skeleton soldier image size
        for k, v in self.orig_skeleton_soldier_left.items():
            self.skeleton_soldier_left.update({k: pygame.transform.scale(v, (int(self.skeleton_soldier_width), int(self.skeleton_soldier_height)))})
        for k, v in self.orig_skeleton_soldier_right.items():
            self.skeleton_soldier_right.update({k: pygame.transform.scale(v, (int(self.skeleton_soldier_width), int(self.skeleton_soldier_height)))})
        for k, v in self.orig_boom.items():
            self.skeleton_soldier_boom.update({k: pygame.transform.scale(v, (int(self.skeleton_soldier_width), int(self.skeleton_soldier_height)))})


        #Update unicorn image size
        for k, v in self.orig_unicorn_left.items():
            self.unicorn_left.update({k: pygame.transform.scale(v, (int(self.unicorn_width), int(self.unicorn_height)))})
        for k, v in self.orig_unicorn_right.items():
            self.unicorn_right.update({k: pygame.transform.scale(v, (int(self.unicorn_width), int(self.unicorn_height)))})
        for k, v in self.orig_boom.items():
            self.unicorn_boom.update({k: pygame.transform.scale(v, (int(self.unicorn_width), int(self.unicorn_height)))})

        #Update blue dragon image size
        for k, v in self.orig_blue_dragon_left.items():
            self.blue_dragon_left.update({k: pygame.transform.scale(v, (int(self.blue_dragon_width), int(self.blue_dragon_height)))})
        for k, v in self.orig_blue_dragon_right.items():
            self.blue_dragon_right.update({k: pygame.transform.scale(v, (int(self.blue_dragon_width), int(self.blue_dragon_height)))})
        for k, v in self.orig_boom.items():
            self.blue_dragon_boom.update({k: pygame.transform.scale(v, (int(self.blue_dragon_width), int(self.blue_dragon_height)))})

        #Update black dragon image size
        for k, v in self.orig_black_dragon_left.items():
            self.black_dragon_left.update({k: pygame.transform.scale(v, (int(self.black_dragon_width), int(self.black_dragon_height)))})
        for k, v in self.orig_black_dragon_right.items():
            self.black_dragon_right.update({k: pygame.transform.scale(v, (int(self.black_dragon_width), int(self.black_dragon_height)))})
        for k, v in self.orig_boom.items():
            self.black_dragon_boom.update({k: pygame.transform.scale(v, (int(self.black_dragon_width), int(self.black_dragon_height)))})

        #Update Non_Player_Character images size
        for k, v in self.orig_fortune_cat_img.items():
            self.fortune_cat_img.update({k: pygame.transform.scale(v, (int(self.fortune_cat_width), int(self.fortune_cat_height)))})

        for k, v in self.orig_Death_img.items():
            self.Death_img.update({k: pygame.transform.scale(v, (int(self.Death_width), int(self.Death_height)))})

        for k, v in self.orig_little_girl_img.items():
            self.little_girl_img.update({k: pygame.transform.scale(v, (int(self.little_girl_width), int(self.little_girl_height)))})

        #Update bullets' image size
        self.bluebullet_img = pygame.transform.scale(self.orig_bluebullet, (int(self.bluebullet_width), int(self.bluebullet_height)))
        self.coin_bullet_img = pygame.transform.scale(self.orig_coin_bullet, (int(self.coin_bullet_width), int(self.coin_bullet_height)))
        self.skull_bullet_img = pygame.transform.scale(self.orig_skull_bullet, (int(self.skull_bullet_width), int(self.skull_bullet_height)))
        self.redbullet_img = pygame.transform.scale(self.orig_redbullet, (int(self.redbullet_width), int(self.redbullet_height)))
        self.fireball_img = pygame.transform.scale(self.orig_fireball, (int(self.fireball_width), int(self.fireball_height)))
        self.lightning_ball_img = pygame.transform.scale(self.orig_lightning_ball,(int(self.lightning_ball_width), int(self.lightning_ball_height)))
        self.black_fireball_img = pygame.transform.scale(self.orig_black_fireball, (int(self.black_fireball_width), int(self.black_fireball_height)))
        for k, v in self.orig_ground_needles.items():
            self.ground_needles.update({k: pygame.transform.scale(v, (int(self.ground_needle_width), int(self.ground_needle_height)))})

        #Update start's amd end point's image
        self.start_img = pygame.transform.scale(self.orig_start_img, (int(self.maze_block_width), int(self.maze_block_height)))
        self.end_img = pygame.transform.scale(self.orig_end_img, (int(self.maze_block_width), int(self.maze_block_height)))

        #Update treassures' image size
        self.ruby_raw_img = pygame.transform.scale(self.orig_ruby_raw, (int(self.ruby_raw_width), int(self.ruby_raw_height)))
        self.ruby_round_img = pygame.transform.scale(self.orig_ruby_round, (int(self.ruby_round_width), int(self.ruby_round_height)))
        self.ruby_dragon_img = pygame.transform.scale(self.orig_ruby_dragon, (int(self.ruby_dragon_width), int(self.ruby_dragon_height)))
        self.sapphire_raw_img = pygame.transform.scale(self.orig_sapphire_raw, (int(self.sapphire_raw_width), int(self.sapphire_raw_height)))
        self.sapphire_round_img = pygame.transform.scale(self.orig_sapphire_round, (int(self.sapphire_round_width), int(self.sapphire_round_height)))
        self.sapphire_dragon_img = pygame.transform.scale(self.orig_sapphire_dragon, (int(self.sapphire_dragon_width), int(self.sapphire_dragon_height)))

        #Update coins image size
        self.some_coins_img = pygame.transform.scale(self.orig_some_coins, (int(self.some_coins_width), int(self.some_coins_height)))
        self.lots_of_coins_img = pygame.transform.scale(self.orig_lots_of_coins, (int(self.lots_of_coins_width), int(self.lots_of_coins_height)))
        self.massive_coins_img = pygame.transform.scale(self.orig_massive_coins, (int(self.massive_coins_width), int(self.massive_coins_height)))

        self.generatenewmaze()

        #Update the atk distance
        self.skeleton_soldier_atk_distance = self.maze_block_width / 2
        self.unicorn_atk_distance = self.maze_block_width * 2
        self.blue_dragon_atk_distance = self.maze_block_width * 6
        self.black_dragon_atk_distance = self.maze_block_width * 7

    def generatenewmaze(self):
        self.maze = mz.make_maze(self)
        # for (x, y), value in numpy.ndenumerate(self.maze):
        for (y, x), value in numpy.ndenumerate(self.maze):
            #value 2 represents  player start point
            if value == 2:
                self.startx = x
                self.starty = y
                # print("startx, starty", x, y)
                break
        self.walls, self.roads, self.start, self.end = mz.define_maze(self, self.maze)

        #Choose the monster born place
        for i in range(len(self.roads)):
            if random.randint(1,2) == 1:
            # if random.randint(1,100) == 1:
                self.monster_born_coordinate.append([self.roads[i].rect.left, self.roads[i].rect.top])
                # print("monster born place",self.monster_born_coordinate)

        #Chosse the Non_Player_Character born place
        index_max = len(self.roads) - 1
        print("index_max: ",index_max)
        index = random.randint(0, index_max)
        self.npc_born_coordinate = self.roads[index].rect.left, self.roads[index].rect.top



