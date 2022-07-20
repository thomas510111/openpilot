from selfdrive.car import apply_std_steer_torque_limits
from selfdrive.car.suzuki.values import DBC_FILES, CANBUS, CarControllerParams as P
from opendbc.can.packer import CANPacker

class CarController():
  def __init__(self, dbc_name, CP, VM):
    self.apply_steer_last = 0
    self.CP = CP

    self.packer_pt = CANPacker(DBC_FILES.suzuki_vitara)

    self.steer_rate_limited = False

  def update(self, c, CS, frame, actuators):
    """ Controls thread """

    can_sends = []
      
    new_actuators = actuators.copy()


    return new_actuators, can_sends
