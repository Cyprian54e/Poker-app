import tkinter as tk
import time
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
poker_hands = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'Pair', 'High Card']

def get_hand_ranking(hand):
    return 'High Card'

def get_decision(hand):
    hand_ranking = get_hand_ranking(hand)
    if hand_ranking in ['Royal Flush', 'Straight Flush', 'Four of a Kind']:
        return 'all in'
    elif hand_ranking in ['Full House', 'Flush', 'Straight']:
        return 'bet'
    elif hand_ranking in ['Three of a Kind', 'Two Pair']:
        return 'check'
    else:
        return 'fold'

root = tk.Tk()
root.title("Poker App")
#Jeżeli 29 linia nie działa po prostu ją usunąć
root.iconbitmap(r'C:\Users\DELL\Downloads\Icon.ico')
root.geometry("400x200")

def start_game():
    clear_window()
    player_hand_label = tk.Label(root, text="Enter your cards (Separate them with,): ")
    player_hand_label.pack()
    player_hand_entry = tk.Entry(root, width=40)
    player_hand_entry.pack()
    def process_player_hand():
        player_hand = player_hand_entry.get().split(", ")
        if len(player_hand) == 2:          
                clear_window()
                table_cards_label = tk.Label(root, text="Enter the cards on the table (Separate them with,): ")
                table_cards_label.pack()
                table_cards_entry = tk.Entry(root, width=40)
                table_cards_entry.pack()
                def process_table_cards():
                    table_cards = table_cards_entry.get().split(", ")
                    if 3 <= len(table_cards) <= 5:
                        combined_hand = player_hand + table_cards
                        decision = get_decision(combined_hand)
                        clear_window
                        tk.Label(root, text=(f"Based on your hand, you should {decision}.")).pack()
                    else:
                        tk.Label(root, text=("3 min 5 max")).pack()
                        time.sleep(3)
                        clear_window
                        process_table_cards
                table_cards_button = tk.Button(root, text="Enter table cards", command=process_table_cards)
                table_cards_button.pack()
        else:
            tk.Label(root, text=("Two cards max")).pack()
            time.sleep(3)
            start_game
    player_hand_button = tk.Button(root, text="Enter player hand", command=process_player_hand)
    player_hand_button.pack()
start_button = tk.Button(root, text="Start game", command=start_game)
start_button.pack()
root.mainloop()
