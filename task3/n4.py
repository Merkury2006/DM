from task3.TuringMachine import TuringMachine


def simple_example(test=False):
    transitions1 = {
        ('q1', '1'): ('q2', '0', 'R'),
        ('q2', '1'): ('q3', '0', 'R'),
        ('q2', '0'): ('q0', '1', 'S'),
        ('q3', '0'): ('q0', '1', 'S'),
        ('q3', '1'): ('q0', '1', 'S'),
    }
    transitions2 = {  #Если должна все же зацикливаться
        ('q1', '1'): ('q2', '0', 'R'),
        ('q2', '1'): ('q3', '0', 'R'),
        ('q2', '0'): ('q2', '0', 'S'),
        ('q3', '0'): ('q3', '0', 'S'),
        ('q3', '1'): ('q0', '1', 'S'),
    }
    initial_state = 'q1'
    final_states = {'q0'}
    if not test:
        tape = "11"
        tm = TuringMachine(tape, initial_state, final_states, transitions2)

        print("Задание №3")
        print("=" * 40)

        tm.run(verbose=True)

        print("\nРезультат:")
        print(f'Вход: {" ".join([letter for letter in tape])}')
        print(f"Выход: {tm.get_tape_string()}")
    else:
        for x in range(100):
            tape = '1' * (x + 1)
            tm = TuringMachine(tape, initial_state, final_states, transitions2)
            tm.run()
            if (x == 0 or x == 1) and tm.get_tape_test().count('1') == 1:
                print(f"Тест с x={x} пройден")
            elif (x != 0 and x != 1 and tm.get_tape_test().count('1') == x - 1):
                print(f"Тест с x={x} пройден")

if __name__ == "__main__":
    simple_example(True)