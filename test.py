def test():
	return "ahoj"

def rozlouceni():
	return "mej se"

text = test()
text2 = rozlouceni()

print(text)
print(text2)

class MojeTrida:
	def __init__(self, jmeno):
		self.krestni = jmeno
		self.prijmeni = jmeno + "Prijmeni"


	def predstavse(self):
		return (self.krestni + " " + self.prijmeni)

	def __repr__(self):
		self.predstavse()

	def __str__():
		return self.predstavse()

david = MojeTrida("david")
david
david
print(david)
print(david.predstavse())

print("--- konec skriptu ---")

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
    	print "label=" + label
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    print "counts=" + str(counts)
    return counts

def gini(rows):
    """Calculate the Gini Impurity for a list of rows.
    There are a few different ways to do this, I thought this one was
    the most concise. See:
    https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    print "impurity=" + str(impurity)
    return impurity

data = [['francouz', 'renault', 'auto'], ['nemec', 'bmw', 'auto'], ['cech', 'skoda', 'kram']] 
print(gini(data))

print(3**2)
cislo=10
cislo -= 2
print(cislo)