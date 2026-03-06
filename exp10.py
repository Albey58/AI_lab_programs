# Simple Wumpus World with logical reasoning
# Represent knowledge base with sets of clauses

def tell(kb, sentence):
    kb.add(sentence)

def ask(kb, query):
    # Simple check if query is entailed
    return query in kb

def main():
    kb = set()
    # Example: if breeze in 1,1 then pit in adjacent
    # But simplified
    tell(kb, "breeze_at_1_1 -> pit_at_1_2 or pit_at_2_1")
    # Perceive
    tell(kb, "breeze_at_1_1")
    # Infer
    if ask(kb, "pit_at_1_2"):
        print("Pit at 1,2")
    else:
        print("No pit at 1,2")

if __name__ == "__main__":
    main()