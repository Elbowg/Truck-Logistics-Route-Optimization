def simulate_path(path):
    print("\n Truck traveling...\n")
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\nDestination reached!")
    
    print("\nVisited Order:", visit_order)
    print("Optimal Path:", pat)
    print("Total Cost:", tot_cost)

simulte_path(pat)