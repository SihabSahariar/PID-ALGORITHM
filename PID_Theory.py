class PID_ALGO:
    def __init__(self,setpoint,t_now,Kp=0,Ki=0,Kd=0):
        self.setpoint = setpoint
        self.t_last = t_now
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0

    def tune(self,process,t_now):
        error = process - self.setpoint
        delta_time = t_now - self.t_last
        proportional = self.Kp * error
        integral = self.Ki * error
        derivative = self.Kd * ((error - self.last_error) / (delta_time))
        desired_process = proportional + integral + derivative
        self.t_last = t_now
        self.last_error = error
        return desired_process

test_controller_1 = PID_ALGO(setpoint = 66, t_now = 0, Kp = 0.2, Kd = 0.1, Ki = 1.0)
print(test_controller_1.tune(66.1,1))
print(test_controller_1.tune(66.2,2))
print(test_controller_1.tune(65.9,3))
print('-------------')

test_controller_1 = PID_ALGO(setpoint = 66, t_now = 0, Kp = 0.2, Kd = 0.1, Ki = 1.5)
print(test_controller_1.tune(66.1,1))
print(test_controller_1.tune(66.2,2))
print(test_controller_1.tune(65.9,3))
print('-------------')

test_controller_1 = PID_ALGO(setpoint = 66, t_now = 0, Kp = 0.2, Kd = 0.1, Ki = 1.2)
print(test_controller_1.tune(66.1,1))
print(test_controller_1.tune(66.2,2))
print(test_controller_1.tune(65.9,3))