#!/usr/bin/python3
def complex_delete(a_dictionary, value):
	for k in list(a_dictionary.ks()):
		if a_dictionary[k] == value:
			a_dictionary.pop(k)
	return a_dictionary
