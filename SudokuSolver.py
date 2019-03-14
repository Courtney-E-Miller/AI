import copy

# Returns a CSP containing a dictionary of variables and corresponding domains, and a list of constraints
def createCSP(filename):

    ## CREATES LIST OF NUMBERS REPRESNETING INITIAL VALUES FOR EACH SQUARE ###

    listOfNumbers = []
    fin = open(filename)

    # Takes in each line of input, splits it into singular strings representing numbers, and adds then to listOfNumbers
    for line in fin:
        nums = line.split(" ")
        listOfNumbers.extend(nums)

    # Removes all new lines from list
    for item in listOfNumbers:
        if item == '\n':
            listOfNumbers.remove(item)

    # For some reason, new line at end of file was not cooperating,
    # so this is a special condition to remove it
    if len(listOfNumbers) == 82:
        if listOfNumbers[81] == '\n':
            listOfNumbers.pop()

    # Casts  string representations of numbers to actual numbers
    listOfNumbers = list(map(int, listOfNumbers))


    ##  CREATES DICTIONARY WITH VARIABLES AND CORRESPONDING DOMAINS ##
    valueDomain = {}

    # List of all variables that will be iterated over to create dictionary
    allVar = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
              'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
              'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
              'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
              'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']

    for i in range(0, len(listOfNumbers)):
        # If the square is empty, make the domain ints 1 - 9
        if listOfNumbers[i] == 0:
            valueDomain[allVar[i]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # If the square is not empty, set the domain equal to the value of the square
        elif listOfNumbers[i] != 0:
            valueDomain[allVar[i]] = [listOfNumbers[i]]

    ## CREATES DICTIONARY WITH EACH VARIABLE AND THE CORRESPONDING VARIABLES IT CAN'T CONFLICT WITH ##
    constraints = {}

    # Creates list of constraining variables for each variable
    # PLEASE SCROLL QUICKLY THROUGH THE SHAME, IT SHOULD HELP MAKE CHECKING FOR CONSISTENCY EASIER LATER
    constraints['A1'] = ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1',
                         'B2', 'B3', 'C2', 'C3']
    constraints['A2'] = ['A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                         'B1', 'B3', 'C1', 'C3']
    constraints['A3'] = ['A1', 'A2', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3',
                         'B1', 'B2', 'C1', 'C2']
    constraints['A4'] = ['A1', 'A2', 'A3', 'A5', 'A6', 'A7', 'A8', 'A9', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4',
                         'B5', 'B6', 'C5', 'C6']
    constraints['A5'] = ['A1', 'A2', 'A3', 'A4', 'A6', 'A7', 'A8', 'A9', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5',
                         'B4', 'B6', 'C4', 'C6']
    constraints['A6'] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A7', 'A8', 'A9', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6',
                         'B4', 'B5', 'C4', 'C5']
    constraints['A7'] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A8', 'A9', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7',
                         'B8', 'B9', 'C8', 'C9']
    constraints['A8'] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A9', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8',
                         'B7', 'B9', 'C7', 'C9']
    constraints['A9'] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9',
                         'B7', 'B8', 'C7', 'C8']

    constraints['B1'] = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'A1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1',
                         'A2', 'A3', 'C2', 'C3']
    constraints['B2'] = ['B1', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'A2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                         'A1', 'A3', 'C1', 'C3']
    constraints['B3'] = ['B1', 'B2', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'A3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3',
                         'A1', 'A2', 'C1', 'C2']
    constraints['B4'] = ['B1', 'B2', 'B3', 'B5', 'B6', 'B7', 'B8', 'B9', 'A4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4',
                         'A5', 'A6', 'C5', 'C6']
    constraints['B5'] = ['B1', 'B2', 'B3', 'B4', 'B6', 'B7', 'B8', 'B9', 'A5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5',
                         'A4', 'A6', 'C4', 'C6']
    constraints['B6'] = ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B8', 'B9', 'A6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6',
                         'A4', 'A5', 'C4', 'C5']
    constraints['B7'] = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B8', 'B9', 'A7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7',
                         'A8', 'A9', 'C8', 'C9']
    constraints['B8'] = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B9', 'A8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8',
                         'A7', 'A9', 'C7', 'C9']
    constraints['B9'] = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'A9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9',
                         'A7', 'A8', 'C7', 'C8']

    constraints['C1'] = ['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'A1', 'B1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1',
                         'A2', 'A3', 'B2', 'B3']
    constraints['C2'] = ['C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                         'A1', 'A3', 'B1', 'B3']
    constraints['C3'] = ['C1', 'C2', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'A3', 'B3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3',
                         'A1', 'A2', 'B1', 'B2']
    constraints['C4'] = ['C1', 'C2', 'C3', 'C5', 'C6', 'C7', 'C8', 'C9', 'A4', 'B4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4',
                         'A5', 'A6', 'B5', 'B6']
    constraints['C5'] = ['C1', 'C2', 'C3', 'C4', 'C6', 'C7', 'C8', 'C9', 'A5', 'B5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5',
                         'A4', 'A6', 'B4', 'B6']
    constraints['C6'] = ['C1', 'C2', 'C3', 'C4', 'C5', 'C7', 'C8', 'C9', 'A6', 'B6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6',
                         'A4', 'A5', 'B4', 'B5']
    constraints['C7'] = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C8', 'C9', 'A7', 'B7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7',
                         'A8', 'A9', 'B8', 'B9']
    constraints['C8'] = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C9', 'A8', 'B8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8',
                         'A7', 'A9', 'B7', 'B9']
    constraints['C9'] = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'A9', 'B9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9',
                         'A7', 'A8', 'B7', 'B8']

    constraints['D1'] = ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'A1', 'B1', 'C1', 'E1', 'F1', 'G1', 'H1', 'I1',
                         'E2', 'E3', 'F2', 'F3']
    constraints['D2'] = ['D1', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'A2', 'B2', 'C2', 'E2', 'F2', 'G2', 'H2', 'I2',
                         'E1', 'E3', 'F1', 'F3']
    constraints['D3'] = ['D1', 'D2', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'A3', 'B3', 'C3', 'E3', 'F3', 'G3', 'H3', 'I3',
                         'E1', 'E2', 'F1', 'F2']
    constraints['D4'] = ['D1', 'D2', 'D3', 'D5', 'D6', 'D7', 'D8', 'D9', 'A4', 'B4', 'C4', 'E4', 'F4', 'G4', 'H4', 'I4',
                         'E5', 'E6', 'F5', 'F6']
    constraints['D5'] = ['D1', 'D2', 'D3', 'D4', 'D6', 'D7', 'D8', 'D9', 'A5', 'B5', 'C5', 'E5', 'F5', 'G5', 'H5', 'I5',
                         'E4', 'E6', 'F4', 'F6']
    constraints['D6'] = ['D1', 'D2', 'D3', 'D4', 'D5', 'D7', 'D8', 'D9', 'A6', 'B6', 'C6', 'E6', 'F6', 'G6', 'H6', 'I6',
                         'E4', 'E5', 'F4', 'F5']
    constraints['D7'] = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D8', 'D9', 'A7', 'B7', 'C7', 'E7', 'F7', 'G7', 'H7', 'I7',
                         'E8', 'E9', 'F8', 'F9']
    constraints['D8'] = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D9', 'A8', 'B8', 'C8', 'E8', 'F8', 'G8', 'H8', 'I8',
                         'E7', 'E9', 'F7', 'F9']
    constraints['D9'] = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'A9', 'B9', 'C9', 'E9', 'F9', 'G9', 'H9', 'I9',
                         'E7', 'E8', 'F7', 'F8']

    constraints['E1'] = ['E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'A1', 'B1', 'C1', 'D1', 'F1', 'G1', 'H1', 'I1',
                         'D2', 'D3', 'F2', 'F3']
    constraints['E2'] = ['E1', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'A2', 'B2', 'C2', 'D2', 'F2', 'G2', 'H2', 'I2',
                         'D1', 'D3', 'F1', 'F3']
    constraints['E3'] = ['E1', 'E2', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'A3', 'B3', 'C3', 'D3', 'F3', 'G3', 'H3', 'I3',
                         'D1', 'D2', 'F1', 'F2']
    constraints['E4'] = ['E1', 'E2', 'E3', 'E5', 'E6', 'E7', 'E8', 'E9', 'A4', 'B4', 'C4', 'D4', 'F4', 'G4', 'H4', 'I4',
                         'D5', 'D6', 'F5', 'F6']
    constraints['E5'] = ['E1', 'E2', 'E3', 'E4', 'E6', 'E7', 'E8', 'E9', 'A5', 'B5', 'C5', 'D5', 'F5', 'G5', 'H5', 'I5',
                         'D4', 'D6', 'F4', 'F6']
    constraints['E6'] = ['E1', 'E2', 'E3', 'E4', 'E5', 'E7', 'E8', 'E9', 'A6', 'B6', 'C6', 'D6', 'F6', 'G6', 'H6', 'I6',
                         'D4', 'D5', 'F4', 'F5']
    constraints['E7'] = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E8', 'E9', 'A7', 'B7', 'C7', 'D7', 'F7', 'G7', 'H7', 'I7',
                         'D8', 'D9', 'F8', 'F9']
    constraints['E8'] = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E9', 'A8', 'B8', 'C8', 'D8', 'F8', 'G8', 'H8', 'I8',
                         'D7', 'D9', 'F7', 'F9']
    constraints['E9'] = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'A9', 'B9', 'C9', 'D9', 'F9', 'G9', 'H9', 'I9',
                         'D7', 'D8', 'F7', 'F8']

    constraints['F1'] = ['F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'A1', 'B1', 'C1', 'D1', 'E1', 'G1', 'H1', 'I1',
                         'D2', 'D3', 'E2', 'E3']
    constraints['F2'] = ['F1', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'A2', 'B2', 'C2', 'D2', 'E2', 'G2', 'H2', 'I2',
                         'D1', 'D3', 'E1', 'E3']
    constraints['F3'] = ['F1', 'F2', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'A3', 'B3', 'C3', 'D3', 'E3', 'G3', 'H3', 'I3',
                         'D1', 'D2', 'E1', 'E2']
    constraints['F4'] = ['F1', 'F2', 'F3', 'F5', 'F6', 'F7', 'F8', 'F9', 'A4', 'B4', 'C4', 'D4', 'E4', 'G4', 'H4', 'I4',
                         'D5', 'D6', 'E5', 'E6']
    constraints['F5'] = ['F1', 'F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'A5', 'B5', 'C5', 'D5', 'E5', 'G5', 'H5', 'I5',
                         'D4', 'D6', 'E4', 'E6']
    constraints['F6'] = ['F1', 'F2', 'F3', 'F4', 'F5', 'F7', 'F8', 'F9', 'A6', 'B6', 'C6', 'D6', 'E6', 'G6', 'H6', 'I6',
                         'D4', 'D5', 'E4', 'E5']
    constraints['F7'] = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F8', 'F9', 'A7', 'B7', 'C7', 'D7', 'E7', 'G7', 'H7', 'I7',
                         'D8', 'D9', 'E8', 'E9']
    constraints['F8'] = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F9', 'A8', 'B8', 'C8', 'D8', 'E8', 'G8', 'H8', 'I8',
                         'D7', 'D9', 'E7', 'E9']
    constraints['F9'] = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'A9', 'B9', 'C9', 'D9', 'E9', 'G9', 'H9', 'I9',
                         'D7', 'D8', 'E7', 'E8']

    constraints['G1'] = ['G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'H1', 'I1',
                         'H2', 'H3', 'I2', 'I3']
    constraints['G2'] = ['G1', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'H2', 'I2',
                         'H1', 'H3', 'I1', 'I3']
    constraints['G3'] = ['G1', 'G2', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'H3', 'I3',
                         'H1', 'H2', 'I1', 'I2']
    constraints['G4'] = ['G1', 'G2', 'G3', 'G5', 'G6', 'G7', 'G8', 'G9', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'H4', 'I4',
                         'H5', 'H6', 'I5', 'I6']
    constraints['G5'] = ['G1', 'G2', 'G3', 'G4', 'G6', 'G7', 'G8', 'G9', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'H5', 'I5',
                         'H4', 'H6', 'I4', 'I6']
    constraints['G6'] = ['G1', 'G2', 'G3', 'G4', 'G5', 'G7', 'G8', 'G9', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'H6', 'I6',
                         'H4', 'H5', 'I4', 'I5']
    constraints['G7'] = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G8', 'G9', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'H7', 'I7',
                         'H8', 'H9', 'I8', 'I9']
    constraints['G8'] = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G9', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'H8', 'I8',
                         'H7', 'H9', 'I7', 'I9']
    constraints['G9'] = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'H9', 'I9',
                         'H7', 'H8', 'I7', 'I8']

    constraints['H1'] = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'I1',
                         'G2', 'G3', 'I2', 'I3']
    constraints['H2'] = ['H1', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'I2',
                         'G1', 'G3', 'I1', 'I3']
    constraints['H3'] = ['H1', 'H2', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'I3',
                         'G1', 'G2', 'I1', 'I2']
    constraints['H4'] = ['H1', 'H2', 'H3', 'H5', 'H6', 'H7', 'H8', 'H9', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'I4',
                         'G5', 'G6', 'I5', 'I6']
    constraints['H5'] = ['H1', 'H2', 'H3', 'H4', 'H6', 'H7', 'H8', 'H9', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'I5',
                         'G4', 'G6', 'I4', 'I6']
    constraints['H6'] = ['H1', 'H2', 'H3', 'H4', 'H5', 'H7', 'H8', 'H9', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'I6',
                         'G4', 'G5', 'I4', 'I5']
    constraints['H7'] = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H8', 'H9', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'I7',
                         'G8', 'G9', 'I8', 'I9']
    constraints['H8'] = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H9', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'I8',
                         'G7', 'G9', 'I7', 'I9']
    constraints['H9'] = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'I9',
                         'G7', 'G8', 'I7', 'I8']

    constraints['I1'] = ['I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
                         'H2', 'H3', 'G2', 'G3']
    constraints['I2'] = ['I1', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
                         'H1', 'H3', 'G1', 'G3']
    constraints['I3'] = ['I1', 'I2', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
                         'H1', 'H2', 'G1', 'G2']
    constraints['I4'] = ['I1', 'I2', 'I3', 'I5', 'I6', 'I7', 'I8', 'I9', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
                         'H5', 'H6', 'G5', 'G6']
    constraints['I5'] = ['I1', 'I2', 'I3', 'I4', 'I6', 'I7', 'I8', 'I9', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
                         'H4', 'H6', 'G4', 'G6']
    constraints['I6'] = ['I1', 'I2', 'I3', 'I4', 'I5', 'I7', 'I8', 'I9', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
                         'H4', 'H5', 'G4', 'G5']
    constraints['I7'] = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I8', 'I9', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
                         'H8', 'H9', 'G8', 'G9']
    constraints['I8'] = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I9', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
                         'H7', 'H9', 'G7', 'G9']
    constraints['I9'] = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9',
                         'H7', 'H8', 'G7', 'G8']
    ##  Creates initial CSP, with both dictionaries for the value and domain pairs, and the constraints for each variable ##
    initialCSP = [valueDomain, constraints]
    return initialCSP


