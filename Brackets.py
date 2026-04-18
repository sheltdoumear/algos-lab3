def check_str(str_to_check):
    queue = []
    for i in str_to_check:
        if len(queue) != 0:

            if i in "({[":
                queue.append(i)

            elif i in ")]}":

                if (i == ")" and queue[-1] == "(") or (i == "]" and queue[-1] == "[") or (i == "}" and queue[-1] == "{"):
                    queue.pop()
                else:
                    print("wrong bracket")
                    return False

            else:
                print("not a bracket")
                return False

        else:
            if i in "]})":
                print("no open bracket")
                return False
            elif i not in "([{":
                print("not a bracket")
                return False
            else:
                queue.append(i)

    if len(queue) != 0:
        print("no close bracket")
        return False

    return True

check_str("(){}[][")

