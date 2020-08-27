from cmd import Cmd
from pyfiglet import Figlet

class JukeBox():
  def __init__(self,name,songs):
    self.name = name
    self.songs = []
    for song in songs:
      self.songs.append(song.name)
    # copying by valye not reference
    self.queue = self.songs[:]

  #def floatConversion(self,coin):

  
  def records(self):
    if not self.queue:
      self.queue = self.songs
      '''
      ['Through The Fire and Flames',
                    'Fury of The Storm',
                    'Heroes of Out Time',
                    'Soldiers of The Wastelands',
                    'Cry Thunder']
      '''
      print('recharge de la pile')
      return self.queue
    elif len(self.queue) == 1:
      return self.queue + self.songs[0:5]
    elif len(self.queue) == 2:
      return self.queue + self.songs[0:4]
    else:
      return self.queue

  def play(self,coin):
    self.queue = self.records()
    if coin == 50:
      selected = self.queue.pop(0)
      print(f"Jukebox will play: '{selected}'")
    elif coin == 2:
      for i in range(0,3):
        if i == 0:
          print(f"Jukebox will play: '{self.queue.pop(0)}'")
        else:
          print(f"followed by: '{self.queue.pop(0)}'")
    else:
      print(f"Not enough money")

class Song:
  def __init__(self,name):
    self.name = name


class Menu(Cmd):
  f = Figlet(font ='slant')
  print(f.renderText('JukeBox\n'))
  print('-------------------------------------------------')
  print('----------------------Menu-----------------------')
  print('-------------------------------------------------\n')

  print('One song for 0.50\u20ac')
  print('Three songs for 2\u20ac \n')

  print('* To run music insert money with command add\n')
  print('* Press q to exit at anytime \n')
  prompt = 'jukebox2020> '

  def __init__(self):
    super(Menu, self).__init__()
    song1 = Song('Through The Fire and Flames')
    song2 = Song('Fury of The Storm') 
    song3 = Song('Heroes of Out Time') 
    song4 = Song('Soldiers of The Wastelands') 
    song5 = Song('Cry Thunder') 
    self.jukebox = JukeBox('JukeBox 2020',[song1,song2,song3,song4,song5])
  
  def do_q(self, args=True):
    print('\n Closed Jukebox')
    raise SystemExit

  def do_add(self,args=True):
    try:
        self.jukebox.play(int(args[0:2]))
    except Exception as e:
      print('\nFailed')


def main():
  # les pièces acceptées sont 0.10,0.20,0.50,1 et 2 euros
  menu = Menu().cmdloop('Starting the jukebox...\n' + 'Please insert coins...\n'+'50 cents or 2 euros\n')

if __name__ == '__main__':
  main()