# Returns a copy of a CSP
def copyCSP(originalCSP):
    # Creates copy of CSP
    cloneCSP = copy.deepcopy(originalCSP)
    return cloneCSP


# Takes in a child CSP, checks whether any of its assignments violate any of the constraints
# Returns 1 if none of the assignments violate the constraints, returns 0 if one of them does
def checkConstraints(childCSP):
    for variable in childCSP[0]:  # For variable in dictionary of variables and domains
        if len(childCSP[0][variable]) == 1:  # If the variable has been assigned
            for varConstraint in childCSP[1][variable]:  # for each variable in the list of constraints
                if childCSP[0][variable] == childCSP[0][varConstraint]:  # if they have the same domain
                    return 0  # Return 0 meaning one of the assignments violates the constraints

    return 1  # If its made it to the end, that means none of the assignments violate the constraints so we return 1


# Takes in a CSP and a variable that was just assigned a value, performs forward checking and either returns
# the forward checked CSP, or -1 if the forward checked CSP is inconsistent
def fowardCheck(cloneCSP, variable):
    # Should be a single numbre in domain at index 0, this is what we want to remove from the other domains
    varAssignment = cloneCSP[0][variable][0]

    # For each variable in the list of constraints
    for contraint in cloneCSP[1][variable]:

        # If constraint is not does not have an assigned value
        if len(cloneCSP[0][contraint]) > 1:

            # If varAssignment is in the domain of the constraint
            if varAssignment in cloneCSP[0][contraint]:

                # Removes varAssignment from domain
                cloneCSP[0][contraint].remove(varAssignment)

    # If the forward checked CSP is NOT consistent
    if checkConstraints(cloneCSP) == 0:
        return 0

    # Returns forward checked version of cloneCSP since it is consistent
    return cloneCSP


