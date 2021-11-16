

'''
[선언]
- getter, setter 함수 이름은 동일하게
- getter 먼저
- getter -> @proterty
  setter -> @함수이름.setter

[사용]
- 객체.함수() 이렇게 사용하면 안됨
- 객체 변수처럼 사용할것!
'''

class Person():

    def __init__(self):
        self._age = 0
        self._name = ""

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, _age):
        self._age = _age


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name



if __name__ == "__main__":
    ssong = Person()

    print(ssong.age)
    print(ssong.name)

    ssong.age = 29
    ssong.name = "송태영"

    print(ssong.age)
    print(ssong.name)
