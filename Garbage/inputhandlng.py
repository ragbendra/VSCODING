def do_this():
    print("doing this")
def do_that():
    print("doing that")
match input("Do this or that: "):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print("Invalid Input")