# # Takes in a CSP, generates all possible children, check whether each violates the constraints, and returns a list
# # of the children that don't violate the constraints.
# def generateChildren(originalCSP):
#     goodKids = []  # List of viable children
#     for variable in originalCSP[0]:  # For variable in dictionary of variables and domains
#         if len(originalCSP[0][variable]) > 1:  # If the variable has not been assigned
#             for possibleValue in originalCSP[0][variable]:  # For each possible value for variable
#                 cloneCSP = copyCSP(originalCSP)  # Creates a copy of the original CSP
#                 cloneCSP[0][variable] = [possibleValue]  # Sets domain of the variable to the possible value
#                 kosher = checkConstraints(cloneCSP)  # Checks to see if this assignment violates any of the constraints
#                 if kosher == 1:  # If the assignment doesn't violate any of the constraints
#                     goodKids.append(cloneCSP)  # Adds viable child to goodKids
#     return goodKids # returns list of viable children


# Takes in a CSP, generates all possible children, check whether each violates the constraints, and returns a list
# of the children that don't violate the constraints.
def generateChildren(originalCSP):
    goodKids = []  # List of viable children
    for variable in originalCSP[0]:  # For variable in dictionary of variables and domains
        if len(originalCSP[0][variable]) > 1:  # If the variable has not been assigned
            for possibleValue in originalCSP[0][variable]:  # For each possible value for variable
                cloneCSP = copyCSP(originalCSP)  # Creates a copy of the original CSP
                cloneCSP[0][variable] = [possibleValue]  # Sets domain of the variable to the possible value
                kosher = checkConstraints(cloneCSP)  # Checks to see if this assignment violates any of the constraints
                #print("Variable: ", variable, " , Assignment: ", possibleValue, sep='')
                #print(kosher)
                # for constraint in cloneCSP[1][variable]:
                #     print("Constriant: ", constraint, " , Domain: ", cloneCSP[0][constraint], sep='')
                if kosher == 1:  # If the assignment doesn't violate any of the constraints
                    fowardChecked = fowardCheck(cloneCSP, variable)  # Performs forward checking on child CSP
                    if fowardChecked != 0:  # If the forward checked version is consistent
                        goodKids.append(fowardChecked)  # Adds forward checked version of viable child to goodKids
    return goodKids  # returns list of viable children


