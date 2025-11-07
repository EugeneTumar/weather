from .tempCalculator import temp_calculator
from ..temptype import TempType
from ..weatherSchema import WeatherSchema

class TempConvertor:
    @staticmethod
    def temp_to_c(weather: WeatherSchema):
        if weather.temp_type == TempType.C:
            return 
        
        res = weather.temp
        if weather.temp_type == TempType.K:
            res = temp_calculator.k_to_c(weather.temp)
        if weather.temp_type == TempType.F:
            res = temp_calculator.f_to_c(weather.temp)
        
        weather.temp_type = TempType.C
        weather.temp = res

    
    @staticmethod
    def temp_to_f(weather: WeatherSchema):
        if weather.temp_type == TempType.F:
            return 
        
        res = weather.temp
        if weather.temp_type == TempType.K:
            res = temp_calculator.k_to_f(weather.temp)
        if weather.temp_type == TempType.C:
            res = temp_calculator.c_to_f(weather.temp)
        
        weather.temp_type = TempType.F
        weather.temp = res
    

    @staticmethod
    def temp_to_k(weather: WeatherSchema):
        if weather.temp_type == TempType.K:
            return 
        
        res = weather.temp
        if weather.temp_type == TempType.C:
            res = temp_calculator.c_to_k(weather.temp)
        if weather.temp_type == TempType.F:
            res = temp_calculator.f_to_k(weather.temp)
        
        weather.temp_type = TempType.K
        weather.temp = res

temp_convertor = TempConvertor()