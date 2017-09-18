from pbge import effects
from pbge.scenes import animobs
import damage
import random

#  *******************
#  ***   AnimObs   ***
#  *******************

class SmallBoom( animobs.AnimOb ):
    SPRITE_NAME = 'anim_smallboom.png'
    SPRITE_OFF = ((0,0),(-7,0),(-3,6),(3,6),(7,0),(3,-6),(-3,-6))
    def __init__(self, sprite=0, pos=(0,0), loop=0, delay=1, y_off=0 ):
        super(SmallBoom, self).__init__(sprite_name=self.SPRITE_NAME,pos=pos,start_frame=0,end_frame=7,loop=loop,ticks_per_frame=1, delay=delay)
        self.x_off,self.y_off = self.SPRITE_OFF[sprite]
        self.y_off += y_off

class NoDamageBoom( SmallBoom ):
    SPRITE_NAME = 'anim_nodamage.png'

class BigBoom( animobs.AnimOb ):
    def __init__(self, pos=(0,0), loop=0, delay=1, y_off=0 ):
        super(BigBoom, self).__init__(sprite_name="anim_bigboom.png",pos=pos,start_frame=0,end_frame=7,loop=loop,ticks_per_frame=1, delay=delay, y_off=y_off)


#  *******************
#  ***   Effects   ***
#  *******************

class AttackRoll( effects.NoEffect ):
    """ One actor is gonna attack another actor.
        This may be opposed by a succession of defensive rolls.
        If a defensive roll beats the attack roll, its children get returned.
        Otherwise, the penetration score is recorded in the fx_record and
        the children of this effect get returned.
    """
    def __init__(self, att_stat, att_skill, children=(), anim=None, accuracy=0, penetration=0, defenses=() ):
        self.att_stat = att_stat
        self.att_skill = att_skill
        if not children:
            children = list()
        self.children = children
        self.anim = anim

    def handle_effect(self, camp, fx_record, originator, pos, anims, delay=0 ):
        if originator:
            att_bonus = originator.get_skill_score(self.att_stat,self.att_skill)
        else:
            att_bonus = random.randint(1,100)
        att_roll = random.randint(1,100)

        targets = camp.scene.get_actors(pos)
        for target in targets:
            hi_def_roll = 0
            for defense in self.defenses:
                if defense.can_attempt(originator,target):
                    def_roll = defense.make_roll(originator,target)
                    hi_def_roll = max(def_roll,hi_def_roll)

    def get_odds( self, camp, originator, target ):
        # Return the percent chance that this attack will hit.
        if originator:
            att_bonus = originator.get_skill_score(self.att_stat,self.att_skill)
        else:
            att_bonus = 50

class DoDamage( effects.NoEffect ):
    """ Whatever is in this tile is going to take damage.
    """
    def __init__(self, damage_n, damage_d, children=(), anim=None, scale=None ):
        if not children:
            children = list()
        self.damage_n = damage_n
        self.damage_d = damage_d
        self.children = children
        self.anim = anim
        self.scale = scale

    def handle_effect(self, camp, fx_record, originator, pos, anims, delay=0 ):
        targets = camp.scene.get_actors(pos)
        penetration = fx_record.get("penetration",random.randint(1,100))
        for target in targets:
            scale = self.scale or target.scale
            mydamage = damage.Damage( camp, scale.scale_health( 
                  sum( random.randint(self.damage_d) for n in range(self.damage_n) ),
                  gears.materials.Metal ), random.randint(1,100), mychar, anims )

#  **************************
#  ***   Defense  Rolls   ***
#  **************************

class DodgeRoll( object ):
    def make_roll( self, attacker, target ):
        pass
    def can_attempt( self, attacker, target ):
        pass

# BlockRoll, ParryRoll, ECMRoll, AntiMissileRoll







