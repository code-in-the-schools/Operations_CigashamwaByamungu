annual_rainfall_2019 = annual_rainfall_2019

January_rainfall_2019 = 3.15
february_rainfall_2019 = 3.64
march_rainfall_2019 = 4.14

winter_rainfall_2019 = january_rainfall_2019 + february_rainfall_2019 + march_rainfall_2019
avg_winter_rainfall_2019 = winter_rainfall_2019 / 3

print("The total winter rainfall is", winter_rainfall_2019, "inches.")
print("The average winter rainfall is",avg_winter_rainfall_2019, "inches.")

annual_rainfall_2019 += winter_rainfall_2019