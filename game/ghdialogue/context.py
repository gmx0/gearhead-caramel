
# Constants for dialogue contexts.

HELLO,ASK_FOR_ITEM,INFO,MISSION,PROBLEM,ACCEPT,ARREST,GOODBYE,JOIN,PERSONAL,ATTACK,CHALLENGE,COMBAT_INFO,MERCY,RETREAT,WITHDRAW,CHAT,OPEN_SHOP = range(18)

# HELLO = NPC says hello. Usually the first offer in a peaceful conversation.
# ASK_FOR_ITEM: The NPC gives the PC an item, or at least replies to the request.
#       The data property should contain "item"
# INFO: The NPC offers the PC some information.
#       The data property should contain "subject"
# MISSION: 
# ACCEPT: The NPC responds to PC accepting a mission or offer
# ARREST: The PC will attempt to arrest the NPC
# CHAT: The NPC will provide miscellaneous chatter, maybe including rumors + news.
# OPEN_SHOP: The NPC will provide shop services

# ATTACK: The greeting from a hostile NPC.
# CHALLENGE: The reply from a hostile NPC when challenged by PC.
# COMBAT_INFO: An information offer that occurs during combat.
#       The data property should contain "subject"
# MERCY: The enemy is being allowed to leave the battle.
# RETREAT: The enemy is withdrawing from battle.
# WITHDRAW: The PC is withdrawing from battle.


