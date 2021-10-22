from DBHelper import DBHelper
import ChyperMap
import utilities


class UserManagement:
    def Login(self):
        print("Enter your credentials to login:\n")
        userEmail = input("Enter your Email:\n")
        userPassword = input("Enter your Password:\n").upper()
        encryptedPassword = userPassword.translate(ChyperMap.character_map)
        userChecked = self.checkIfUserExist(userEmail)
        if userChecked[0]:
            # fetch second position form tuple, then first object of array and in last first position of tuple
            if userChecked[1][0][0] == encryptedPassword:
                DBHelper().updateUser(userEmail)
                self.takeBackup()
                print("------------------------")
                print("{} Successfully Login.".format(userEmail))
                print("------------------------")
                updatedUser = self.getUpdatedUserByEmail(userEmail)
                utilities.show_UserAccessCount(userEmail, updatedUser[1][0][1])
                self.Continue()
            else:
                print("Please enter valid password.\n")
                self.Login()
        else:
            print("{} email-id not found in database.".format(userEmail))
            self.get_Menu()

    def RegisterUser(self):
        print("User Registration")
        userEmail = input("Enter Email:\n")
        userPassword = input("Enter Password:\n").upper()
        if self.checkIfUserExist(userEmail)[0]:
            print("{} found in database, you can't use it.".format(userEmail))
            self.get_Menu()
        else:
            encryptedPassword = userPassword.translate(ChyperMap.character_map)
            DBHelper().insertUser(userEmail, encryptedPassword)
            #DBHelper().updateUser(userEmail)
            self.takeBackup()
            print("--------------------------------------------")
            print("Congratulation!!, User Successfully Created.")
            print("--------------------------------------------")
            self.Continue()

    def checkIfUserExist(self, userEmail):
        dbResults = DBHelper().selectUser(userEmail)
        if len(dbResults) == 0:
            return False, []
        else:
            return True, dbResults

    def getUpdatedUserByEmail(self,email):
        result = self.checkIfUserExist(email)
        return result[0], result[1]

    def Continue(self):
        inputCorrect = False
        while not inputCorrect:
            print("########################################################")
            user_input = input("Do you wants to Continue? Press 'Y' for YES and 'N' for NO:\n").upper()
            if user_input == 'N':
                inputCorrect = True
                print("Thank you for visiting.")
            elif user_input == 'Y':
                inputCorrect = True
                self.get_Menu()
            else:
                print("Please enter valid input.\n")

    def get_Menu(self):
        print("1. Create User")
        print("2. Login")
        print("3. Quit")
        correct_input = False
        while not correct_input:
            selectedOption = input("Please enter valid choice from above options:\n")
            enteredValue = utilities.int_Validator(selectedOption)
            if enteredValue[0] and enteredValue[1] < 4:
                correct_input = True
                if enteredValue[1] == 1:
                    self.RegisterUser()
                elif enteredValue[1] == 2:
                    self.Login()
                elif enteredValue[1] == 3:
                    print("Thank you for visiting.")
            else:
                pass

    def takeBackup(self):
        results = DBHelper().selectAllUsers()
        utilities.writeBackup(results)
