import sys
import warnings
from dbus.mainloop.glib import DBusGMainLoop
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from friends import *

def test_remove_friend():
    mainloop = DBusGMainLoop(set_as_default=True)
    arguments = sys.argv[1].split(",")
    try:
        friend1 = FriendBuddyModel(arguments[0], arguments[1], arguments[2], arguments[3])
        os.chdir('../reports')
        f = open("testOutput.html", "a+")
        myFriends = Friends()
        myFriends.make_friend(friend1)
        test = (myFriends.has_buddy(friend1))
    except Exception as exception:
        print(exception)
    try:
        assert str(test) == sys.argv[2]
        return "Test Passed!"

    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but was: " + str(test)

if __name__ == '__main__':
    test_remove_friend()
    print(test_remove_friend())
