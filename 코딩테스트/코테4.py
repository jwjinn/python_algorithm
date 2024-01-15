HOURLY_RATE_FOR_ALICE = 25
HOURLY_RATE_FOR_BOB = 30
HOURLY_RATE_FOR_CHARLIE = 20
HOURLY_RATE_FOR_DAVE = 25
HOURLY_RATE_FOR_EVE = 140


class SalaryCalculator:

    def __init__(self):
        self.total_cost = None
        self.result = None
        self.hourly_rate = None

    def pay_salary(self):
        if self.result == None:
            self.result = ""

        if self.total_cost == None:
            self.total_cost = 0

        user_file = open("users.txt")
        user_file.readline()
        while True:
            user = user_file.readline()
            if not user:
                break
            user = user.strip()

            # parse user name, worked time
            user, worked_time, _, _, bc = user.split(" ")
            hour = worked_time[:2]
            min = worked_time[5:7]
            hour = float(hour) + float(min) / 60
            self.calculate_payroll(user, hour, bc)

        for pay in self.result.split("\n"):
            if pay:
                self.total_cost += float(pay.split(",")[0].split(" ")[-1])
        # pay salary
        self.result += "TC=" + str(self.total_cost) + "\n"
        return self.result

    def calculate_payroll(self, employee_name, hours_worked, benefits_cost):
        user_table = open("users.txt")
        user_table.readline()
        result = ""
        while True:
            line = user_table.readline()
            user = line.strip().split(" ")[0]
            if user == employee_name:
                bank = line.strip().split(" ")[2]
                account = line.strip().split(" ")[3]
                result += f"Pay {user} "
                if user == "Alice":
                    self.hourly_rate = HOURLY_RATE_FOR_ALICE
                elif user == "Bob":
                    self.hourly_rate = HOURLY_RATE_FOR_BOB
                elif user == "Charlie":
                    self.hourly_rate = HOURLY_RATE_FOR_CHARLIE
                elif user == "Dave":
                    self.hourly_rate = HOURLY_RATE_FOR_DAVE
                elif user == "Eve":
                    self.hourly_rate = HOURLY_RATE_FOR_EVE
                break
        user_table.close()

        while True:
            if self.hourly_rate == 25:
                if hours_worked <= 40:
                    salary = hours_worked * self.hourly_rate
                else:
                    overtime_hours = hours_worked - 40
                    salary = 40 * self.hourly_rate + overtime_hours * self.hourly_rate * 1.5
                if salary >= 5000:
                    tax_rate = 0.35
                else:
                    tax_rate = 0.25
                taxes = salary * tax_rate
            elif self.hourly_rate == 30:
                if hours_worked <= 40:
                    salary = hours_worked * self.hourly_rate
                else:
                    overtime_hours = hours_worked - 40
                    salary = 40 * self.hourly_rate + overtime_hours * self.hourly_rate * 1.5
                if salary >= 6000:
                    tax_rate = 0.35
                else:
                    tax_rate = 0.25
                taxes = salary * tax_rate
            else:
                if hours_worked <= 40:
                    salary = hours_worked * self.hourly_rate
                else:
                    overtime_hours = hours_worked - 40
                    salary = 40 * self.hourly_rate + overtime_hours * self.hourly_rate * 1.5
                if salary >= 4000:
                    tax_rate = 0.35
                else:
                    tax_rate = 0.25
                taxes = salary * tax_rate
            total_cost = salary + taxes + float(benefits_cost)
            if total_cost >= 10000:
                print("Warning: total cost is too high! Trying again with higher rate")
                self.hourly_rate -= 5
                continue
            else:
                break

        result += str(int(total_cost)) + ", " + bank + " " + account + "\n"
        self.result = result
        return self.result


k = SalaryCalculator()
# k.pay_salary()
print(k.calculate_payroll('Alice', 42,1000))