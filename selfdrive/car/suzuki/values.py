class CAR:
  SUZUKI = 'suzuki'
  
class CANBUS:
  pt = 0
  cam = 2 
  
  
class DBC_FILES:
  suzuki_vitara = "suzuki_vitara"  # Used for all cars with MQB-style CAN messaging 


class CarControllerParams:
  LKAS_STEP = 2                  # LKAS message frequency 50Hz

  # TODO: placeholder values pending discovery of true EPS limits
  STEER_MAX = 300                # As-yet unknown fault boundary, guessing 300 / 3.0Nm for now
  STEER_DELTA_UP = 3             # 3 unit/sec observed from factory LKAS, fault boundary unknown
  STEER_DELTA_DOWN = 3           # 3 unit/sec observed from factory LKAS, fault boundary unknown
  STEER_DRIVER_ALLOWANCE = 25
  STEER_DRIVER_MULTIPLIER = 3    # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1        # from dbc


