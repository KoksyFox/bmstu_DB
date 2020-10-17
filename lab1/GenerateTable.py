from faker import Faker
from random import randint
from random import sample
from random import choice

MAX_N = 1000
N = 1000

sex = ['m', 'f']
cardType = ['standart', 'gold', 'platinum']


def generate_people():
    faker = Faker()
    cardId = [i for i in range(N, N + MAX_N)]
    cardId = sample(cardId, MAX_N)
    IDpeople = [i for i in range(1, MAX_N+1)]
    IDpeople = sample(IDpeople, MAX_N)
    
    f = open('people.csv', 'w')
    for i in range(MAX_N):
        age = randint(14, 99)
        line = "{0},{1},{2},{3},{4}\n".format(
                                                  IDpeople[i],
                                                  cardId[i],
                                                  faker.last_name(),
                                                  choice(sex),
                                                  age)
        f.write(line)
    f.close()

def generate_cards():
    faker = Faker()
    f = open('cards.csv', 'w')
    idCard = [i for i in range(N, N + MAX_N)]
    idCard = sample(idCard, MAX_N)

    idGym = [i for i in range(MAX_N)]
    idGym = sample(idGym, MAX_N)
    for i in range(MAX_N):
        line = "{0},{1},{2},{3}\n".format(
                                                  idCard[i],
                                                  idGym[i],                                                  
                                                  choice(cardType),
                                                  faker.date_this_year())
        f.write(line)
    f.close()                                          


def generate_gyms():
    faker = Faker() 
    f = open('gyms.csv', 'w')
    idGym = [i for i in range(1,MAX_N+1)]
    idGym = sample(idGym, MAX_N)
    
    for i in range(MAX_N):
        line = "{0},{1},{2}\n".format(idGym[i],
                                      faker.first_name(),
                                      faker.street_address())
        f.write(line)
        
    f.close()


if __name__ == "__main__":
    generate_cards()
    generate_people()
    generate_gyms()