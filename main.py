class Beat():
    def __init__(self,hat,clap,kick,bass,melody,time):
        self.hat=hat
        self.clap=clap
        self.kick=kick
        self.bass=bass
        self.melody=melody
        self.time=time
    def pattern(self):
        print('Я написал бит за ',self.time)
    def score(self):
        if self.time <= 5 and (self.hat+self.clap+self.kick+self.bass+self.melody)<5:
            wrost='бит говно'
        else:
            wrost='написал хит'
        print("В итоге",wrost)
nomelody=Beat(hat=1,clap=1,kick=1,bass=1,melody=0,time=4)
print(nomelody.time)
nomelody.pattern()
nomelody.score()
hiphop=Beat(hat=1,clap=1,kick=1,bass=3,melody=2,time=30)
print(hiphop.score)