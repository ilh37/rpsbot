import model
import sys

names = ['rock', 'paper', 'scissors']

def main():
	print('Welcome to Rock Paper Scissors!')
	print("Type 'r', 'p', or 's' for rock, paper, or scissors, or type 'q' to quit.") 

	m = model.RPSModel()
	wins, losses, ties = 0, 0, 0

	while True:
		print('> ', end='', flush=True)
		s = sys.stdin.readline().strip()

		n = None
		if s == 'r':
			n = 0
		elif s == 'p':
			n = 1
		elif s == 's':
			n = 2
		elif s == 'q':
			break
		elif s == 'x':
			print(m.unigrams)
			continue
		else:
			print('Please type a valid input.')
			continue		

		p = m.predict()
		m.update(n)

		print('The computer chooses', names[p])
		if (n-p) % 3 == 0:
			print('Tied!')
			ties += 1
		elif (n-p) % 3 == 1:
			print('You win!')
			wins += 1
		else:
			print('You lose!')
			losses += 1
	
	print('--------------')
	print('Score summary:')
	print('Wins:', wins, ', Losses:', losses, ', Ties:', ties)

if __name__ == '__main__':
	main()
