class Value(object):
    def __init__(self):
        self.value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


    def add_value(self, value_type):
        self.value.append(value_type)

    def delete_value(self):
        print "The values are:", self.value
        remove_value = raw_input('Which value do you want to remove?')
        if remove_value in self.value:
            self.value.remove(remove_value)
            return self.value
        else:
            print "Not a valid value"

'''
value_new=Value()
print value_new.value
value_new.add_value('Joker')
print value_new.value

value_new.delete_value()
print value_new.value
'''
