def outer_logic():
    print("Outer function is running.")
    
    def inner_logic():
        print("Inner function is running.")
        
    # The outer function must call the inner function for it to execute
    inner_logic()

outer_logic()


