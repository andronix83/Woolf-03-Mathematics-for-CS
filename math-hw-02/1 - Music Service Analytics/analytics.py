import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# --- Data Input ---
# Defining the sets of user IDs for each genre
rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}

print("--- Music Service Analytics Results ---\n")

# 1. Total Reach (Union)
# Calculate unique users who listened to at least one genre
total_users = rock_fans | pop_fans | jazz_fans
print(f"1. Total unique users (Reach): {len(total_users)}")
print(f"   IDs: {sorted(list(total_users))}")

# 2. Omnivorous Music Lovers (Intersection of all three)
# Users who listened to Rock AND Pop AND Jazz
omnivores = rock_fans & pop_fans & jazz_fans
print(f"\n2. Omnivorous music lovers (All 3 genres): {len(omnivores)}")
print(f"   IDs: {sorted(list(omnivores))}")

# 3. Target Audience: Pure Rockers (Difference)
# Users who listened to Rock but NOT Pop and NOT Jazz
pure_rockers = rock_fans - pop_fans - jazz_fans
print(f"\n3. Pure Rockers (Rock only): {len(pure_rockers)}")
print(f"   IDs: {sorted(list(pure_rockers))}")

# 4. Exactly Two Genres
# Logic: (A & B without C) + (A & C without B) + (B & C without A)
rock_pop_only = (rock_fans & pop_fans) - jazz_fans
rock_jazz_only = (rock_fans & jazz_fans) - pop_fans
pop_jazz_only = (pop_fans & jazz_fans) - rock_fans

# Combine these groups
exactly_two = rock_pop_only | rock_jazz_only | pop_jazz_only

print(f"\n4. Users who listened to exactly two genres: {len(exactly_two)}")
print(f"   IDs: {sorted(list(exactly_two))}")
print(f"   - Rock & Pop (only): {rock_pop_only}")
print(f"   - Rock & Jazz (only): {rock_jazz_only}")
print(f"   - Pop & Jazz (only): {pop_jazz_only}")

# 5. Visualization (Venn Diagram)
plt.figure(figsize=(10, 10))
plt.title("User Audience Intersection")

# The venn3 function automatically calculates overlaps based on the sets provided
venn3([rock_fans, pop_fans, jazz_fans], set_labels=('Rock', 'Pop', 'Jazz'))

# Show the plot
plt.show()