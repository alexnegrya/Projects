# data
plane_altitude = 500    # meters
plane_speed    = 300    # km/hours
free_lane      = True
wind_speed     = 30     # km/hours
plane_direction = True  # the coincidence of the direction of the plane with the direction of the wind
plane_fuel = 50         # % of fuel
plane_bad_condition = False

# logic 
can_land = plane_altitude >= 100 and plane_speed >= 200\
    and free_lane and wind_speed <= 100 and plane_direction\
    or plane_fuel < 1 or plane_bad_condition

# view
print("Plane altitude:",plane_altitude,"m")
print("Plane speed:",plane_speed,"km/h")
print("Is a free lane at airport?",free_lane)
print("Wind speed:",wind_speed,"km/h")
print("The direction of the plane coincides with the direction of the wind?",plane_direction)
print("Plane fuel:",plane_fuel,"%")
print("The plane is in bad condition?",plane_bad_condition)
print("Can the plane land?",can_land)