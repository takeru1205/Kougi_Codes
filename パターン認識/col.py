class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def pink(String):
    print(Colors.HEADER+String+Colors.ENDC)

def blue(String):
    print(Colors.OKBLUE+String+Colors.ENDC)

def red(String):
    print(Colors.WARNING+String+Colors.ENDC)
