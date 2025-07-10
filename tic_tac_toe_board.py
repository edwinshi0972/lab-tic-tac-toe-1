from dataclasses import dataclass, field
from typing import List
import redis
import os
import json

@dataclass
class TicTacToeBoard:
    state: str = "is_playing"
    player_turn: str = "x"
    positions: List[str] = field(default_factory=lambda: ["", "", "", "", "", "", "", "", ""], init=False)
    
    redis_password = os.getenv('REDIS_PASSWORD')
    r = redis.Redis(
        host='ai.thewcl.com',  # Replace with your Redis host
        port=6379,               # Default port is 6379
        password=redis_password # Replace with your Redis password
    )
    
    TIC_TAC_TOE_GAME_STATE_KEY = "tic_tac_toe:game_state:{team}"
    team_number = "TA"
    key = TIC_TAC_TOE_GAME_STATE_KEY.format(team=team_number)
    
    def serialize(self):
        return json.dumps({
            "state": self.state,
            "player_turn": self.player_turn,
            "positions": self.positions
        })
        
    def save_to_redis(self):
        self.r.json().set(self.key, ".", self.serialize())
    
        
    def is_my_turn(self, i_am):
        return self.player_turn == i_am
    
    def make_move(self, index: int):
        if self.state != "is_playing":
            return
        
        if index < 0 or index > 8:
            return
            
        if self.positions[index] != "":
            return
        
        self.positions[index] = self.player_turn
        
        winner = self.check_winner()
        if winner is not None:
            self.state = winner    
        elif self.check_draw():
            self.state = "draw"
        else:
            self.switch_turn()
            
    def switch_turn(self):
        if self.player_turn == "x":
            self.player_turn = "o"
        else:
            self.player_turn = "x"
        
    def check_winner(self):
        if self.positions[0] == self.positions[1] == self.positions[2] == "x":
            return "x"
        
        if self.positions[0] == self.positions[1] == self.positions[2] == "o":
            return "o"
        
        if self.positions[3] == self.positions[4] == self.positions[5] == "x":
            return "x"
        
        if self.positions[3] == self.positions[4] == self.positions[5] == "o":
            return "o"
        
        if self.positions[6] == self.positions[7] == self.positions[8] == "x":
            return "x"
        
        if self.positions[6] == self.positions[7] == self.positions[8] == "o":
            return "o"
        
        if self.positions[0] == self.positions[3] == self.positions[6] == "x":
            return "x"
        
        if self.positions[0] == self.positions[3] == self.positions[6] == "o":
            return "o"
        
        if self.positions[1] == self.positions[4] == self.positions[7] == "x":
            return "x"
        
        if self.positions[1] == self.positions[4] == self.positions[7] == "o":
            return "o"
        
        if self.positions[2] == self.positions[5] == self.positions[8] == "x":
            return "x"
        
        if self.positions[2] == self.positions[5] == self.positions[8] == "o":
            return "o"
        
        if self.positions[0] == self.positions[4] == self.positions[8] == "x":
            return "x"
        
        if self.positions[0] == self.positions[4] == self.positions[8] == "o":
            return "o"
        
        if self.positions[2] == self.positions[4] == self.positions[6] == "x":
            return "x"
        
        if self.positions[2] == self.positions[4] == self.positions[6] == "o":
            return "o"
        
        return None
    
    def check_draw(self):
        for position in self.positions:
            if position == "":
                return False
        
        return self.check_winner() is None