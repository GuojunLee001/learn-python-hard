#coding:utf-8

# 导入的包
from sys import exit
from random import randint

# 创建一个类
class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

# 创建第二个类，
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

# 游戏第一个场景
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom wolud be proud..if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    def enter(self):
        print Death.quips[0, (len(self.quips)-1)]
        exit(1)
    
# 创建CentralCorridor并定义规则
class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet #25 have invaded ship ang destroyed"
        print "your entire crew. You are the lst surviving member and you last"
        print "mission is to get the neutron sestruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        
        action = raw_input("> ")
        
        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your lasser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "yu are dead. Then he aes you."
            return 'death'
            
        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip ang slide right"
            print "as the Gothon's blaster crankes a laser past you head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall ang pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head ang eats you."
            return 'death'
        
        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhap gur ubhfr, fur fvgf nebhap gur ubhfr."
            print "The Gothong stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughong you run up and shoot him square in the head"
            print "putting him dowm, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'
            
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

# 创建一个类            
class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch nd the room"
        print "for more Gothons that might be hiding It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the code"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock clases forever ad you can't"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_imput("[keypad]")
            
        if guess == code:
            print "The container clicks open and seal breaks, letting gas ut,"
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there,and finally the Gothon blow up the"
            print "ship from their ship and you die."
            return 'death'

# 创建一个类
class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destrust bomb"
        print "under your arm and surprise 5 Gothon who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. The haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        
        action = raw_imput("> ")
        
        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothon"
            print "and make a leap for the door. Right as you drop it a"
            print "Gouthon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
            
        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under you arm"
            print "and the Gouthon put their hands up and start to aseat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gouthon can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get odd this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
            
# 定义另外一个类
class EscapePod(Scene):

    def enter(self):
        print "You rush though the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gouthon are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"
        
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")
        
        if int(guess) != good_pod:
            print "You jump into %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "imp;odes as the hull reptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gouthon ship the same"
            print "time. You won!"
            
            return 'finished'
            
# 创建另外一个类
class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'
        
# 附加题
"""
门锁11次，原因是初始值不为0
通过return返回下一个房间
"""
