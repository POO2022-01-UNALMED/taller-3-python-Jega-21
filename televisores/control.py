class Control:
    def __init__(self):
        self._tv = None
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.tunrOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDowm(self):
        self._tv.canalDowm()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()
    def setCanal(self):
        self._tv.setCanal(canal)
    def enlazar(self, tv):
        self.setTv(tv)
        self._tv.setControl(self)
    def getTv(self):
        return self._tv
    def setTv(self, tv):
        self._tv = tv