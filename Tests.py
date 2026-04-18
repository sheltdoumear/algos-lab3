import Brackets
from Brackets import check_str

check_str("")          # -> True
check_str("()[]{}")    # -> True
check_str("{}]")       # -> False, нет открывающей скобки
check_str("[](")       # -> False, нет закрывающей скобки
check_str("{[}]")      # -> False, не та скобка
check_str("{}g")       # -> False, не скобка