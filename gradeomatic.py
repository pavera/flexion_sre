import argparse
from temp_converters import TempConverter

valid_scales = ['Fahrenheit', 'Celsius', 'Kelvin', 'Rankine']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('orig_temp', type=str, nargs=1,
                        help='Temperature to be converted')
    parser.add_argument('orig_scale', type=str, nargs=1, choices=valid_scales)
    parser.add_argument('dest_scale', type=str, nargs=1, choices=valid_scales)
    parser.add_argument('student_answer', type=str, nargs=1)

    args = parser.parse_args()
    tc = TempConverter()
    print(tc.run_conversion(args.orig_temp[0], args.orig_scale[0], args.dest_scale[0], args.student_answer[0]))


