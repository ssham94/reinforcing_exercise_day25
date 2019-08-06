ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

ballot_count = {}

for i in range(len(ballots)):
    gold = ballots[i]['gold']
    silver = ballots[i]['silver']
    bronze = ballots[i]['bronze']
    if gold not in ballot_count:
        ballot_count[gold] = 3
    else:
        ballot_count[gold] += 3
    if silver not in ballot_count:
        ballot_count[silver] = 2
    else:
        ballot_count[silver] +=2
    if bronze not in ballot_count:
        ballot_count[bronze] = 1
    else:
        ballot_count[bronze] += 1

print(ballot_count)
print("Winner is: " + max(ballot_count, key=ballot_count.get))