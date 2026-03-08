SIZE = 4

percepts = {
    (1,1): {"B": False, "S": False, "G": False},
    (1,2): {"B": False, "S": True,  "G": False},
    (2,1): {"B": True,  "S": False, "G": False},
    (2,3): {"B": True,  "S": True,  "G": True }
}

safe=set()
possible_pit=set()
possible_wumpus=set()
gold_location=None
wumpus_location=None

def get_adj(x,y):
    return[ (a,b)
         for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
         if 1<=a<=SIZE and 1<=b<=SIZE
        ]

def logical_reasoning():
    global gold_location,wumpus_location 
    
    visited=set(percepts.keys())
    
    for (x,y),p in percepts.items():
        
        print(f"\nCurrently in {x,y} \n")
        adj=get_adj(x,y)
        
        if p["G"]:
            gold_location=(x,y)
            print(f"Gold found at {x,y}")
            
        if not p["B"]:
            for c in adj:
                possible_pit.discard(c)
                if c not in visited:
                    safe.add(c)
            print(f"No Breeze at {x,y}")
            
        else:
            for c in adj:
                if c not in visited:
                   possible_pit.add(c)
            print(f"Possible pits at {[c for c in adj if c not in visited]}")
        
        if not p["S"]:
            for c in adj:
                possible_wumpus.discard(c)
                if c not in visited:
                    safe.add(c)
            print(f"No Stench at {x,y}")
            
        else:
            for c in adj:
                if c not in visited:
                   possible_wumpus.add(c)
            print(f"Possible wumpus at {[c for c in adj if c not in visited]}")
            
    safe.update(visited)
    
    if len(possible_wumpus) == 1:
        wumpus_location=next(iter(possible_wumpus))
        print(f"Wumpus at {wumpus_location}")
        

print("=" * 45)
print("       WUMPUS WORLD — LOGICAL REASONING")
print("=" * 45)
print("\n--- Applying inference rules ---")
logical_reasoning() 


print("\n--- Results ---")
print(f"  Safe Cells          : {sorted(safe)}")
print(f"  Possible Pit Cells  : {sorted(possible_pit)}")
print(f"  Possible Wumpus     : {sorted(possible_wumpus)}")
print(f"  Wumpus Location     : {wumpus_location}")
print(f"  Gold Location       : {gold_location}")

print("\n--- Agent Decision ---")
if gold_location:
    print(f"   Navigate to {gold_location} to grab the Gold!")
if wumpus_location:
    print(f"    Shoot arrow toward {wumpus_location} — Wumpus is there!")
if possible_pit:
    print(f"    Avoid {sorted(possible_pit)} — possible pits!")
