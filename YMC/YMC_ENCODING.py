# YMC Instruction Set Encoding

# Define opcodes (you can adjust these as needed)
OPCODES = {
    'mov': '0001',
    'add': '0100',
    'sub': '0101',
    'mult': '0110',
    'div': '0111',
    'cmp': '1000',
    'jg': '1010',
    'jmp': '1011',
    'loop': '1100'
}

# Define registers
REGISTERS = {
    'eax': '00',
    'ebx': '01',
    'ecx': '10',
    'edx': '11'
}

def encode_instruction(instruction):
    parts = instruction.split()
    opcode = parts[0].lower()

    if opcode in OPCODES:
        encoded_instruction = OPCODES[opcode]

        if opcode == 'mov':
            # Handle mov instructions
            dest_reg = REGISTERS[parts[1]]
            if parts[2].isdigit():
                # Immediate value
                immediate_value = format(int(parts[2]), '08b')
                encoded_instruction += dest_reg + immediate_value
            else:
                # Register-to-register
                src_reg = REGISTERS[parts[2]]
                encoded_instruction += dest_reg + src_reg
        elif opcode in ('add', 'sub', 'mult', 'div'):
            # Handle arithmetic instructions
            dest_reg = REGISTERS[parts[1]]
            op1_reg = REGISTERS[parts[2]]
            op2_reg = REGISTERS[parts[3]]
            encoded_instruction += dest_reg + op1_reg + op2_reg
        elif opcode == 'cmp':
            # Handle compare instruction
            op1_reg = REGISTERS[parts[1]]
            op2_reg = REGISTERS[parts[2]]
            encoded_instruction += op1_reg + op2_reg
        else:
            # Handle jumps and loops
            # (Assume label addresses will be resolved later)
            pass

        return encoded_instruction
    else:
        return None

# Example usage
if __name__ == "__main__":
    # Sample YMC instructions
    # instructions = [
    #     "mov ecx 3",
    #     "add ecx eax ebx",
    #     "cmp eax ecx",
    #     "jg label"
    # ]

    # for instr in instructions:
    #     encoded = encode_instruction(instr)
    #     if encoded:
    #         print(f"{instr} -> {encoded}")
    #     else:
    #         print(f"Invalid instruction: {instr}")
    
    instr = input("Enter YMC instruction: ")
    encoded = encode_instruction(instr)
    if encoded:
        print(f"{instr} -> {encoded}")
    else:
        print(f"Invalid instruction: {instr}")
