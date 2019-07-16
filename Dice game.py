import random

def main():
    again = True
    while(again):
        randnum = random.randint(1,6)
        print(randnum)
        roll_again = input("PRESS ENTER TO ROLL AGAIN ")
        if (roll_again == 1):
            break
        else:
            ("PRESS ENTER TO ROLL AGAIN ")
            
    
    
if __name__ == "__main__":
    main()