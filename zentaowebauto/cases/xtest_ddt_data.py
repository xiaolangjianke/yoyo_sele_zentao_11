import unittest
import ddt

datas = [
    {"user":"admin1", "psw":"1111111111"},
    {"user":"admin2", "psw":"22222222222"},
    {"user":"admin3", "psw":"3333333333"},
    {"user":"admin4", "psw":"44444444"},
    {"user":"admin4", "psw":"555555555"},
]

@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*datas)
    def test_(self, test_data):
        u = test_data["user"]
        print(u)
        p = test_data["psw"]
        print(p)

if __name__ == '__main__':
    unittest.main(verbosity=2)
