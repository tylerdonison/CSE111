import math

def main():
  name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
  
  radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
  
  height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
  
  cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

  max_storage_efficiency = 0
  max_cost_efficiency = 0
  for i in range(0,12):
    volume = cylinder_volume(radius[i], height[i])
    
    surface_area = cylinder_surface_area(radius[i], height[i])
    
    storage_efficiency = compute_storage_efficiency(volume, surface_area)

    cost_efficiency = compute_cost_efficiency(volume, cost[i])
    
    print(f"{name[i]:15} {storage_efficiency:10.2f} {cost_efficiency:10.2f}")

    if storage_efficiency > max_storage_efficiency:
      max_storage_efficiency = storage_efficiency
      max_storage_name = name[i]

    if cost_efficiency > max_cost_efficiency:
      max_cost_efficiency = cost_efficiency
      max_cost_name = name[i]

  print(f"The best storage efficiency is {max_storage_efficiency:.2f} from can {max_storage_name:}.")
  print(f"The best cost efficiency is {max_cost_efficiency:.2f} from can {max_cost_name:}.")
  

def cylinder_volume(radius, height):
  volume = math.pi * (radius ** 2) * height
  return volume

def cylinder_surface_area(radius, height):
  return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
  return volume / surface_area

def compute_cost_efficiency(volume, cost):
  return volume / cost

main()