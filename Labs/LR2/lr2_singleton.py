class Singleton(object):
    def __new__(cls): #специальный метод для создания объектов
        if not hasattr(cls, 'instance'): #Проверяет наличие у объекта cls свойства instance.
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)