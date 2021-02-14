import json
name = ''
hp = int()
energy_type=''
weakness=''
resistance =()
moves= ()
is_fainted =()

with open('pokemon_party.json') as reader:
  info=json.load(reader)
for item in info:
  print(item["name"])


class Pokemon():

  def __init__(self,name,hp,energy_type,weakness,resistance,moves):
    self.name = str(item['name'])
    
    
    self.hp = int(item['hp'])

    
    self.energy_type =str(item['types'])

    
    weakness_type = item['weakness'][0]['type']
    weakness_value = item['weakness'][0]['value']
    self.weakness = f'({weakness_type},int{weakness_value})'
    print(self.weakness)
    resistance_type = item['weaknesses'][0]['type']
    self.resistance =resistance_type
    attack_name =item['attacks'][0]['name']
    attack_damage = item['attacks'][0]['damage']
    self.moves = ((str(attack_name), int(attack_damage)),)
    self.is_fainted=False

class PokeCardDex():
  def __init__(self,json_file_path=None):
     self.path = json_file_path
  def set_order(self,order):
      pass  
  def battle(self,challenger_party):
      pass
  def heal_party(self):
      pass
  def add_to_party(self):
      pass

if __name__ == "__main__":
  my_dex=PokeCardDex('pokemon_party_2021-02-09.json')
  rival_dex=PokeCardDex('rivalParty.json')
  print(rival_dex)
  Cymdie = Pokemon('Cymdie',50,'Water',None,None,(('waterfall',30),),)
  my_dex=PokeCardDex('pokemon_party_2021-02-09.json')
  rival_dex=PokeCardDex('rivalParty.json')
  rival2_dex = PokeCardDex()
  CGYdie= Pokemon('CGYdie','60','electric',None,None,(('electric charge',20),),)
