class Value(object):
    def __init__(self):
        self.value = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']


    def add_value(self):
        print "The current values are:", self.value
        value_type = raw_input('Which value do you want to add? ')
        if value_type not in self.value:
            self.value.append(value_type.upper())
        else:
            print "Value already exists."

    def delete_value(self):
        print "The values are:", self.value
        remove_value = raw_input('Which value do you want to remove? ')
        if remove_value.upper() in self.value:
            self.value.remove(remove_value.upper())
            return self.value
        else:
            print "Not a valid value"



'''
value_new=Value()
print value_new.value
value_new.add_value()
print value_new.value

value_new.delete_value()
print value_new.value
'''
