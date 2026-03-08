visited=set()
def water_jug_dfs(a,b,jug1,jug2,target):
    if (a,b) in visited:
        return False
    print(f"Visited states:({a},{b})")
    visited.add((a,b))
    if a==target or b==target:
        print("Solution Found:",(a,b))
        return True
    return(
        water_jug_dfs(jug1,b,jug1,jug2,target) or
        water_jug_dfs(a,jug2,jug1,jug2,target) or 
        water_jug_dfs(0,b,jug1,jug2,target) or 
        water_jug_dfs(a,0,jug1,jug2,target) or
        water_jug_dfs(a-min(a,jug2-b),b+min(a,jug2-b),jug1,jug2,target) or
        water_jug_dfs(a+min(a,jug1-a),b-min(a,jug1-a),jug1,jug2,target)
    )
a=int(input("Enter jug1 cap:"))
b=int(input("Enter jug2 cap:"))
water_jug_dfs(a,b,4,3,2)
