# Daniel Feuer
# 10/9/24

from itertools import combinations

def getTransactions(filename):
    transactions = []
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into items and add them to the transactions list
            items = line.strip().split()
            transactions.append(items)
    return transactions

def generateCandidates(items, length):
    # Generate all possible combinations of items with the given length
    return list(combinations(items, length))

def calcSupport(candidate, transactions):
    count = 0
    for transaction in transactions:
        # Check if all items in the candidate are in the transaction
        if all(item in transaction for item in candidate):
            count += 1
    # Calculate the support level as a percentage
    return count / len(transactions) * 100

def apriori(filename, minSupportLevel):
    transactions = getTransactions(filename)
    # Sorts the items in the transactions and removes duplicates to get all items
    allItems = sorted(set(item for transaction in transactions for item in transaction))
    length = 1
    freqItemSets = []
    
    while True:
        # Generate all possible candidates of the current length
        candidates = generateCandidates(allItems, length)
        freqItems = []

        # Calculate the support level for each candidate and add it to the frequent itemsets if it meets the minimum support level
        for candidate in candidates:
            support = calcSupport(candidate, transactions)
            if support >= minSupportLevel:
                freqItems.append(candidate)

        if not freqItems:
            break
        
        freqItemSets.extend(freqItems)
        length += 1
    
    return freqItemSets

def main():
    filename = input("Enter the filename: ")
    minSupportLevel = float(input("Enter the minimal support level (%): "))
    freqItemSets = apriori(filename, minSupportLevel)

    print("\nFrequent Itemsets:")
    for itemset in freqItemSets:
        print(itemset)

if __name__ == "__main__":
    main()