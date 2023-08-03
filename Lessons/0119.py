"""Check the light"""

light: str = input('what color is the light? ').lower()

if (light == 'green'):
    print("Go!")
    print("Have a safe trip! ")
else:
    if (light != "red"):
        if (light == 'yellow'):
            print('slow down')
        else:
            print("report this to the police")

    else: 
        print('Stop!')
print("according to the law: \"Don't look at your phone! \"")
