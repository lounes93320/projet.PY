class player:
    def __init__(self, name):
        if name == "vegeta":
            self.name = name
            self.pv = 180
            self.attack = 50
            self.deffense = 30
        elif name == "melito":
            self.name = name
            self.pv = 210
            self.attack = 60
            self.deffense = 10
        elif name == "gougoutman":
            self.name = name
            self.pv = 150
            self.attack = 80
            self.deffense = 5    
        else :
            self.name = "goku"
            self.pv = 200
            self.attack = 40
            self.deffense = 40


