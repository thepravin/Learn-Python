class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass=acc_pass  # private : __variable

    def reset_pass(self):
        print(self.__acc_pass)

    def __forget_pass(self):  # private fun
        print(self.__acc_pass)


acc1 = Account(123456, "abcd")
print(acc1.acc_no)
# print(acc1.__acc_pass) error: AttributeError: 'Account' object has no attribute '__acc_pass'
acc1.reset_pass()

# acc1.__forget_pass() error:
