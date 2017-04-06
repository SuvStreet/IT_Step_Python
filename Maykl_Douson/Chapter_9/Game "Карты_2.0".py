# Карты 2.0 
# Демонстрирует расширение класса  через наследование

class Card(object): 
    """ Одна  игральная  карта. """
    RANKS = ["T", "2", "З", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К"] # атрибут возможных значений у карт 
    SUIТS = ["♣", "♦", "♥", "♠"] # атрибут, предстовляющий масть карты (♣ - трефы; ♦ - бубны; ♥ - червы; ♠ - пики)
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit 
    def __str__(self): 
        rep = self.rank + self.suit
        return rep
    
class Hand(object): 
    """ 'Рука': набор карт на руках у одного игрока. """
    def __init__ (self):
            self.cards = []
    def __str__ (self):
        if self.cards:
            rep = " "
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep
    def clear(self): # очистить
        self.cards = []
    def add(self, card): # добавить
        self.cards.append(card)
    def give(self, card, other_hand): # дать
        self.cards.remove(card)
        other_hand.add(card)
        
class Deck(Hand):
    """ Колода игральных карт. """
    def populate(self): # заполнение 
        self.cards = []
        counter = 0 # в вожу счётчик
        for suit in Card.SUIТS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
                counter += 1
                if counter % 13 == 0: # как только счётчик делит число 13 без остатка
                    self.add('\n')    # вывод переносит на новую строку
    def shuffle(self): # перетосовать
        import random 
        random.shuffle(self.cards) 
    def deal(self, hands, per_hand = 1): # взаимодействие с руками игрока
        for rounds in range(per_hand): 
            for hand in hands: 
                if self.cards: 
                    top_card = self.cards[0]
                    self.give(top_card, hand) 
                else: 
                    print("He могу больше сдавать: карты закончились!") 

# основная часть
deck1 = Deck()
print("Создана новая колода.")
print("Вот эта колода:", deck1)

deck1.populate() # заполнение колоды

print("\nВ колоде появились карты.")
print("Вот как она выглядит теперь:")
print(deck1)

my_hand = Hand() # моя рука
your_hand = Hand() # твоя рука
hands = [my_hand, your_hand] # руки

deck1.deal(hands, per_hand = 5) # раздача в каждую руку по пять карт

print("Мне и вам на руки раздано 5 карт.")
print("У меня на руках:")
print(my_hand)
print("У вас на руках:")
print(your_hand)
print("Осталось в колоде:")
print(deck1)

deck1.clear() # Очистка колоды
print("Колода очищена.")

print("Вот как она выглядит теперь:", deck1)

input("\nHaжмитe Enter, чтобы выйти...")
