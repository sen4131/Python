"""
Sen Varghese
Lab4
Chapter 5
"""

'''
5.14 Write function mult3() that takes as input a list of integers and prints only the multiples
of 3, one per line.
>>> mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])
'''
def mult3(lst):

	for i in lst:
		if i % 3 == 0:
			print(i)

mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])

'''
5.15 Implement the function vowels() that takes as input a string and prints the indexes of
all vowels in the string. Hint:Avowel can be defined as any character in string 'aeiouAEIOU
'''

def vowels(lst):
	
	x = 'aeiouAEIOU'
	for i,ch in enumerate(lst):
		if ch in x:
			print(i)

vowels('Hello WORLD')

'''
5.16 Implement function indexes() that takes as input a word (as a string) and a onecharacter
letter (as a string) and returns a list of indexes at which the letter occurs in the
word.
'''
def indexes(word,letter):
    l = []
    for i,ch in enumerate(word):
        if ch == letter:
            l.append(i)
    print(l)
	
indexes('mississippi', 's')

'''
5.18 Implement function four_letter() that takes as input a list of words (i.e., strings)
and returns the sublist of all four letter words in the list.
'''
def four_letter(lst):
	#lst = ['dog', 'letter', 'stop', 'door', 'bus', 'dust']
	newList = []
	for i in lst:
		if len(i) == 4:
			newList.append(i)
	print (newList)

four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust'])

'''
5.23 Write function pay() that takes as input an hourly wage and the number of hours an
employee worked in the last week. The function should compute and return the employee’s
pay. Overtime work should be paid in this way: Any hours beyond 40 but less than or equal
60 should be paid at 1.5 times the regular hourly wage. Any hours beyond 60 should be paid
at 2 times the regular hourly wage.
'''

def pay(wage,hours):
	
	pay = 0
	
	if  hours <= 40:
		pay += wage*hours
	elif hours > 40 and hours <= 60:
		pay += wage*40
		pay += wage*1.5*(hours-40)
	elif hours > 60:
		pay += wage*40
		pay += wage*1.5*20
		pay += wage*2*(hours-60)
	print(pay)

pay(10, 35)

'''
5.27 Write function letter2number() that takes as input a letter grade (A, B, C, D, F,
possibly with a 􀀀 or +) and returns the corresponding number grade. The numeric values
for A, B, C, D, and F are 4, 3, 2, 1, 0. A + increases the number grade value by 0.3 and a 􀀀
decreases it by 0.3.
'''

def letter2number(grade):

	gr = ('A','B','C','D','F')
	num = (4, 3, 2, 1, 0)
	GPA = 0
	
	for i,ch in enumerate(grade):
		if ch in gr:
			j = gr.index(ch)
			GPA += num[j]
		elif ch == '+':
			GPA += 0.3
		elif ch == '-':
			GPA -= 0.3

	print(GPA)

letter2number('A-')

