print("30 Days Down - What do you think about your journey?")
print()
for i in range(1,31):
  thoughts = input(f"Day {i}:\n")
  print()
  response = f"You thought Day {i} was"
  print(f"{response:35}")
  print(f"{thoughts:35}")
  