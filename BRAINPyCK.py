class interpreter:
	def __init__(self, contents):
		self.text = contents
		self.splice = [c for c in self.text]
		self.bracemap = self.gen_brace('[', ']')
		self.comment_skipto = self.skipto('/', '/')
		self.function_skipto = self.skipto('$', '%')
		self.functions = {}
		self.memory = [None for x in range(30000)]
		self.out = []

	def gen_brace(start_char, end_char):
		temp_bracestack, bracemap = [], {}
		code = self.splice
		passed = None
		for position, command in enumerate(code):
			if command == start_char:
				temp_bracestack.append(position)
			elif command == end_char:
				start = temp_bracestack.pop()
				bracemap[start] = position
				bracemap[position] = start
		if len(temp_bracestack) != 0:
			return None	
		return bracemap

	def gen_skipto(start_char, end_char):
		temp_stack, skipto = [], {}
		code = self.splice
		idx = 0
		while idx < len(code):
			if code[idx] == start_char:
				if len(temp_stack) == 0:
					temp_stack.append(idx)
			if code[idx] == end_char:
				if len(temp_stack) == 1:
					start = temp_stack.pop()
					skipto[start] = idx
					skipto[idx] = start
		if len(temp_stack) != 0:
			return None
		return skipto



	def syntax(code):
		if self.bracemap != None and self.comment_skipto != None:
			idx = 0
			while idx < len(code):
				if code[idx] in [c for c in '><.,+-[]']:

				elif code[idx] == '$':
					char = code[idx + 1]
					end = code[idx+2:].index('%')
					if not self.vanilla(code[idx+2:end+idx+2]):
						return False
					self.functions[char] = ''.join(code[idx+2:end+idx+2])
					idx = end + idx + 2

				elif code[idx] == '/':
					idx = self.comment_skipto[idx]
				else:
					if code[idx] in self.functions.keys():
						pass
					else:
						return False

				idx += 1
			return True

	def interpret(predef_input=None, output_location='print'):
		code = self.cleanup(self.splice)
		if not self.syntax(code):
			return False

		for key in self.functions.keys():
			code.replace(key, self.functions[key])



		if predef_input != None:
			inp = [ord(c) for c in predef_input]
			inp_idx = 0

		idx = 0
		pointer = 0
		while idx < len(code):

			# +
			if code[idx] == '+':
				self.memory[pointer] += 1

			# - 
			elif code[idx] == '-':
				self.memory[pointer] -= 1

			# >
			elif code[idx] == '>':
				pointer += 1

			# <
			elif code[idx] == '<':
				pointer -= 1

			# [
			elif code[idx] == '[' and memory[pointer] == 0:
				idx = self.bracemap[idx]

			elif code[idx] == ']' and memory[pointer] != 0:
				idx = self.bracemap[idx]

			elif code[idx] == '.':
				if output_location == 'print':
					print(chr(self.memory[pointer]))
				elif output_location == 'self':
					self.out.append(chr(self.memory[pointer]))

			elif code[idx] == ',':
				if predef_input != None:
					try:
						self.memory[pointer] = inp[inp_idx]
					except IndexError:
						return False

					if inp_idx + 1 != len(inp):
						inp_idx += 1

			elif code[idx] == '/':
				idx = self.comment_skipto[idx]

			idx += 1

	def cleanup(code):
		op = code.replace(' ', '')
		for c in '\n\t\f\b\v':
			op.replace(c, '')
		return op

	def vanilla(code):
		for x in code:
			if x not in [c for c in '+-.,><[]']:
				return False
		return True

	def flush():
		self.memory = [None for x in range(30000)]
		self.out = []

	def new(code):
		self.__init__(code)










