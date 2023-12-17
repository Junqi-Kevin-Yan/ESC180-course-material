'''
1)	create	a	frequency	dic0onary	mapping	str:int
2)	find	word	that	occurs	the	most and	how	many times 
• 	use	a	list,	in	case	there	is	more	than	one	word	
• 	return	a	tuple	(list,int)	for		(words_list,	highest_freq)	
3)	find	the	words	that	occur	at	least	X	0mes	
• 	let	user	choose	“at	least	X	Smes”,	so	allow	as	parameter	
• 	return	a	list	of	tuples,	each	tuple	is	a	(list, int)
containing	the	list	of	words	ordered	by	their	frequency	
• 	IDEA:	From	song	dicSonary,	find	most	frequent	word.	Delete	
most	common	word.	Repeat.	It	works	because	you	are	mutating song dictionary'''
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1 # update value with key 
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.value() # get all values from freqs 
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
