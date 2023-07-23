class PID:
    def __init__(self, k_p, k_d, k_i, delta_t, lower_bound, upper_bound):
        self.k_p = k_p
        self.k_d = k_d
        self.k_i = k_i
        self.delta_t = delta_t
        self.prev_err = None
        self._prop = 0
        self._dif = 0
        self._integ = 0
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def _constain(self,tmp):
        if tmp > self.upper_bound:
            return self.upper_bound
        elif tmp < self.lower_bound:
            return self.lower_bound
        return tmp

    def update(self, real_x, x_des):
        err = real_x - x_des
        self._prop = self.k_p * err
        if self.prev_err is not None:
            self._dif = self.k_d * (err - self.prev_err) / self.delta_t
        self._integ += self.k_i * err
        self.prev_err = err
        outp = self._prop + self._dif + self._integ
        return self._constain(outp)
    