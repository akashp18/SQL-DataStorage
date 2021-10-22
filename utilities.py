

def int_Validator(input_amount):
    try:
        selected_int = int(input_amount)
        if selected_int < 0:
            print("Negative value detected.")
            return False, 0
        else:
            return True, selected_int
    except ValueError:
        print("Please enter number.")
        return False, 0


def show_UserAccessCount(email, accessCount):
    print("User : {}".format(email))
    print("Access count : {}".format(accessCount))


def writeBackup(result):
    FILE_NAME = "usersdb-backup.csv"
    backupFile = open(FILE_NAME, "w+")
    backupFile.truncate()
    for row in result:
        backupFile.write("{}, {}, {}, {}\n".format(row[0], row[1], row[2], row[3]))
    backupFile.close()