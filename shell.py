import AlephNull

print("AlephNull 0.2")
print("AlephNull created 2020 by Eric Zou and the Arch-X Corporation.")
print("============Shell============")
while True:
    text = input('AlephNull>>>')
    result, error = AlephNull.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
input("Error detected. Press any key to exit...")
