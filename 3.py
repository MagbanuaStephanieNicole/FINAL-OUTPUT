import time

def typing_master():
    # Text for the user to type
    text_to_type = "The quick brown fox jumps over the lazy dog."
    
    print("Are you ready to become a Typing Master?")
    print()
    print("Type the following text as accurately and quickly as possible:")
    print(text_to_type)
    print()
    input("If you are ready to type press ENTER.")
    
    start_time = time.time()
    user_input = input("TYPE HERE: ")
    end_time = time.time()
    
    # Calculate time taken in seconds
    time_taken = end_time - start_time
    
    # Calculate accuracy
    errors = 0
    for i in range(min(len(text_to_type), len(user_input))):
        if text_to_type[i] != user_input[i]:
            errors += 1
    
    accuracy = (len(text_to_type) - errors) / len(text_to_type) * 100
    
    # Display results
    print("\nTyping test completed!")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    
    # Optional: Display the errors
    if errors > 0:
        print(f"Errors found: {errors}")
        print("Here is the text you typed with errors marked:")
        for i in range(len(text_to_type)):
            if i < len(user_input) and text_to_type[i] != user_input[i]:
                print(f"{user_input[i]}", end=' ')
            else:
                print(f"{text_to_type[i]}", end=' ')
        print()
    
# Run the typing master program
typing_master()
