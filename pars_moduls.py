import re

print('-----------Calculator----------')
print('available operastions: +,-,*,/ ')
fake=True
while fake:
    row_str=input("Введите последовательность действий,\nНапример:20-5*2 enter, результат будет равен 30: ")
    expr_row=re.findall(r'.',row_str)
    expr_clean=re.findall(r'[0-9,\+\-\/\*\.]', row_str)
    operations=re.findall(r'[\+\-\/\*]',row_str)
    fake_op=re.findall(r'[\+\/\-\*][+/*\-]',row_str)
    fake_op2=re.findall(r'[.][+/*\-]',row_str)
    if len(expr_row)!=len(expr_clean) or len(fake_op)>0 or len(fake_op2)>0:
        fake=True
    else:
        fake=False

operations.append('=')
expr_clean.append('=')
# print(expr_row,expr_clean, 'len_row_str',len(row_str))
# print('fake_op',fake_op)
# print(operations)
# print('fake=',fake)

if fake:
    exit()

j=0
value=[]
i=0
str_=''
while i<len(operations):
    while expr_clean[j]!=operations[i]:
        # print('str=',str_)
        str_+=expr_clean[j]
        j+=1

    value.append(str_)
    # print('str_=', str_, 'i= ', i, 'len op=', len(operations), 'op i=', operations[i], 'j=', j)
    i += 1
    j+=1
    str_=''

# print(value)



values=value
operators=operations

len_op=len(operators)
print(values)
print(operators)

i=0
z=0
result=0
while i<len_op-1:
    while z<len(values):
        if operators[i]=='+':
            result=float(values[z])+float(values[z+1])
            values[z+1]=result
            # print('value',z,'=',values[z],'value',z+1,'=',values[z+1], 'operator=',operators[z], 'result=',result)
            # print(values)
            z+=1
            i+=1
            break
        elif operators[i]=='-':
            result = float(values[z]) - float(values[z + 1])
            values[z + 1] = result
            # print('value', z, '=', values[z], 'value', z + 1, '=', values[z + 1], 'operator=', operators[z], 'result=',
            #       result)
            # print(values)
            z += 1
            i+=1
            break
        elif operators[i] == '/':
            try:
                result = float(values[z]) / float(values[z + 1])
                values[z + 1] = result
                # print('value', z, '=', values[z], 'value', z + 1, '=', values[z + 1], 'operator=', operators[z], 'result=',
                #       result)
                # print(values)
                z += 1
                i += 1
                break
            except:
                z += 1
                i += 1
                print('Ошибка деления на 0')

                break
        elif operators[i]=='*':
            result = float(values[z]) * float(values[z + 1])
            values[z + 1] = result
            # print('value', z, '=', values[z], 'value', z + 1, '=', values[z + 1], 'operator=', operators[z], 'result=',
            #       result)
            # print(values)
            z += 1
            i += 1
            break

print('result=',result)

