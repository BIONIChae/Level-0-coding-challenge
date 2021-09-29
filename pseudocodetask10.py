def common(string1, string2):
  string1Set = set()
  for letter in string1.lower():
    string1Set.add(letter)

  string2Set = set()
  for letter in string2.lower():
    string2Set.add(letter)

  common_words = list(string1Set.intersection(string2Set))
  print('Common letters: ' + ','.join(common_words))
common('house', 'computers')
