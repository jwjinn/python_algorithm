

employee = {
  "ALICE" : 25,
  "BOB" : 30,
  "CHARLIE" : 20,
  "DAVE" : 25,
  "EVE" : 140,
}


class Employee:
    rasieAmount = 1.04

    def __init__(self, ):
        self.name = 'ALICE'

    def test(self, tt):

        for key, value in tt.items():
            print(key, value)

            if key == 'ALICE':
                print('ALCIE이다.')

            

t = Employee()
t.test(employee)