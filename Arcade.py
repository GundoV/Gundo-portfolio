# Arcade High Score Tracker

while True:
    # 1. Prompt for input (the prompt string leaves the cursor right next to it)
    user_input = input("Enter your game score (or type 'stop' to quit): ")
    
    # 2. Clean up the input string to handle extra spaces or mixed casing
    cleaned_input = user_input.strip().lower()
    
    # 3. Check for the exit command
    if cleaned_input == "stop":
        print("Game session ended!")
        break
    
    # 4. Process the numerical score
    score = int(cleaned_input)
    
    if score > 100:
        print("Wow! That’s a new high score!\n")
    else:
        print("Good try, keep playing!\n")