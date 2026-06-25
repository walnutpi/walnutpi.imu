
from .imu.qma6100 import qma6100_


def qma6100_direction() -> int|None:
    qma = qma6100_()
    if not qma.is_available():
        return None
    date = qma.read()
    # 方向0 [-0.069, -1.042, 0.075]
    # 方向1 [-1.04, -0.064, 0.059]
    # 方向2 [-0.007, 0.958, 0.066]
    # 方向3 [0.94, -0.03, -0.011]

    # 若 X 和 Y 都很小（设备平放），默认返回 0
    if abs(date[0]) < 0.3 and abs(date[1]) < 0.3:
        return 0

    # 否则比较 X 和 Y 轴的绝对值，判断设备朝向
    if abs(date[1]) > abs(date[0]):  # Y轴主导
        return 0 if date[1] < 0 else 2
    else:  # X轴主导
        return 1 if date[0] < 0 else 3

def get_lcd()->int: 
    '''
    获取IMU的方向数据，返回为0到3，分别对应设备的四个方向
    '''
    res = qma6100_direction()
    if res is not None:
        return res

    return 0