from question import Question

training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

header = ["color", "diameter", "label"]

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

def unique_vals(rows, col):
    return set([row[col] for row in rows])

def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

for row in training_data:
	print(row)

def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def class_counts(rows):
    counts = {} 
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

pocet_radku = len(training_data[0]) - 1
print(pocet_radku)
range_radku = range(pocet_radku)
print(range_radku)

default_uncertainity = gini(training_data)
print(default_uncertainity)
		
for col in range_radku:  
	print col
	values = unique_vals(training_data, col)
	#values = set([radek[col] for radek in range_radku])
	for val in values:
		print(val)
		question = Question(col, val)
		true_answer, false_answer = partition(training_data, question)
		info_gain_val = info_gain(true_answer, false_answer, default_uncertainity)