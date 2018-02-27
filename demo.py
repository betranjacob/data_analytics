import exercise as ex
import utils

def call(f, *args):
    try:
        print(f.__name__)
        result = f(*args)
        print(result)
        print('completed')
        return result
    except ValueError as err:
        print('{0} Failed, Value Error {1}'.format(f.__name__, err))
    except Exception as err:
        print('{0} Failed, {1}'.format(f.__name__, err))

s = utils.load_json_as_string()
a = call(ex.run_part_a, s)
b = call(ex.run_part_b, s)
c = call(ex.run_part_c, s)
d = call(ex.run_part_d, s)
call(ex.run_chart_c, c)
call(ex.run_chart_d, d)
