# class ASTNode:
#     def __init__(self, type, value=None, children=None):
#         self.type = type
#         self.value = value
#         self.children = children if children is not None else []

# # Sample HLC code
# hlc_code = """
# unsigned a, b, c
# signed x, y, z

# a = 3
# b = 15 + a
# c = b * a / 10

# x = -5
# y = 13

# if c <= 10:
#     x = y + 10
# else:
#     x = y - 20

# while y > 0:
#     print y
#     y = y - 1
# """

# # Variable to register mapping
# variable_registers = {
#     'a': 'eax',
#     'b': 'ebx',
#     'c': 'ecx',
#     'x': 'edx',
#     'y': 'esi',  # Using esi for y in this example
#     'z': 'edi',  # Using edi for z in this example
# }
# def parse_statement(tokens):
#     if not tokens:
#         return
#     token = tokens[0]
#     print(f"{token}")
#     if token[0] == 'VAR':
#         return parse_variable_declaration(tokens)
#     elif token[0] == 'DATATYPE':
#         return parse_variable_declaration(tokens)
#     elif token[0] == 'KEYWORD':
#         if token[1] == 'if':
#             return parse_if_else(tokens)
#         elif token[1] == 'else':
#             tokens.pop(0)  # Consume 'else' token    
#         elif token[1] == 'while':
#             return parse_while(tokens)
#         elif token[1] == 'print':
#             return parse_print(tokens)
#     elif token[0] == 'PUNCTUATION':
#         if token[1] == '{':
#             return parse_block(tokens)
#         elif token[1] == ';':
#             tokens.pop(0)  # Consume ';' token for empty statement
#             return None
#         elif token[1] == '}':
#             return None  # Consume '}' token
#         else:
#             return parse_assignment(tokens)

# def parse(code):
#     tokens = tokenize(code)
#     statements = []
#     while tokens:
#         statement = parse_statement(tokens)
#         if statement:
#             statements.append(statement)
#     return ASTNode('PROGRAM', children=statements)
# # Tokenize and parse HLC code into AST
# def parse_hlc(hlc_code):
#     lines = hlc_code.split('\n')
#     lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines and whitespace
#     ast_root = ASTNode('program')
#     for line in lines:
#         tokens = line.split()
#         if len(tokens) >= 3 and tokens[1] == '=':
#             # Assignment statement
#             var_name = tokens[0].strip(',')  # Remove any trailing commas
#             expr = ' '.join(tokens[2:])
#             assignment_node = ASTNode('assignment', (var_name, expr))
#             ast_root.children.append(assignment_node)
#         elif tokens[0] == 'if':
#             # Conditional statement
#             cond_expr = ' '.join(tokens[1:])
#             conditional_node = ASTNode('conditional', cond_expr)
#             ast_root.children.append(conditional_node)
#         elif tokens[0] == 'while':
#             # Loop statement
#             cond_expr = ' '.join(tokens[1:])
#             loop_node = ASTNode('loop', cond_expr)
#             ast_root.children.append(loop_node)
#         elif tokens[0] == 'print':
#             # Print statement
#             var_name = tokens[1]
#             print_node = ASTNode('print', var_name)
#             ast_root.children.append(print_node)
#         else:
#             # Variable declaration
#             var_names = [var.strip(',') for var in tokens[1:]]  # Remove trailing commas from variable names
#             var_decl_node = ASTNode('variable_declaration', var_names)
#             ast_root.children.append(var_decl_node)
#     return ast_root

# # Generate YMC code from AST
# def generate_ymc_code(ast_root):
#     ymc_code = []

#     def traverse(node):
#         nonlocal ymc_code
#         if node.type == 'variable_declaration':
#             # Replace variable names with register names
#             var_names = ', '.join([f"{variable_registers[var]}" for var in node.value])
#             ymc_code.append(f"Declare variables: {var_names}")
#         elif node.type == 'assignment':
#             var_name, expr = node.value
#             # Replace variable name with register name
#             var_reg = variable_registers[var_name]
#             # Replace variable names in expressions with register names
#             for var, reg in variable_registers.items():
#                 expr = expr.replace(var, reg)
#             # Convert operators to YMC instructions
#             expr = expr.replace('+', 'ADD').replace('-', 'SUB').replace('*', 'MUL').replace('/', 'DIV')
#             ymc_code.append(f"mov {var_reg}, {expr}")
#         elif node.type == 'conditional':
#             ymc_code.append(f"If {node.value}:")
#         elif node.type == 'loop':
#             ymc_code.append(f"While {node.value}:")
#         elif node.type == 'print':
#             ymc_code.append(f"Print {node.value}")

