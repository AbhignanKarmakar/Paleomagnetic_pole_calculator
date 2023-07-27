import math

def calculate_magnetic_pole(latitude, longitude, declination, inclination):
    # Convert all angles from degrees to radians
    latitude = math.radians(latitude)
    longitude = math.radians(longitude)
    declination = math.radians(declination)
    inclination = math.radians(inclination)

    # Calculate the magnetic pole coordinates
    P = math.atan(2/math.tan(inclination))
    pole_latitude = math.asin(math.sin(latitude) * math.cos(P) +
                              math.cos(latitude) * math.sin(P) * math.cos(declination))

    B = math.asin(math.sin(P) * math.sin(declination) / math.cos(pole_latitude))
    if math.cos(P) < math.sin(latitude) * math.sin(pole_latitude):
        pole_longitude = longitude + (180 - B)
    else:
        pole_longitude = longitude + B

    # Convert the pole coordinates back to degrees
    pole_latitude = math.degrees(pole_latitude)
    pole_longitude = math.degrees(pole_longitude)

    return pole_latitude, pole_longitude


# Get user input
latitude = float(input("Enter the latitude in degrees: "))
longitude = float(input("Enter the longitude in degrees: "))
declination = float(input("Enter the declination in degrees: "))
inclination = float(input("Enter the inclination in degrees: "))

# Calculate the magnetic pole
pole_latitude, pole_longitude = calculate_magnetic_pole(latitude, longitude, declination, inclination)

# Display the results
print(f"The magnetic pole is located at latitude: {pole_latitude:.4f}°, longitude: {pole_longitude:.4f}°")