# Takes in a CSP, checks to see if its a solution.  Returns 1 if it is a solution, returns 0 if it isn't a solution
def checkSolution(currentCSP):
    #print(currentCSP[0])
    for var in currentCSP[0]:  # For each variable in the dictionary
        if len(currentCSP[0][var]) > 1:  # If the size of the domain is greater than 1
            return 0  # Return 0 because at least one of the variables hasn't been assigned yet
    return 1  # Return 1 because all of the domains were of length one meaning the CSP is a solution


# Takes in a file, creates an original CSP, returns a list with (1)dictionary where the keys are the variables, and the
# values are the assigned values for said variable; and (2) the number of assignments made (including backtracking).
# If no solution is possible returns -1
def backtrack(filename):
    stack = []  # Creates list that will be used as a stack
    numAssignments = 0  # Creates variable to keep track of number of assignments
    originalCSP = createCSP(filename)  # Creates original CSP
    stack.append(originalCSP)  # Pushes original CSP to stack
    while len(stack) != 0:  # while the stack is not empty
        currentCSP = stack.pop()  # pops top CSP off stack
        if checkSolution(currentCSP) == 1:  # If the current CSP is a solution
            return [currentCSP[0], numAssignments]  # return a list containing the dictionary and number of assignments
        kiddos = generateChildren(currentCSP)  # Creates list of all viable children of current CSP
        if len(kiddos) != 0:  # If the list of children is not empty
            for kid in kiddos:  # For each child CSP in kiddos
                stack.append(kid)  # Add the kid to the stack
                numAssignments += 1  # Increment the number of assignments
    return -1  # If it exits the wile loop, that means the stack is empty and there is no solution

