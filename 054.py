hands = []


def card_value(card):
    return '23456789TJQKA'.index(card[0])


def find_hand(hand):
    nums = sorted([h[0] for h in hand], key=lambda x: '23456789TJQKA'.index(x))
    suits = sorted([h[1] for h in hand])
    
    # Royal Flush
    if all([h[1] == hand[0][1] for h in hand]) and ''.join(nums) == 'TJQKA':
        return 9, 12, 12, 12, 12, 12
    
    # Straight Flush
    if all([s == suits[0] for s in suits]) and ''.join(nums) in '23456789TJQKA':
        return 8, card_value(nums[-1]), 12, 12, 12, 12
        
    # Four of a Kind
    nums_count = [nums.count(h) for h in nums]
    if any(map(lambda x: x == 4, nums_count)):
        return 7, card_value(nums[-1] if nums_count[-1] == 4 else nums[0]), card_value(nums[-1] if nums_count[-1] == 1 else nums[0]), 12, 12, 12
    
    # Full House
    if any(map(lambda x: x == 3, nums_count)) and any(map(lambda x: x == 2, nums_count)):
        return 6, card_value(nums[-1] if nums_count[-1] == 3 else nums[0]), card_value(nums[-1] if nums_count[-1] == 2 else nums[0]), 12, 12, 12
    
    # Flush
    if all([s == suits[0] for s in suits]):
        return 5, card_value(nums[-1]), card_value(nums[-2]), card_value(nums[-3]), 12, 12
    
    # Straight
    if ''.join(nums) in '23456789TJQKA':
        return 4, card_value(nums[-1]), 12, 12, 12, 12
    
    # Three of a Kind
    if any(map(lambda x: x == 3, nums_count)):
        c1 = nums[nums_count.index(1)]
        c2 = nums[nums_count.index(1, nums_count.index(1) + 1)]
        return 3, card_value(nums[nums_count.index(3)]), card_value(c2), card_value(c1), 12, 12
    
    # Two Pairs
    if nums_count.count(2) == 4:
        p1 = nums[nums_count.index(2)]
        p2 = nums[nums_count.index(2, nums_count.index(2) + 2)]
        c = nums[nums_count.index(1)]
        return 2, card_value(p2), card_value(p1), card_value(c), 12, 12
    
    # One Pair
    if nums_count.count(2) == 2:
        p = nums[nums_count.index(2)]
        c1 = nums[nums_count.index(1)]
        c2 = nums[nums_count.index(1, nums_count.index(1) + 1)]
        c3 = nums[nums_count.index(1, nums_count.index(1, nums_count.index(1) + 1) + 1)]
        return 1, card_value(p), card_value(c3), card_value(c2), 12, 12
    
    # High Card
    return 0, card_value(nums[-1]), card_value(nums[-2]), card_value(nums[-3]), card_value(nums[-4]), card_value(nums[-5])
    

with open('./input/0054_poker.txt', 'r') as f:
    data = f.read().split('\n')
    hands = [((d.split()[:5]), (d.split()[5:])) for d in data][:-1]
    

p1_wins = 0
for p1, p2 in hands:
    ss1, ss2 = find_hand(p1), find_hand(p2)
    for s1, s2 in zip(ss1, ss2):
        if s1 == s2:
            continue
        
        fss1 = ".".join(map(lambda x: f'{x:>1X}', ss1))
        fss2 = ".".join(map(lambda x: f'{x:>1X}', ss2))
        print(f'{p1} - {fss1}   vs   {p2} - {fss2}', end='   ')
        if s1 > s2:
            print('P1 wins')
            p1_wins += 1
        else:
            print('P2 wins')
        break
        

print(f'Answer: {p1_wins}')