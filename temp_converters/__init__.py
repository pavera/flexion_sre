from decimal import Decimal


class InvalidTemp(Exception):
    pass


class TempConverter(object):

    @staticmethod
    def f_to_c(temp_f):
        return (temp_f - 32) * 5/Decimal('9.0')

    @staticmethod
    def f_to_k(temp_f):
        return (temp_f + Decimal('459.67')) * 5/Decimal('9.0')

    @staticmethod
    def f_to_r(temp_f):
        return temp_f + Decimal('459.67')

    @staticmethod
    def c_to_f(temp_c):
        return (temp_c * 9/Decimal('5.0')) + 32

    @staticmethod
    def c_to_k(temp_c):
        return temp_c + Decimal('273.15')

    @staticmethod
    def c_to_r(temp_c):
        return (temp_c * 9/Decimal('5.0')) + Decimal('491.67')

    @staticmethod
    def k_to_c(temp_k):
        if temp_k < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_k - Decimal('273.15')

    @staticmethod
    def k_to_f(temp_k):
        if temp_k < 0:
            raise InvalidTemp("Invalid Temp")
        return (temp_k * 9/Decimal('5.0')) - Decimal('459.67')

    @staticmethod
    def k_to_r(temp_k):
        if temp_k < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_k * 9/Decimal('5.0')

    @staticmethod
    def r_to_c(temp_r):
        if temp_r < 0:
            raise InvalidTemp("Invalid Temp")
        return (temp_r - Decimal('491.67')) * 5/Decimal('9.0')

    @staticmethod
    def r_to_f(temp_r):
        if temp_r < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_r - Decimal('459.67')

    @staticmethod
    def r_to_k(temp_r):
        if temp_r < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_r * 5/Decimal('9.0')

    def run_conversion(self, orig_temp, orig_scale, dest_scale, student_answer):
        conversion = "{0}_to_{1}".format(orig_scale[0].lower(), dest_scale[0].lower())
        try:
            answer = getattr(self, conversion)(Decimal(orig_temp))
            if round(answer) == round(Decimal(student_answer)):
                result = "correct"
            else:
                result = "incorrect"
        except InvalidTemp as exc:
            result = "invalid"

        return result
