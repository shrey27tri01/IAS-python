'''
Test the IAS machine 
This implements the addition and multiplication of two numbers 
To test the machine, install python and make sure that both the IAS.py and test.py are in the same folder
Then run the following commands in the terminal in the directory where the files are stored
- pip3 install -r requirements.txt
- python3 test.py
'''



'''
- addition -
0000:   0000 0001   0000 0000 0010    : load data at address 2 into AC
0001:   0000 0101   0000 0000 0011    : add data at address 3 to the AC
0010:   0010 0001   0000 0000 0100    : store value in AC to address 4
'''

'''
- multiplication -
0000:   0000 1001   0000 0000 0010    : load data from address 2 into MQ
0001:   0000 1011   0000 0000 0011    : mul data at address 3
0010:   0010 0001   0000 0000 0101    : store value from AC into address 5
'''

from IAS import IAS

#each process contains a series of instructions containing 8-bit opcode and 12-bit address
adddition = [['00000001','000000000010'],['00000101','000000000011'],['00100001','000000000100']]
multiplication = [['00001001','000000000010'],['00001011','000000000011'],['00100001','000000000101']]

ias = IAS()

#provide two input values
ias.input('000000000011', 10)
ias.input('000000000010', 20)

for instruction in adddition:
    ias.instruction(instruction[0], instruction[1])

#addition result
print(f"Result of addition: {ias.read('000000000100')}")
print("----")

for instruction in multiplication:
    ias.instruction(instruction[0], instruction[1])

#multiplication result
print(f"Result of multiplication: {ias.read('000000000101')}")
print("----")

