

questions=("where is india in asia","why nobita wants to marry sizuka","who is narendra modi")
answer=("south asia","life","prime minister")
i=0
k=0
loose=True
while( i < len(questions)):
    print(questions[i])
    z = (input("write your answer :"))

    while( k < len(answer)):



        if(z == answer[k]):
            print("10 lakh")
            i+=1
            k+=1
            loose=False
            break

        else:
            print("bye bye")
            loose=True
            break

    if(loose):
        print("you loose")
        break
















