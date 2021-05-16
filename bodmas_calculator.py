
def solve(calculation):
    Operator_Precedence = {"^": 4, "/": 3, "*": 2, "+": 1, "-": 1}
    Operator_Index = [] 

    for i in range(len(calculation)):
        if calculation[i] in Operator_Precedence:
            if len(Operator_Index) == 0: 
                Operator_Index.append(i)
            else: 
             for x in range(len(Operator_Index)): 

                    if Operator_Precedence[calculation[i]] < Operator_Precedence[calculation[Operator_Index[-1]]]:
                        Operator_Index.append(i)
                        break

                    elif Operator_Precedence[calculation[i]] > Operator_Precedence[calculation[Operator_Index[x]]]:
                        Operator_Index.insert(x, i) 
                        break

                    elif Operator_Precedence[calculation[i]] == Operator_Precedence[calculation[Operator_Index[x]]]:
                        if calculation[i] == "+" or calculation[i] == "-":
                            Operator_Index.append(i)
                            break
                        else:
                            Operator_Index.insert(x + 1, i)
                            break
                            
                    else:
                        continue

    while len(Operator_Index) != 0:

        if calculation[Operator_Index[0]] == '^':
            calculation_result = calculation[Operator_Index[0] - 1] ** calculation[Operator_Index[0] + 1]

        elif calculation[Operator_Index[0]] == '/':
            calculation_result = calculation[Operator_Index[0] - 1] / calculation[Operator_Index[0] + 1]

        elif calculation[Operator_Index[0]] == '*':
            calculation_result = calculation[Operator_Index[0] - 1] * calculation[Operator_Index[0] + 1]

        elif calculation[Operator_Index[0]] == '+':
            calculation_result = calculation[Operator_Index[0] - 1] + calculation[Operator_Index[0] + 1]

        else:
            calculation_result = calculation[Operator_Index[0] - 1] - calculation[Operator_Index[0] + 1]

        calculation[Operator_Index[0]-1] = calculation_result
        calculation.pop(Operator_Index[0]+1)
        calculation.pop(Operator_Index[0])

        for i in range(len(Operator_Index)):
            if Operator_Index[i] > Operator_Index[0]:
                Operator_Index.insert(i, Operator_Index[i] - 2)
                Operator_Index.pop(i + 1)

        Operator_Index.pop(0)

    return calculation[0]


def Bracket_pair(calculation):

    Start_Array = []
    End_Array = []
    _Pairs = {}

    for i in range(len(calculation)):
        if calculation[i] == '(':
            Start_Array.append(i)
        elif calculation[i] == ')':
           End_Array.append(i)




    for i in range(len(Start_Array) - 1, -1, -1):
        for x in range(len(End_Array)):
            if End_Array[x] < Start_Array[i] or End_Array[x] in _Pairs.values():
                continue
            else:
                _Pairs[Start_Array[i]] = End_Array[x]
                break
        break
    if len(_Pairs) != 0:
        return _Pairs


def  _Calculator(calculation):
    brackets = Bracket_pair(calculation)
    answer = []

    if brackets is None :
        return float(solve(calculation))
    else:
        Start_Index= list(brackets.keys())[0]
        End_Index = brackets[Start_Index]
        answer.append(solve(calculation[Start_Index+ 1:End_Index]))
        calculation = calculation[:Start_Index] + answer + calculation[End_Index + 1:]
        #print(calculation)
        return  _Calculator(calculation)


def calc_input():

    cal_array = []
    calculation = input('Enter your expression: ')
    _num = ""

    for i in range(len(calculation)):

       
        if calculation[i].isnumeric() or calculation[i] == ".":
            _num = _num + calculation[i]

            if i == len(calculation)-1:
               cal_array.append(float(_num))
        else:

            if _num == "":
               cal_array.append(calculation[i])
            
            else:
               cal_array.append(float(_num))
               cal_array.append(calculation[i])
               _num = ""

    return  _Calculator(cal_array)


answer = calc_input()
print(answer)
