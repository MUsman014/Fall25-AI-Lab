# List of films with title and cost
films = [
    ("The Dark Knight", 185000000),
    ("Interstellar", 165000000),
    ("Joker", 55000000),
    ("Avatar", 237000000),
    ("Titanic", 200000000),
    ("Frozen II", 150000000),
    ("Shutter Island", 80000000)
]

# Option to add more films
more = int(input("How many films do you want to add? "))

for i in range(more):
    title = input("Enter film title: ")
    cost = int(input("Enter film budget: "))
    films.append((title, cost))

# Calculate average budget
total_cost = sum(c for _, c in films)
avg_cost = total_cost / len(films)
print(f"\nAverage film budget: {avg_cost}")

# Films above average
print("\nFilms with budget above average:")
high_count = 0
for t, c in films:
    if c > avg_cost:
        gap = c - avg_cost
        print(f"- {t}: {c} (Above by {gap})")
        high_count += 1

# Print count
print(f"\nNumber of films above average: {high_count}")
