import csv
def save(best_score,total_coins,unlocked_items): 
    header = ["best_score","coins","unlocked_items"]
    data = [[int(best_score),total_coins,unlocked_items]]
    filename = 'Save.csv'
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(data)
        
def load(): 
    with open('Save.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            return row