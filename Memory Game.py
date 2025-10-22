import os
import time
import random
class Node:
    def __init__(self, value):
        self.value = value
        self.revealed = False
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        pos = 1
        print("\nCurrent Board:")
        while temp:
            if temp.revealed:
                print(f"[ {temp.value} ]", end=" ")
            else:
                print(f"[ {pos} ]", end=" ")
            temp = temp.next
            pos += 1
        print("\n")
    def get_node(self, pos):
        temp = self.head
        count = 1
        while temp and count < pos:
            temp = temp.next
            count += 1
        return temp
    def all_revealed(self):
        temp = self.head
        while temp:
            if not temp.revealed:
                return False
            temp = temp.next
        return True
def setup_game():
    symbols = ['A', 'B', 'C', 'D']  # 4 pairs = 8 cards
    cards = symbols * 2
    random.shuffle(cards)
    linked_list = LinkedList()
    for c in cards:
        linked_list.append(c)
    return linked_list
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def play_game():
    print("Memory Game using Linked List ")
    print("Match all pairs to win!\n")
    time.sleep(1)
    game = setup_game()
    moves = 0
    while not game.all_revealed():
        clear_screen()
        game.display()
        try:
            first = int(input("Choose the first card position: "))
            second = int(input("Choose the second card position: "))
        except ValueError:
            print("Enter valid numbers!")
            time.sleep(1.5)
            continue
        if first == second or first < 1 or second < 1:
            print("Invalid positions. Try again!")
            time.sleep(1.5)
            continue
        card1 = game.get_node(first)
        card2 = game.get_node(second)
        if not card1 or not card2:
            print("Position out of range. Try again!")
            time.sleep(1.5)
            continue
        clear_screen()
        print(f"\nYou flipped: {card1.value} and {card2.value}")
        game.display()
        moves += 1
        if card1.value == card2.value:
            print("It's a match!")
            card1.revealed = True
            card2.revealed = True
        else:
            print("Not a match. Remember their positions!")
            time.sleep(2)
        time.sleep(1.5)

    clear_screen()
    print("\nCongratulations! You matched all pairs!")
    print(f"Total Moves: {moves}")
if __name__ == "__main__":
    play_game()
