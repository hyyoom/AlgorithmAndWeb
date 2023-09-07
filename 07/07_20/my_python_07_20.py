
cnt = 0
user_list = []

def create_user(user):
    global cnt
    ret = is_validation(user)
    if ret == True:
        user_list.append(user)
    elif ret == 'blocked':
        cnt += 1
    elif bool(ret[0]) == False and ret[1] != []:
        cnt += 1
        for i in range(1, len(ret)):
            user[str(ret[i][0])] = None
        user_list.append(user)

def is_validation(user):
    boolean = True
    tmp = []
    ret = ()
    if user["company"] in black_list:
        return "blocked"
    if user['blood_group'] not in blood_types:
        tmp.append('blood_group')
        ret = (False, tmp)
    if "@" not in user["mail"]:
        tmp.append("mail")
        ret = (False, tmp)
    if len(user["name"]) < 2 and len(user["name"]) > 30:
        tmp.append("name")
        ret = (False, tmp)
    if len(user["website"]) < 1:
        tmp.append("website")
        ret = (False, tmp)
    if tmp == []:
        return boolean
    return ret


for user in user_data:
    create_user(user)

print(f"잘못된 데이터로 구성 된 유저의 수는 {cnt} 입니다 .")
for i in user_list:
    print(i)