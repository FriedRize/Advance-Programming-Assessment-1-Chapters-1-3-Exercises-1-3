# Create a dictionary with film data
film_data = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Sci-Fi",
    "Rating": 8.8
}

# Display the film details using a loop
print("Film Details:")
for key, value in film_data.items():
    print(f"{key}: {value}")