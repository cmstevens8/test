def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

destination = input("enter your destination: ")

start_engine()
move_forward()

if destination == "grocery store":
    turn("left")
    print("You arrived at the grocery store")
elif destination == "tech park":
    turn("right")
    print("You arrived at the tech park")
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    print("You arrived at the roundabout")
    if destination == "hospital":
        print("Take the 1st exit")
        print("You arrived at the hospital")
    elif destination == "mall":
        print("Take the 2nd exit")
        move_forward()
        turn("right")
        print("You arrived at the mall")
    elif destination == "airport":
        print("Take the 3rd exit")
        print("You arrived at the airport")
    elif destination == "university" or destination == "stadium":
        print("take the 4th exit")
        move_forward()
        if destination == "university":
            turn("left")
            print("You arrived at the university")
        else:
            turn("right")
            print("You arrived at the stadium")
    else:
        print("Invalid destination")

stop_engine()