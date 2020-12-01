import re

def greeting():
    print('*************************************************')
    print('**         Welcome To The Madlib Game          **')
    print('*************************************************')
    print('*************************************************')
    print('**                                             **')
    print('**You will have to answer some question and the**')
    print('**     Answers will be replaced with some      **') 
    print('**        Words in a random paragraph          **')
    print('**                                             **')
    print('***********        Have Fun       ***************')
    print('*************************************************')


def readTemplate(path):
    with open(path, 'r') as file:
        content = file.read()
        file.close()
        return content.strip()
   

def parse(cont,ask_for_input=True):
    counter=1
    modified_data=[]
    data = re.findall(r"\{(.*?)\}",cont)
    print(f'For This Game You Will Be Asked {len(data)} Qustion\n')

    if ask_for_input ==True:
        for i in data:
            user_input=input(f'{counter}) Please Insert {i} \n')
            modified_data.append(user_input)   
            counter+=1
    else:
        return data

    return modified_data


def merge(modified_data,cont):
    f=0
    data = re.findall(r"\{(.*?)\}",cont)

    for i in modified_data:
        cont=cont.replace(data[f],i,1)
        f+=1

    cont=cont.replace('{','')
    cont=cont.replace('}','')

    with open('assets/user_input.txt', 'w') as input_content:
        input_content.write(cont)

    print('**************')
    return cont

if __name__ == "__main__":
    content=readTemplate('assets/message.txt')

    greeting()
    print(f'{merge(parse(content),content)}\n')