#         # Traverse children nodes
#         for child in node.children:
#             traverse(child)

#     traverse(ast_root)
#     return ymc_code
# ymc_instructions = {
#     'mov': '0001',
#     'add': '0100',
#     'sub': '0101',
#     'mul': '0110',
#     'div': '0111',
#     # Add more YMC instructions here as needed
# }

# register_codes = {
#     'eax': '00',
#     'ebx': '01',
#     'ecx': '10',
#     'edx': '11',
#     # Add more register codes here as needed
# }

# # Convert YMC assembly code to machine code
# def convert_to_machine_code(ymc_code):
#     machine_code = []
#     for instruction in ymc_code:
#         parts = instruction.split()
#         opcode = ymc_instructions.get(parts[0], '0000')  # Default to 0000 if instruction not found
#         operands = ' '.join(parts[1:])
#         # Replace register names with register codes in operands
#         for reg_name, reg_code in register_codes.items():
#             operands = operands.replace(reg_name, reg_code)
#         machine_code.append(f"{opcode} {operands}")
#     return machine_code
# # Tokenize and parse HLC code into AST
# ast_root = parse_hlc(hlc_code)

# # Generate YMC code from AST
# ymc_code = generate_ymc_code(ast_root)

# # Print the generated YMC code with register codes
# # for instruction in ymc_code:
# #     print(instruction)
# machine_code = convert_to_machine_code(ymc_code)

# # Print the generated machine code
# for code in machine_code:
#     print(code)
# # 







import csv
import os
# Define AST node classes
class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

# Define YMC instructions, binary encodings, and register codes
ymc_instructions = {
    'mov': 'mov',
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div',
    '<=': 'cmp_le',
    '>=': 'cmp_ge',
    '==': 'cmp_eq',
    '!=': 'cmp_ne',
    'jle': 'jle',
    'jge': 'jge',
    'je': 'je',
    'jne': 'jne',
    'jmp': 'jmp',
    'loop': 'loop',
    'Declare': 'DECLARE',  # Updated mapping for Declare statement
    'Print': 'print'
}

binary_encodings = {
    'mov': '0001',
    'add': '0100',
    'sub': '0101',
    'mul': '0110',
    'div': '0111',
    'cmp_le': '1000',
    'cmp_ge': '1001',
    'cmp_eq': '1010',
    'cmp_ne': '1011',
    'jle': '1100',
    'jge': '1101',
    'je': '1110',
    'jne': '1111',
    'jmp': '1110',  # Placeholder for JMP instruction
    'loop': '0110',  # Placeholder for LOOP instruction
    'DECLARE': '0000',  # Placeholder for DECLARE instruction
    'PRINT': '0000'  # Placeholder for PRINT instruction
}

register_codes = {
    'eax': '00',
    'ebx': '01',
    'ecx': '10',
    'edx': '11'
}

# Define AST node classes
class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

# Sample HLC code
hlc_code = """
unsigned a, b, c
signed x, y, z

a = 3
b = 15 + a
c = b * a / 10

x = -5
y = 13

if c <= 10:
    x = y + 10
else:
    x = y - 20

while y > 0:
    print y
    y = y - 1
"""

variable_registers = {
    'a': 'eax',
    'b': 'ebx',
    'c': 'ecx',
    'x': 'edx',
    'y': 'esi',
    'z': 'edi',
}

