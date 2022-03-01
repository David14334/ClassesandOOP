class procedure:

    def __init__(self, name, date, practname, charge, id):
        self.__name = name
        self.__date = date
        self.__practname = practname
        self.__charge = charge
        self.__id = id


    def get_name(self): 
        return self.__name

    def get_date(self): 
        return self.__date
    
    def get_practname(self): 
        return self.__practname

    def get_charge(self): 
        return self.__charge
    
    def get_id(self): 
        return self.__id