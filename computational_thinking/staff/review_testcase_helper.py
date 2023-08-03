from string import ascii_lowercase

def str_to_idx_list(da_str: str):
    li = []
    for char in da_str:
        li.append(ascii_lowercase.index(char))
    return li

if __name__ == '__main__':
    print(str_to_idx_list("amp"))
    print(str_to_idx_list("csone"))
    print(str_to_idx_list("python"))
    print(str_to_idx_list("helloworld"))
    print(str_to_idx_list("a"))
    print(str_to_idx_list("z"))
    print(str_to_idx_list(""))
    print("banana", str_to_idx_list("banana"))
    
