import string

my_str = "American.Gangster.2007.1080p.BluRay.x264.YIFY.mp4"
test_str = "hope it doesnt work .. ha"

found = my_str.find("YIFY")
not_found = test_str.find("YIFY")

if found != -1:
    print("HAPPY DAYS")
else:
    print("OH SHIT")
if my_str[-1] == "4":
    print("super happy")

if not_found == -1:
    print("HAPPY DAYS")

if test_str.find(" ") != -1:
    print("WHOOP")
elif test_str.find(" ") == -1:
    print("SHITTY")

bold = "\033[1m"
reset = "\033[0;0m"

print("I want " + bold + "this" + reset + " text to be bold.")

if my_str.find(" ") == -1:
    print("NO \033fucking SPACES")

un_str = test_str.replace(" ","_")
print(un_str)
