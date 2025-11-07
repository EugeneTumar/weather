
class TempCalculator:
    @staticmethod
    def k_to_c(k: float):
        return k - 273
    
    @staticmethod
    def c_to_k(c: float):
        return c +273

    @staticmethod
    def c_to_f(c: float):
        return (c * 9/5) + 32

    @staticmethod
    def f_to_c(f: float):
        return (f - 32) * 5/9
    
    @staticmethod
    def k_to_f(k: float):
        return ((k - 273) * 9/5) + 32

    @staticmethod
    def f_to_k(f: float):
        return ((f - 273) - 32) * 5/9
    
temp_calculator = TempCalculator()
