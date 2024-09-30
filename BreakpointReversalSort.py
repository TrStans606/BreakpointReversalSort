import copy
import random
def BreakpointReversalSort (input_list):
	step = 0
	breakpoints = BreakPointFinder(input_list)
	while len(breakpoints) > 1 or breakpoints[0][0] == "-":
		breakpoints = BreakPointFinder(input_list)
		first_index = 0 
		last_index = 0

		if len(breakpoints) > 1:
			min_breakpoints = len(breakpoints)
			min_first_index = 0
			min_last_index = 0
			for x in range(len(input_list)-1):
				for y in range(x+1,len(input_list)):
					clone_list = copy.deepcopy(input_list)
					first_index = x
					last_index = y
					storage = clone_list[first_index:last_index+1]
					for z in range(first_index,last_index+1):
						clone_list[z] = storage.pop()					
					test_breakpoints =  BreakPointFinder(clone_list)
					if len(test_breakpoints) < min_breakpoints:
						min_breakpoints = len(test_breakpoints)
						min_first_index = first_index
						min_last_index = last_index
			if min_breakpoints == len(breakpoints):
				for x in range(len(breakpoints)):
					if breakpoints[x][0] == '+':
						min_first_index = input_list.index(breakpoints[x][1][0])
						min_last_index = input_list.index(breakpoints[x][1][len(breakpoints[x][1])-1])
				if min_breakpoints == len(breakpoints):
					if breakpoints[x][0] == '-':
						min_first_index = input_list.index(breakpoints[x][1][0])
						min_last_index = input_list.index(breakpoints[x][1][len(breakpoints[x][1])-1])			
			step += 1
			print(f'Step {step}')
			print(f'Input: {input_list}')
			print(BreakPointFinder(input_list))
			storage = input_list[min_first_index:min_last_index+1]
			print(f'Section to be flipped {storage}')
			for x in range(min_first_index,min_last_index+1):
				input_list[x] = storage.pop()
			print(f'Output: {input_list}')
			print(BreakPointFinder(input_list))
		
		if len(breakpoints) == 1 and breakpoints[0][0] == "-":
			step += 1
			print(f'Step {step}')
			print(f'Input: {input_list}')
			print(BreakPointFinder(input_list))
			first_index = input_list.index(breakpoints[0][1][0])
			last_index = input_list.index(breakpoints[0][1][len(breakpoints[0][1])-1])
			storage = input_list[first_index:last_index+1]
			for x in range(first_index,last_index+1):
				input_list[x] = storage.pop()
			print(f'Output: {input_list}')
			print(BreakPointFinder(input_list))
	return input_list

def BreakPointFinder(input_list):
	breakpoints = []
	i = 0
	x = 0
	while x < len(input_list):
		contig = True
		breakpoints.append(['+',[input_list[x]]])
		j=x
		while contig and j < len(input_list)-1 :
			if abs(input_list[j] - input_list[j+1]) == 1:
				breakpoints[i][1].append(input_list[j+1])
				x += 1
			else:
				i += 1
				contig = False
			j += 1
		x += 1
	for x in range(len(breakpoints)):
		if len(breakpoints[x][1]) > 1 and breakpoints[x][1][0] > breakpoints[x][1][1]:
			breakpoints[x][0] = '-'
	return breakpoints

test = list(range(50))
print(test)
random.shuffle(test)

print(f'The starting list is {test}')

final = BreakpointReversalSort(test)

print(f'The final list is {final}')	