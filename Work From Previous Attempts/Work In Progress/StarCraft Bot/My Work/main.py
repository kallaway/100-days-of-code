
import sys
import os

import sc2

from sc2 import run_game, maps, Race, Difficulty
from sc2.ids.unit_typeid import UnitTypeId
from sc2.player import Bot, Computer

class StarterBot(sc2.BotAI):
    async def on_step(self, iteration: int):
        #what to do every step
        await self.distribute_workers() #in sc2/bot_ai.py
        
        if(
            self.can_afford(UnitTypeId.SCV)
            and self.supply_left > 0
            and self.supply_workers < 22
            and(
                self.structures(UnitTypeId.BARRACKS).ready.amount < 1
                and self.townhalls(UnitTypeId.COMMANDCENTER).idle
                and self.townhalls(UnitTypeId.ORBITALCOMMAND).idle
            )
        ):
            for th in self.townhalls.idle:
                th.train(UnitTypeId.SCV)
        

run_game(maps.get("AcropolisLE"), [
    Bot(Race.Terran, StarterBot()),
    Computer(Race.Zerg, Difficulty.Easy)
], realtime = True)

