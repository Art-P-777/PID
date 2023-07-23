class MassSpringDamper:
    def __init__(self, kof_prug, cof_sopr, mass, tmp_10=0, speed0=0, delta_t=0.01):
        self.kof_prug = kof_prug
        self.cof_sopr = cof_sopr
        self.mass = mass
        self.delta_t = delta_t
        self.tmp_1 = tmp_10
        self.speed = speed0

    def update(self, F):
        tmp_1new = self.speed * self.delta_t + self.tmp_1
        speednew = self.delta_t / self.mass * (F - self.cof_sopr * self.speed - self.kof_prug * self.tmp_1) + self.speed
        self.tmp_1 = tmp_1new
        self.speed = speednew
        return self.tmp_1
