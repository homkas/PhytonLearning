class SortedSetList():
    def __init__(self, sorted_order):
        self.container = []
        self.sorted_order = sorted_order

    def __repr__(self):
        return self.container


    def add_new_items(self, n):
        while n > 0:
            n -= 1
            i = float(input("Введите число: "))
            if i not in self.container:
                self.container.append(i)


    def get_some_max_elements(self, n):
        additional_list = self.container.copy()
        max_list = []
        while n > 0:
            n -= 1
            i = max(additional_list)
            additional_list.remove(i)
            max_list.append(i)
        print(str(len(max_list)) + " максимальн.знач.: " + " , ".join([str(i) for i in max_list]))


    def get_some_min_elements(self, n):
        additional_list = self.container.copy()
        min_list = []
        while n > 0:
            n -= 1
            i = min(additional_list)
            additional_list.remove(i)
            min_list.append(i)
        print(str(len(min_list)) + " минимальн.знач.: " + " , ".join([str(i) for i in min_list]))


    def convert_list_to_dict(self):
        additional_list = []
        n = len(self.container)
        while n > 0:
            n -= 1
            additional_list.append(n+1)
        additional_list.reverse()
        my_dict = dict(zip(additional_list, self.container))
        return my_dict


    def get_element_by_index(self, n):
        if n > len(self.container):
            print("Номер превышает длину списка!!!")
        elif n == 0:
            print("Номер должен быть больше 0!!!")
        else:
            return self.convert_list_to_dict().get(n)


    def delete_last_element(self):
        self.container.pop()


    def delete_first_element(self):
        self.container.pop(0)


    def delete_element_by_index(self, n):
        if n > len(self.container):
            print("Номер превышает длину списка!!!")
        elif n == 0:
            print("Номер должен быть больше 0!!!")
        else: self.container.pop(n-1)




my_list = SortedSetList(False)
my_list.add_new_items(5)
print(my_list.__repr__())
my_list.delete_last_element()
print(my_list.__repr__())
my_list.delete_first_element()
print(my_list.__repr__())
my_list.delete_element_by_index(1)
print(my_list.__repr__())













