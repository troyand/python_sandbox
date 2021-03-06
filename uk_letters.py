# -*- coding: utf-8 -*-

def get_transliteration_dict(out_encoding='BGN/PCGN'):
    import csv
    txt_reader = csv.DictReader(open("ukrainian_character_map.csv"), delimiter="\t", quotechar="|")
    letters = {}
    for row in txt_reader:
        letters[ unicode(row['Cyrillic'].split(' ')[1], 'utf-8') ] = unicode(row[out_encoding].strip(), 'utf-8')

    small_letters = letters.copy()
    for small_letter in small_letters:
        letters[small_letter.upper()] = small_letters[small_letter].capitalize()

    return letters

if __name__=="__main__":
    letters = get_transliteration_dict()
    for letter in letters:
        print letter, '->', letters[letter]
