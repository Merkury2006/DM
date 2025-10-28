from task3.TuringMachine import TuringMachine


def simple_example(test=False):
    transitions = {
        ('q1', '1'): ('q2', '0', 'R'),
        ('q2', '1'): ('q2', '1', 'R'),
        ('q2', '0'): ('q3', '0', 'R'),
        ('q3', '0'): ('q4', '1', 'R'),
        ('q4', '0'): ('q5', '1', 'L'),
        ('q5', '1'): ('q5', '1', 'L'),
        ('q5', '0'): ('q6', '0', 'L'),
        ('q6', '1'): ('q6', '1', 'L'),
        ('q6', '0'): ('q1', '0', 'R'),
        ('q3', '1'): ('q3', '1', 'R'),
        ('q1', '0'): ('q0', '0', 'R'),
    }
    initial_state = 'q1'
    final_states = {'q0'}
    if not test:
        tape = "1111111"
        tm = TuringMachine(tape, initial_state, final_states, transitions)

        print("Задание №3")
        print("=" * 40)

        tm.run(verbose=True)

        print("\nРезультат:")
        print(f'Вход: {" ".join([letter for letter in tape])}')
        print(f"Выход: {tm.get_tape_string()}")
    else:
        for x in range(100):
            tape = '1' * (x + 1)
            tm = TuringMachine(tape, initial_state, final_states, transitions)
            tm.run()
            if (tm.get_tape_test().count('1') == 2 * x + 2):
                print(f"Тест с x={x} пройден")

if __name__ == "__main__":
    simple_example()