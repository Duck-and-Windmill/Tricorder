import classifier

def main():
	with open("can.jpg") as can:

		model = classifier.model(can)

main()