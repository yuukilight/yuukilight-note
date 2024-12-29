from show import A

def main():
    # a_normal_1 = A(1, 1.3, 'hello', [1,2], {'a': 1, 'b': 2})
    a_normal_1 = A.get_nromal_instance()
    # ===
    a2 = A(1, 1.3, 'world', [3,4], {'a': 3, 'b': 4})
    # ===
    a3 = A(2, 2.3, 'world', [5,6], {'a': 5, 'b': 6})

    # ===
    a_normal_2 = A.get_nromal_instance()

    print(a_normal_1)

if __name__ == '__main__':
    main()