from collections import defaultdict
import operator, random, os

count_reg=defaultdict(int)
count_pb=defaultdict(int)
data={}

def get_num():
    r_fname = input('Enter your first name:')
    r_lname = input('Enter your last name:')
    full_name=str(r_fname+' '+r_lname)
    r_1st = input('select 1st # (1 thru 69):')
    r_1st=int(r_1st)

    while r_1st<1 or r_1st>69:
        r_1st=input('select 1st # (1 thru 69):')
        r_1st=int(r_1st)

    r_2nd=input('select 2nd # (1 thru 69 excluding {}):'.format(r_1st))
    r_2nd=int(r_2nd)

    while r_2nd<1 or r_2nd>69 or r_2nd==r_1st:
        r_2nd=input('select 2nd # (1 thru 69 excluding {}):'.format(r_1st))
        r_2nd=int(r_2nd)

    r_3rd=input('select 3rd # (1 thru 69 excluding {} and {}):'.format(r_1st, r_2nd))
    r_3rd=int(r_3rd)

    while r_3rd<1 or r_3rd>69 or r_3rd==r_1st or r_3rd==r_2nd:
        r_3rd=input('select 3rd # (1 thru 69 excluding {} and {}):'.format(r_1st, r_2nd))
        r_3rd=int(r_3rd)

    r_4th=input('select 4th # (1 thru 69 excluding {}, {} and {}):'.format(r_1st, r_2nd, r_3rd))
    r_4th=int(r_4th)

    while r_4th<1 or r_4th>69 or r_4th==r_1st or r_4th==r_2nd or r_4th==r_3rd:
        r_4th=input('select 4th # (1 thru 69 excluding {}, {} and {}):'.format(r_1st, r_2nd, r_3rd))
        r_4th=int(r_4th)

    r_5th=input('select 5th # (1 thru 69 excluding {}, {}, {} and {}):'.format(r_1st, r_2nd, r_3rd, r_4th))
    r_5th=int(r_5th)

    while r_5th<1 or r_5th>69 or r_5th==r_1st or r_5th==r_2nd or r_5th==r_3rd or r_5th==r_4th:
        r_5th=input('select 5th # (1 thru 69 excluding {}, {}, {} and {}):'.format(r_1st, r_2nd, r_3rd, r_4th))
        r_5th=int(r_5th)

    r_pb = input('select Power Ball # (1 thru 26):')
    r_pb=int(r_pb)

    while r_pb<1 or r_pb>26:
        r_pb = input('select Power Ball # (1 thru 26):')
        r_pb=int(r_pb)

    for i in [r_1st, r_2nd, r_3rd, r_4th, r_5th]:
        if count_reg[i]:
            count_reg[i]+=1
        else:
            count_reg[i]=1

    if count_pb[r_pb]:
        count_pb[r_pb]+=1
    else:
        count_pb[r_pb]=1

    data[full_name] = [r_1st, r_2nd, r_3rd, r_4th, r_5th, r_pb]

def get_pb():

    print('PB winning number collector\n')

    get_num()

    r_another = input('Do you want to enter another set of PB #? Enter y or n:')

    while True:
        if r_another.lower() == 'y':
            get_num()
            r_another = input('Do you want to enter another set of PB #? Enter Y or N:')
        elif r_another.lower() == 'n':
            break
        else:
            r_another = input('Can not recognize your input. \n\nDo you want to enter another set of PB #? Enter Y or N:')
        
    pb_list = sorted(count_pb.items(), key=operator.itemgetter(1), reverse=True)
    pb_pb=pb_list[0][0]
##    if pb_list[0][1] != pb_list[1][1]:
##        pb_pb=pb_list[0][0]
##    else:
##        pb_bag = []
##        pb_bag.extend([pb_list[0][0], pb_list[1][0]])
##        for i, (k, v) in enumerate(pb_list):
##            if v == pb_list[i+2][1]:
##                pb_bag.append(pb_list[i+2][0])
##            else:
##                break
##        pb_pb=random.choice(pb_bag)

    pb_num_list = sorted(count_reg.items(), key=operator.itemgetter(1), reverse=True)

    pb_reg=[]

    for i in [pb_num_list[0], pb_num_list[1], pb_num_list[2], pb_num_list[3], pb_num_list[4]]:
        pb_reg.append(i[0])

    return pb_reg, pb_pb

def main():

    pb_reg, pb_pb = get_pb()

    for k, v in data.items():
        print('\n{} {} Powerball: {}\n'.format(k, v[0:5], v[5]))

    print('Powerball winning number:\n\n{} Powerball: {}'.format(pb_reg, pb_pb))


main()

os.system('pause')
