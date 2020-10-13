n= int(input())
my_dict = {}
for i in range((n*(n-1))//2):
    mylist = []
    x, y, z = input().split()
    mylist.append(x)
    mylist.append(y)
    mylist.append(z)
    first_t=mylist[0]
    second_t = mylist[1]
    first_t_score = mylist[2][0]
    second_t_score = mylist[2][2]
    if first_t_score<second_t_score:
        scorefinalfirst=0
        scorefinalsecond =3
        if (first_t=='A' and second_t=='B') or (first_t=='B' and second_t=='C') or (first_t=='A' and second_t=='C'):
            if first_t in my_dict:
                my_dict[first_t] += 0
            else:
                my_dict[first_t]= 0
            if second_t in my_dict:
                my_dict[second_t] += 3
            else:
                my_dict[second_t] = 3

    elif first_t_score == second_t_score:
        if (first_t == 'A' and second_t == 'B') or (first_t == 'B' and second_t == 'C') or (
                first_t == 'A' and second_t == 'C'):
            if first_t in my_dict:
                my_dict[first_t] += 1
            else:
                my_dict[first_t] = 1
            if second_t in my_dict:
                my_dict[second_t] += 1
            else:
                my_dict[second_t] = 1
    else:
        scorefinalfirst = 3
        scorefinalsecond=0

        if (first_t == 'A' and second_t == 'B') or (first_t == 'B' and second_t == 'C') or (first_t == 'A' and second_t == 'C'):
            if first_t in my_dict:
                my_dict[first_t] += 3
            else:
                my_dict[first_t] = 3
            if second_t in my_dict:
                my_dict[second_t] += 0
            else:
                my_dict[second_t] = 0
Keymax = max(my_dict, key=my_dict.get)
print(Keymax,my_dict[Keymax])
