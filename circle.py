import math


def area(r):
    '''
    Возвращает площадь круга радиусом r
    
        Параметры: 
            r (int): радиус крута
            
        Возвращаемое значение:
            math.pi * r * r (float): площадь круга 
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Возвращает периметр круга радиусом r
        
            Параметры: 
                r (int): радиус крута
                
            Возвращаемое значение:
                2 * math.pi * r (float): периметр круга 
        '''
    return 2 * math.pi * r

