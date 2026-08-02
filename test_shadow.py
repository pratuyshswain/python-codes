import wish
print("Imported:", wish.__file__ if hasattr(wish, "__file__") else "builtin")
try:
    print(wish.strftime("%H"))
except AttributeError as e:
    print("Error:", e)
