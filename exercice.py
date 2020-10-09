#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import math

def get_fibonacci_number(indice):
	return (
		0 if indice == 0
		else 1 if indice == 1
		else get_fibonacci_number(indice - 1) + get_fibonacci_number(indice - 2)
	)


def get_fibonacci_sequence(taille): #Avec cette méthode, on regénère la suite à chaque fois, donc pas optimal
	return [get_fibonacci_number(indice) for indice in range(0, taille)]


def get_sorted_dict_by_decimals(dictValues): #Utiliser une fct lambda et sorted()
	#Même chose mais en plusieurs lignes
	# def decPart(n):
	# 	return n % 1.0
	#
	# return sorted(dictValues.values(), key = decPart)

	#La solution
	return dict(sorted(dictValues.items(), key = lambda t: t[1] % 1.0))

	#Mon pathetic attempt
	# inverseDict = {}
	# for key in dictValues:
	# 	inverseDict[dictValues[key]] = key
	#
	# decPartDict = {}
	# for key in inverseDict:
	# 	decPartDict[round(key % math.floor(key), 5)] = key
	#
	# decParts = [key for key in decPartDict]
	# decParts.sort()
	#
	# for decPart in decParts:
	# 	originalValue = decPartDict[decPart]
	# 	originalKey = inverseDict[originalValue]
	# 	sortedDict[originalKey] = originalValue

def fibonacci_numbers(length):
	INIT_VALUES = [0, 1, 1]
	seq = deque(INIT_VALUES)
	#Retourner les 2 premiers éléments pas récursifs
	for i in range(0, length):
		if i >= length:
			break
		if i < len(INIT_VALUES):
			yield INIT_VALUES[i]
		else:
			yield seq[-2] + seq[-1]
			seq.append(seq[-2] + seq[-1])
			seq.popleft()

def build_recursive_sequence_generator(INIT_VALUES, seqDef, keepInMemory = False):
	seq = deque(INIT_VALUES)
	i = 0
	while True:
		if i < len(INIT_VALUES):
			yield INIT_VALUES[i]
		else:
			nextValue = seqDef(seq)
			if keepInMemory:
				seq.append(nextValue)
			else:
				seq.append(nextValue)
				seq.popleft()
			yield nextValue
		i += 1


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}

	# def longueur(s):
	# 	return len(s)
	# foo = ["aaa", "bb", "c"]
	# print(sorted(foo))
	# print(sorted(foo, key = longueur))

	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for i in range(0, 10):
		print(next(fibo), end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2, 1], lambda lastElems: lastElems[-1] + lastElems[-2])
	print(f"Lucas : {[next(lucas) for i in range(0, 10)]}")

	perrin = build_recursive_sequence_generator([3, 0, 2], lambda lastElems: lastElems[-2] + lastElems[-3])
	print(f"Perrin : {[next(perrin) for i in range(0, 10)]}")

	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda lastElems: lastElems[-lastElems[-1]] + lastElems[-lastElems[-2]], keepInMemory=True)
	print(f"Hofstadter-Q : {[next(hofstadter_q) for i in range(0, 10)]}")