# Takes in a file name, runs search on problem, returns either a graphic of a solved grid and the number of assignments
# made, or it returns "No solution".
def main(filename):
    # Checks to see if there was no solution
    if backtrack(filename) == -1:
        return print("There is no solution to the Sudoku problem")

    # If there was an assignment
    solutionCSP, numAssinmed = backtrack(filename)

    # Prints the number of assignments made
    print("It took ", numAssinmed, " assignments to find the solution", sep='')

    # Creates grid visualization of sudoku results

    # Creates list that will contain solution values
    sol = []

    # Goes through the variables in the dictionary of variables and assigned values
    for var in solutionCSP:
        # Adds each solution to the list of solutions
        sol.append(solutionCSP[var][0])

    # Creates rows for printing out sudoku solution
    row1 = [sol[0], sol[1], sol[2], sol[3], sol[4], sol[5], sol[6], sol[7], sol[8]]
    row2 = [sol[9], sol[10], sol[11], sol[12], sol[13], sol[14], sol[15], sol[16], sol[17]]
    row3 = [sol[18], sol[19], sol[20], sol[21], sol[22], sol[23], sol[24], sol[25], sol[26]]
    row4 = [sol[27], sol[28], sol[29], sol[30], sol[31], sol[32], sol[33], sol[34], sol[35]]
    row5 = [sol[36], sol[37], sol[38], sol[39], sol[40], sol[41], sol[42], sol[43], sol[44]]
    row6 = [sol[45], sol[46], sol[47], sol[48], sol[49], sol[50], sol[51], sol[52], sol[53]]
    row7 = [sol[54], sol[55], sol[56], sol[57], sol[58], sol[59], sol[60], sol[61], sol[62]]
    row8 = [sol[63], sol[64], sol[65], sol[66], sol[67], sol[68], sol[69], sol[70], sol[71]]
    row9 = [sol[72], sol[73], sol[74], sol[75], sol[76], sol[77], sol[78], sol[79], sol[80]]

    allRows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    # Prints out matrix of solutions
    print("")
    print("       Sudoku Solution:        ")
    print("______________________________")
    for line in allRows:
        for number in line:
            if line.index(number) == 0:
                print("|", end='')
            print("%2d" % number, end=" ")
            if (line.index(number) - 2 )% 3 == 0:
                print("|", end='')
        print()
        if (allRows.index(line) - 2 )% 3 == 0:
            print("______________________________")


main('/Users/courtneymiller/Desktop/Artificial Intelligence/Assignment 3/problems/71/10.sd')




# part1 = {}
# part1['A1'] = [2]
# part1['A2'] = [2, 3, 4]
# part1['A3'] = [3]
#
# part2 = {}
# part2['A1'] = ['A2']
# part2['A2'] = ['A3']
# part2['A3'] = ['A1']
#
# fakeCSP = [part1, part2]
#
# test = fowardCheck(fakeCSP, 'A1')
#
# if test == 0:
#     print("the foward checked CSP was not consistent")
#
# else:
#     print("the foward checked CSP was consistent")







