'''
Snake and Water --> Snake wins
Water and Gun --> Water wins
Gun and Snake --> Gun wins
'''
import random
def get_comp_choice():
    comp=random.choice(["snake","water","gun"])
    return comp

def det_winner(user,comp):
    if user==comp:
        print("It's a tie!")
    elif(comp=="snake" and user=="water") or (comp=="water" and user=="gun") or (comp=="gun" and user=="snake"):
        print("Comp win and You lose!!")
    elif(comp=="water" and user=="snake") or (comp=="gun" and user=="water") or (comp=="snake" and user=="gun"):
        print("Comp lose and You win!!")
    else:
        print("Something went wrong!")
        
def main():
    print("Welcome to the Snake-Water-Gun Game!!")
    choices=["snake","water","gun"]
    while True:
        user_choice=input("Enter your choice [snake/water/gun/exit]: ")
        if (user_choice == "exit"):
            print("Thanks for playing!")
            break
        elif user_choice not in choices:
            print("Invalid choice,please try again!")
            continue
        comp_choice= get_comp_choice()
        print(f"Computer chose: {comp_choice}")
        
        result=det_winner(user_choice,comp_choice)
        # print(result)
        print("-----------------")
if __name__=="__main__":
    main()
        