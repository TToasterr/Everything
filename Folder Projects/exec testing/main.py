cool = False

with open("script.txt", "r") as scriptfile:
    script = scriptfile.read()

exec(script)
if OWO:
    print("big boi")
print(output)
