from .qma6100 import qma6100_


def get_lcd() -> list[float]:
    '''
    获取IMU的加速度数据，返回一个包含三个浮点数的列表，分别表示X、Y、Z轴的加速度值。
    '''
    qma = qma6100_()
    if qma.is_available():
        return qma.read()
    return [0.0, 0.0, 0.0] 