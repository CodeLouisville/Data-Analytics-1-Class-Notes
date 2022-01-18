age = input("How old are you?")
decades = int(age) // 10  # integer division
years = age % 10  # modulus division (get remainder)

print("You are " + str(decades) + " decades and " + str(years) + " years old.")
