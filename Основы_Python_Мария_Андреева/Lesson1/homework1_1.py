nik = "npkfrolov"
device = "MacBook"
work_version = "Python 2.7"
desired_version = "Python 3.7"

print ("Some apps on my %3s" % device)
print ("run under %3s" % work_version)
print ("I'm afraid to spoil it by %3s" % desired_version)
answer = raw_input(
    "What is the best option?\n 1 - install %s on MacOS and repair the rest processes then?\n 2 - install %s under Ubuntu 18 powered by VM Oracle?\n 3 - buy a particular NoteBook with Linux for experiments\n Insert a proper number: " % (
    desired_version, desired_version))

if answer == "1":
        print("\n My developers say it may be dangerous")
elif answer == "2":
        print ("\n It may be uncomfortable to operate between MacOS and Ubuntu in the course of learning")
elif answer == "3":
        print ("\n I've gone to spend money")
print ("\n So, your advise is %s. Anyway, thanks a lot. Sorry for 'raw_input' and no f-strings" %answer)

