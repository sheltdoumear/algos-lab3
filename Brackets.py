def check_str(str_to_check):
    stack = []
    for i in str_to_check.replace(" ", ""):
        if len(stack) != 0:

            if i in "({[":
                stack.append(i)

            elif i in ")]}":

                if (i == ")" and stack[-1] == "(") or (i == "]" and stack[-1] == "[") or (i == "}" and stack[-1] == "{"):
                    stack.pop()
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
                stack.append(i)

    if len(stack) != 0:
        print("нет закрывающей скобки")
        return False

    return True



