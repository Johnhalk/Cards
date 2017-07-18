class Value(object):
    
    def __init__(self):
        self.value = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']


    def add_value(self, value_type):
        if value_type.upper() not in self.value:
            self.value.append(value_type.upper())
        else:
            print "Value already exists."

    def delete_value(self, value_type):
        if value_type.upper() in self.value:
            self.value.remove(value_type.upper())
            return self.value
        else:
            print "Not a valid value."
