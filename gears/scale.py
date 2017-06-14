# A gear's scale determines how big of a thing we're talking about.
# There are two scales: MechaScale and HumanScale. The first is really
# really big and the second is relatively tiny.
#
# The scales are singletons- instead of instancing, just point to the class.

class MechaScale( object ):
    SIZE_FACTOR = 10
    COST_FACTOR = 2
    @classmethod
    def scale_mass( self, mass, material ):
        # Scale mass based on scale and material.
        # The universal mass unit is 100 grams.
        return int( ( mass * pow( self.SIZE_FACTOR, 3 ) * material.mass_scale ) // 10 )
    @classmethod
    def scale_cost( self, cost , material ):
        # Scale mass based on scale and material.
        return ( cost * self.SIZE_FACTOR*self.COST_FACTOR * material.cost_scale ) // 10
    @classmethod
    def scale_health( self, hp , material ):
        # Scale mass based on scale and material.
        return ( hp * ( self.SIZE_FACTOR ** 2 ) * material.damage_scale ) // 2

class HumanScale( MechaScale ):
    SIZE_FACTOR = 1
    COST_FACTOR = 5
