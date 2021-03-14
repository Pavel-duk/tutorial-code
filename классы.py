class Voin():
    def __init__(self,damage=20,health=100,name='Вася',age=20,gun="нож"):
        self.name = name
        self.age = age
        self.gun = gun
        try:
            self.damage = int(input('урон'))
        except:
            self.damage = damage
            print('сработал')
        self.health = int(health)
        print("Воин", self.name, 'создан!')

    def __str__(self):
        return "Привет! меня зовут " + self.name + ", мне " + str(self.age) + ' лет и я мастерски владею оружием под названием ' + self.gun
    def rana(self,damage):
        self.health = self.health - damage
    def regeneration(self,count):
        self.health = self.health + int(count)
class Paladin(Voin):
    def __init__(self):
        super(Paladin,self).__init__()
        self.bronia = 10
    def rana(self,damage):
        self.health = self.health - (damage - damage*self.bronia/100)



voin1 = Voin()
voin2 = Voin(15,100,"Петя",20,"нож")
print(voin1)
print(voin2)

answer = 'да'
while True:

    voin2.rana(voin1.damage)
    voin1.rana(voin2.damage)
    print('У ' + voin1.name + ' осталось ' + str(voin1.health) + ' здоровья')
    print('У ' + voin2.name + ' осталось ' + str(voin2.health) + ' здоровья')



    if voin1.health <= 0 or voin2.health <= 0:
        if voin1.health <= 0:
            print('В битве победил ' + voin2.name)
        else:
            print('В битве победил ' + voin1.name)
        break
    answer = input("хотите сыграть еще раз?")
    if not answer == 'да':
        break

animals                 hosain
id type age name    id id_animal name age

select id,age,name from animals where type = "dog" and age > 5 ;
select hosain.id,animals.name from hosain left join animals on hosain.id_animal = animals.id
where type = "dog" and name = 'Петя'