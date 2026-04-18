def check_str(str_to_check):
    queue = []
    for i in str_to_check.replace(" ", ""):
        if len(queue) != 0:

            if i in "({[":
                queue.append(i)

            elif i in ")]}":

                if (i == ")" and queue[-1] == "(") or (i == "]" and queue[-1] == "[") or (i == "}" and queue[-1] == "{"):
                    queue.pop()
                else:
                    print("не та скобка")
                    return False

            else:
                print("не скобка")
                return False

        else:
            if i in "]})":
                print("нет открывающей скобки")
                return False
            elif i not in "([{":
                print("не скобка")
                return False
            else:
                queue.append(i)

    if len(queue) != 0:
        print("нет закрывающей скобки")
        return False

    return True



