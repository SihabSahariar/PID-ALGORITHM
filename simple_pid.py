import cv2
import numpy as np
import time


class pid_control:
    def __init__(self, _kp=0.1, _ki=0, _kd=0.0001):
        self.Kp = _kp
        self.Ki = _ki
        self.Kd = _kd

        self.current_value = 0

        self.cycle = 1

        self.error = 0
        self.dt_error = 0

    def calc_p(self):
        return round(float(self.Kp * self.error), 4)

    def calc_i(self):
        return round(float(self.Ki * self.dt_error), 4)

    def calc_d(self, _error):
        return round(float(self.Kd * _error), 4)

    def pid_calc(self, _target):
        _c = 0
        self.error = _target - self.current_value
        _c += self.calc_p()

        self.dt_error += self.error
        _c += self.calc_i()

        temp = self.dt_error / self.cycle
        _c += self.calc_d(temp)

        self.current_value += _c
        self.cycle += 1

    def get_current_value(self):
        return self.current_value

    def __str__(self):
        return "Current value = {0}, Error = {1}, Cycle = {2}".format(
            self.current_value, self.error, self.cycle
            )


if __name__ == "__main__":
    pid_controller = pid_control()

    target_value = 5123

    while True:
        pid_controller.pid_calc(target_value)
        print(pid_controller)
        time.sleep(0.01)
