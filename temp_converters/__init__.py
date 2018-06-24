class InvalidTemp(Exception):
    pass


class TempConverter(object):

    def f_to_c(self, temp_f):
        return (temp_f - 32) * 5/9.0

    def f_to_k(self, temp_f):
        return (temp_f + 459.67) * 5/9.0

    def f_to_r(self, temp_f):
        return temp_f + 459.67

    def c_to_f(self, temp_c):
        return (temp_c * 9/5.0) + 32

    def c_to_k(self, temp_c):
        return temp_c + 273.15

    def c_to_r(self, temp_c):
        return (temp_c * 9/5.0) + 491.67

    def k_to_c(self, temp_k):
        if temp_k < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_k - 273.15

    def k_to_f(self, temp_k):
        if temp_k < 0:
            raise InvalidTemp("Invalid Temp")
        return (temp_k * 9/5.0) - 459.67

    def k_to_r(self, temp_k):
        if temp_k < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_k * 9/5.0

    def r_to_c(self, temp_r):
        if temp_r < 0:
            raise InvalidTemp("Invalid Temp")
        return (temp_r - 491.67) * 5/9.0

    def r_to_f(self, temp_r):
        if temp_r < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_r - 459.67

    def r_to_k(self, temp_r):
        if temp_r < 0:
            raise InvalidTemp("Invalid Temp")
        return temp_r * 5/9.0

    def run_conversion(self, orig_temp, orig_scale, dest_scale, student_answer):
        conversion = "{0}_to_{1}".format(orig_scale[0].lower(), dest_scale[0].lower())
        try:
            answer = getattr(self, conversion)(orig_temp)
            if round(answer) == round(student_answer):
                print("correct")
            else:
                print("incorrect")
        except InvalidTemp as exc:
            print("invalid")