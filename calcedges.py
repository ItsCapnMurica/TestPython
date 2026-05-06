# calculates edges

faces = int(input("How many faces?: "))
vertices = int(input("How many vertices?: "))

edges = faces + vertices - 2

print(f"There are {edges} edges")