def parse(file_text, indent):
	json_str = ""
	identation_close = {}
	last_identaions = 0
	num = 1
	for idx in range(len(file_text)):
		if '\n' in file_text[idx]:
			file_text[idx] = file_text[idx].replace('\n', '')
		identations = len(file_text[idx]) - len(file_text[idx].lstrip()) 
		
	
		if file_text[idx] == "---" or file_text[idx] == "...":
			continue
		json_str += ' '  * identations
		if file_text[idx].strip() == "-":
			json_str += str(num) + ':\n'
			num += 1
		else:
			if file_text[idx][-1] == ":":
				key = file_text[idx][:-1]
				value = ""
			elif ":" in file_text[idx]:
				key, value = file_text[idx].split(": ")
			else:
				key = ""
				value = file_text[idx].lstrip()[1:].lstrip()
			if "-" in key:
				key = key.lstrip()[1:].lstrip()
			key = key.lstrip()
			value = value.lstrip()
			if value == "":
				json_str += '' + str(key) + '' + ":"
			else:
				if "-" in file_text[idx]:
					if key == "":
						json_str += '' + str(value) + ''
					else:
						json_str += '' + str(key) + '' + ': ' + str(value) + ''
				else:
					json_str += '' + str(key) + '' + ': ' + str(value) + ''

		last_identaions = identations
		json_str += '\n'
	return json_str + "\n"

		

def main():
	filename = "saturday"
	with open(filename + ".yaml", "r", encoding="utf-8") as f:
		json = parse(f.readlines(), 2)
	write_filename = "saturday"
	with open(filename + ".txt", "w", encoding="utf-8") as f:
		f.write(json)

import time

start_time = time.time()
main()
print(time.time() - start_time)