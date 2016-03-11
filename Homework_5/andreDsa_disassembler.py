
# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"
}

Testlist= [
    901,
    309,
    901,
    109,
    000
]

def disassemble(operation_code):
    firstNumber = operation_code//100
    last2 = operation_code - 100*firstNumber
    lastString = ""
    if last2 < 10:
        lastString = "0" + str(last2)


    if firstNumber > 8 or firstNumber < 1:
        if firstNumber == 9 and last2 == 1:
            return str(operation_code) + ": " + "INP"

        elif firstNumber == 9 and last2 == 2:
            return str(operation_code) + ": " + "OUT"

        elif firstNumber == 0:
            return str(operation_code) + ": " + "HLT"

    return str(operation_code) + ": " + INS_REF[firstNumber] + " " +lastString

def main():
    print("Operation code to mnemonic dictionary")
    for i in range(0, len(Testlist)):
        print(i, disassemble(Testlist[i]))
        
main()
