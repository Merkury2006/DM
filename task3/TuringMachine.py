class TuringMachine:
        def __init__(self, tape, initial_state, final_states, transition_functions, blank_symbol='0'):
            self.tape = list(tape)                         #Лента
            self.head_position = 0                         #Указатель головки
            self.current_state = initial_state             #Текущее состояние
            self.final_states = final_states               #Множество конечных состояний
            self.transition_functions = transition_functions #Таблица переходов
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
                raise Exception(f"Машина Тьюринга не применима к данному слову. Машина Тьюринга выполнила максимальное кол-во шагов({self.max_steps})")



            key = (self.current_state, self.get_current_symbol())  #Формируем ключ для нашей таблицы переходов

            if key not in self.transition_functions:
               return False

            new_state, new_symbol, direction = self.transition_functions[key]  #Достаем значение из таблицы переходов по ключу

            self.tape[self.head_position] = new_symbol  # Изменяем символ нашей ленты

            self.current_state = new_state  # Делаем переход в новое состояние
            self.step_count += 1

            if direction == 'R':  # По направлению меняем указатель головки
                self.head_position += 1
            elif direction == 'L':
                self.head_position -= 1
            elif direction == 'S':
                self.head_position = self.head_position

            if self.head_position >= len(self.tape):  #Динамически расширяем ленту, если индекс вышел за пределы списка (лента МТ бесконечна)
                self.tape.append(self.blank_symbol)
            elif self.head_position < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head_position = 0
            return True

        def run(self, verbose=False): #Флаг verbose отвечает за логи
            if verbose:
                print(f"Начальное состояние: состояние УУ={self.current_state}, начальное слово= {self.get_tape_string()}")
                print(f"указатель головки={self.head_position + 1}" + "\n")
            try:
                while self.step(): #Будет выполняться до конечного состояния или зацикливания
                    if verbose:
                        print(f"Шаг {self.step_count + 1}: состояние УУ={self.current_state}, текущее слово= {self.get_tape_string()}")
                        print(f"указатель головки={self.head_position + 1}" + "\n")
                if verbose:
                    if self.current_state not in self.final_states:
                        print(f"Перехода ({self.current_state},{self.get_current_symbol()}) нет в программе Машины Тьюринга")
                    else:
                        print(f"Машина Тьюринга достигла своего заключительного состояния: {self.current_state}")
                    print("Машина Тьюринга применима к данному слову")
                    print(f"T(P) = {self.get_tape_string().rstrip(self.blank_symbol)}")


                    index = 0
                    for x in self.tape:
                        if x != self.blank_symbol:
                            break
                        index += 1
                    if (self.head_position < index + 1):
                        print("Машина Тьюринга правильно вычисляет f(x)")


                    self.tape.insert(self.head_position, self.current_state)
                    print(f"Заключительное состояние: {' '.join(self.tape)}")
            except Exception as e:
                if verbose:
                    print(f"Ошибка: {e}")

        def get_tape_string(self):
            result = " ".join(self.tape)
            return result if result else self.blank_symbol

        def get_tape_test(self):
            return self.tape