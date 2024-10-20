import math
while True:
    try:
        shape = input("Enter shape: ")
        shape = shape.lower()
        if shape == "sphere":
            radius = float(input("Enter radius: "))
            if radius < 0:
                raise ValueError("Radius cannot be negative")
            vol_sphere = (4/3) * math.pi * (radius**3)
            print(vol_sphere)
            break
        elif shape == "cylinder":
            radius = float(input("Enter radius: "))
            if radius < 0:
                raise ValueError("Radius cannot be negative")
            height = float(input("Enter height: "))
            if height < 0:
                raise ValueError("Height cannot be negative")
            vol_cylinder = math.pi * (radius**2) * height
            print(vol_cylinder)
            break
    except:
        print("Enter valid size")

