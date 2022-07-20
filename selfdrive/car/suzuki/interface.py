#!/usr/bin/env python3
import math
from cereal import car
from selfdrive.config import Conversions as CV
from selfdrive.swaglog import cloudlog
import cereal.messaging as messaging
from selfdrive.car import gen_empty_fingerprint, get_safety_config
from selfdrive.car.interfaces import CarInterfaceBase



class CarInterface(CarInterfaceBase):
  #def __init__(self, CP, CarController, CarState):
  #  super().__init__(CP, CarController, CarState)

  #@staticmethod
  #def compute_gb(accel, speed):
  #  return accel

  @staticmethod
  def get_params(candidate, fingerprint=gen_empty_fingerprint(), car_fw=None):
    ret = CarInterfaceBase.get_std_params(candidate, fingerprint)
    ret.carName = "suzuki"
    ret.safetyConfigs = [get_safety_config(car.CarParams.SafetyModel.allOutput, 1)]
    
    ret.mass = 1700.
    ret.rotationalInertia = 2500.
    ret.wheelbase = 2.70
    ret.centerToFront = ret.wheelbase * 0.5
    ret.steerRatio = 13.  # reasonable
    ret.tireStiffnessFront = 1e6    # very stiff to neglect slip
    ret.tireStiffnessRear = 1e6     # very stiff to neglect slip

    return ret

  # returns a car.CarState
  def update(self, c, can_strings):
    
    # Process the most recent CAN message traffic, and check for validity
    # The camera CAN has no signals we use at this time, but we process it
    # anyway so we can test connectivity with can_valid
    self.cp.update_strings(can_strings)
    self.cp_cam.update_strings(can_strings)

    ret = self.CS.update(self.cp, self.cp_cam)
    ret.canValid = self.cp.can_valid and self.cp_cam.can_valid
    ret.steeringRateLimited = self.CC.steer_rate_limited if self.CC is not None else False
    
    
    events = self.create_common_events(ret)
    
    
    ret.events = events.to_msg()
    


    self.CS.out = ret.as_reader()
    return self.CS.out 
    
  def apply(self, c):
    ret = self.CC.update(c, self.CS, self.frame, c.actuators)
    self.frame += 1
    return ret
