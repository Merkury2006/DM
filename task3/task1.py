from task3.TuringMachine import TuringMachine

def simple_example():
    transitions = {
        ('q1', '0'): ('q2', '1', 'R'),
        ('q1', '1'): ('q2', '1', 'L'),
        ('q2', '0'): ('q3', '1', 'R'),
        ('q2', '1'): ('q3', '0', 'R'),
        ('q3', '1'): ('q1', '1', 'R')
    }
    tape = "111011"
    initial_state = 'q1'
    final_states = {'q0'}

    tm = TuringMachine(tape, initial_state, final_states, transitions)

    print("Задание №1")
    print("=" * 40)

    tm.run(verbose=True)

    print("\nРезультат:")
    print(f'Вход: {" ".join([letter for letter in tape])}')
    print(f"Выход: {tm.get_tape_string()}")




if __name__ == "__main__":
    simple_example()