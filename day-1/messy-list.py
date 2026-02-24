messy_list = [
	"  alice",
	"  BOB  ",
	"    chArLie ",
	" daisy ",
	"   EVE",
]

clean_list = [name.strip().capitalize() for name in messy_list]

for name in clean_list:
	print(f"You are invited, {name}!")
