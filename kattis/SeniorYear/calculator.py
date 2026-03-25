while True:
    try:
        eq = input()
        print(f'{eval(eq):.2f}')
    except EOFError:
        break