# Tokenize and parse HLC code into AST
def parse_hlc(hlc_code):
    lines = hlc_code.split('\n')
    lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines and whitespace
    ast_root = ASTNode('program')
    for line in lines:
        tokens = line.split()
        if len(tokens) >= 3 and tokens[1] == '=':
            # Assignment statement
            var_name = tokens[0].strip(',')  # Remove any trailing commas
            expr = ' '.join(tokens[2:])
            assignment_node = ASTNode('assignment', (var_name, expr))
            ast_root.children.append(assignment_node)
        elif tokens[0] == 'if':
            # Conditional statement
            cond_expr = ' '.join(tokens[1:])
            conditional_node = ASTNode('conditional', cond_expr)
            ast_root.children.append(conditional_node)
        elif tokens[0] == 'while':
            # Loop statement
            cond_expr = ' '.join(tokens[1:])
            loop_node = ASTNode('loop', cond_expr)
            ast_root.children.append(loop_node)
        elif tokens[0] == 'print':
            # Print statement
            var_name = tokens[1]
            print_node = ASTNode('print', var_name)
            ast_root.children.append(print_node)
        else:
            # Variable declaration
            var_names = [var.strip(',') for var in tokens[1:]]  # Remove trailing commas from variable names
            var_decl_node = ASTNode('variable_declaration', var_names)
            ast_root.children.append(var_decl_node)
    return ast_root

# Generate YMC code from AST
def generate_ymc_code(ast_root):
    ymc_code = []

    def traverse(node):
        nonlocal ymc_code
        if node.type == 'variable_declaration':
            # Replace variable names with register names
            var_names = ', '.join([f"{variable_registers[var]}" for var in node.value])
            ymc_code.append(f"Declare variables: {var_names}")
        elif node.type == 'assignment':
            var_name, expr = node.value
            # Replace variable name with register name
            var_reg = variable_registers[var_name]
            # Replace variables within expressions with register codes
            for var in variable_registers:
                expr = expr.replace(var, variable_registers[var])
            # Convert operators to YMC instructions
            expr = expr.replace('+', 'add').replace('-', 'sub').replace('*', 'mul').replace('/', 'div')
            ymc_code.append(f"mov {var_reg}, {expr}")
        elif node.type == 'conditional':
            ymc_code.append(f"If {node.value}:")
        elif node.type == 'loop':
            ymc_code.append(f"While {node.value}:")
        elif node.type == 'print':
            ymc_code.append(f"Print {node.value}")

        # Traverse children nodes
        for child in node.children:
            traverse(child)

    traverse(ast_root)
    return ymc_code

# Generate machine code (binary encoding) from YMC code
def generate_machine_code(ymc_code):
    machine_code = []
    ymc_address = 1000  # Starting YMC address
    for instruction in ymc_code:
        parts = instruction.split()
        opcode = parts[0]
        operands = ' '.join(parts[1:])
        ymc_encoding = binary_encodings.get(opcode, '0000')  # Default to 0000 if instruction not found
        machine_code.append({
            'YMC Address': f"{ymc_address}",
            'YMC assembly': instruction,
            'YMC encoding': ymc_encoding,
            'Modified registers': '',  # Placeholder for modified registers
            'Modified flags': ''  # Placeholder for modified flags
        })
        ymc_address += 4  # Increment YMC address by 4 bytes for each instruction
    return machine_code

def write_processor_states(machine_code, filename='processor_states.csv', download_path=None):
    if download_path:
        filepath = os.path.join(download_path, filename)
    else:
        filepath = filename

    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ['HLC instruction', 'YMC Address', 'YMC assembly', 'YMC encoding', 'Modified registers', 'Modified flags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for instruction in machine_code:
            writer.writerow({
                'HLC instruction': '',  # Placeholder for HLC instruction
                'YMC Address': instruction['YMC Address'],
                'YMC assembly': instruction['YMC assembly'],
                'YMC encoding': instruction['YMC encoding'],
                'Modified registers': instruction['Modified registers'],
                'Modified flags': instruction['Modified flags']
            })

# Define the download path
download_path = ''

# Tokenize and parse HLC code into AST
ast_root = parse_hlc(hlc_code)

# Generate YMC code from AST
ymc_code = generate_ymc_code(ast_root)

# Generate machine code from YMC code
machine_code = generate_machine_code(ymc_code)

# Write processor states to CSV file
write_processor_states(machine_code, download_path=download_path)

print(f"Processor states CSV file saved")