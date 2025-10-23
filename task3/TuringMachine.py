class TuringMachine:
        def __init__(self, tape, initial_state, final_states, transition_function, blank_symbol='0'):
            self.tape = list(tape)                         #Лента
            self.head_position = 0                         #Указатель головки
            self.current_state = initial_state             #Текущее состояние
            self.final_states = final_states               #Множество конечных состояний
            self.transition_function = transition_function #Таблица переходов
            self.blank_symbol = blank_symbol               #Пустой символ

            self.step_count = 0
            self.max_steps = 100000

            if len(self.tape) == 0:
                self.tape.append(blank_symbol)


        def get_current_symbol(self): #Получаем текущий символ МТ
            if 0 <= self.head_position < len(self.tape): #Если в нашем слове, то возвращаем текущий символ, иначе пустой символ
                return self.tape[self.head_position]
            return self.blank_symbol

        def step(self): #Выполнение одного шага МТ
            if self.current_state in self.final_states: #Проверяем, не в конечном ли мы состоянии
                return False

            if self.step_count >= self.max_steps:      #Также делаем проверку на зацикливание
                raise Exception(f"МТ выполнила максимальное кол-во шагов({self.max_steps})")



            key = (self.current_state, self.get_current_symbol())  #Формируем ключ для нашей таблицы переходов

            if key not in self.transition_function:
                return False
            new_state, new_symbol, direction = self.transition_function[key]  #Достаем значение из таблицы переходов по ключу

            if self.head_position < len(self.tape):                #Изменяем символ нашей ленты
                self.tape[self.head_position] = new_symbol
            else:
                self.tape.append(new_symbol)

            if direction == 'R':            #По направлению меняем указатель головки
                self.head_position += 1
            elif direction == 'L':
                self.head_position -= 1

            if self.head_position >= len(self.tape):  #Динамически расширяем ленту, если индекс вышел за пределы списка (лента МТ бесконечна)
                self.tape.append(self.blank_symbol)
            elif self.head_position < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head_position = 0

            self.current_state = new_state  #Делаем переход в новое состояние
            self.step_count += 1
            return True

        def run(self, verbose=False): #Флаг verbose отвечает за логи
            if verbose:
                print(f"Start: state={self.current_state}, tape={self.get_tape_string()}")
            while self.step(): #Будет выполняться до конечного состояния или зацикливания
                if verbose:
                    print(f"Step: {self.step_count}: state={self.current_state}, tape = {self.get_tape_string()}")
            if verbose:
                print(f"Final: state={self.current_state}, tape={self.get_tape_string()}")


        def get_tape_string(self):
            tape_str = "".join(self.tape)
            result = tape_str.rstrip(self.blank_symbol)
            return result if result else self.blank_symbol