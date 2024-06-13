import tkinter as tk
from tkinter import *
import time
import random
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Poker App")
#Jeżeli linia 12 nie działa po prostu ją usunąć
root.iconbitmap(r'C:\Users\DELL\Downloads\Icon.ico')
root.geometry("500x250")

Eng = tk.Label(root, text="Welcome to Poker app your own poker assistant, please select the language: ")
Eng.pack()
Pl = tk.Label(root, text="Witaj w Poker appie twoim własnym asystencie przy grze w pokera, wybierz język: ")
Pl.pack()

def get_hand_ranking(hand):
    hand = random.randint(1, 8)
    if hand == 1 or 2 or 3:
        return 'Royal Flush'
    elif hand == 4 or 5 or 6:
        return 'Flush'
    else:
        return 'Two Pair'

def get_decision(hand, language):
    hand_ranking = get_hand_ranking(hand)
    if hand_ranking in ['Royal Flush', 'Straight Flush', 'Four of a Kind']:
        if language == 'polish':
            return 'pójść all in'
        else:
            return 'all in'
    elif hand_ranking in ['Full House', 'Flush', 'Straight']:
        if language == 'polish':
            return 'Podbić'
        else:
            return 'bet'
    elif hand_ranking in ['Three of a Kind', 'Two Pair']:
        if language == 'polish':
            return 'checkować'
        else:
            return 'check'
    else:
        if language == 'polish':
            return 'sfoldować'
        else:
            return 'fold'

def start_game(language):
    clear_window()
    player_hand_label = tk.Label(root, text="Enter your cards (Separate them with ,)" if language == 'english' else "Podaj swoje karty (Rozdziel je ,)")
    player_hand_label.pack()
    player_hand_entry = tk.Entry(root, width=40)
    player_hand_entry.pack()
    
    def process_player_hand():
        player_hand = player_hand_entry.get().split(", ")
        if len(player_hand) == 2:          
            clear_window()
            table_cards_label = tk.Label(root, text="Enter the cards on the table (Separate them with ,)" if language == 'english' else "Podaj karty na stole (Rozdziel je ,)")
            table_cards_label.pack()
            table_cards_entry = tk.Entry(root, width=40)
            table_cards_entry.pack()
            
            def process_table_cards():
                table_cards = table_cards_entry.get().split(", ")
                if 3 <= len(table_cards) <= 5:
                    combined_hand = player_hand + table_cards
                    decision = get_decision(combined_hand, language)
                    clear_window()
                    tk.Label(root, text=(f"Based on your hand, you should {decision}." if language == 'english' else f"Na podstawie swoich kart powinieneś: {decision}.")).pack()
                else:
                    tk.Label(root, text=("3 min 5 max")).pack()
            table_cards_button = tk.Button(root, text="Enter table cards" if language == 'english' else "Podaj karty na stole", command=process_table_cards)
            table_cards_button.pack()
        else:
            tk.Label(root, text=("Two cards max" if language == 'english' else "Dwie karty max")).pack()
    player_hand_button = tk.Button(root, text="Enter player hand" if language == 'english' else "Podaj swoje karty", command=process_player_hand)
    player_hand_button.pack()

def jezyk_Polski():
    start_game('polish')

def English_language():
    start_game('english')

def Language():
    Polski = Button(root, text="Polski", command=jezyk_Polski)
    Polski.pack()
    English = Button(root, text="English", command=English_language)
    English.pack()

Language()
root.mainloop()
