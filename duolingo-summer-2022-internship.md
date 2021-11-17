# Problem 1: Duo Outfits
- Duo likes to dress up! He has many outfits from tuxedos to track suits. Duo wants to know how many different unique outfits he can make from the items in his wardrobe.
- One caveat: some items obviously don't belong together. For example, Duo can wear a baseball hat and a T-Shirt.
- However, it wouldn't make sense to wear a baseball hat and a cowboy hat! Similarly, his polka-dot shorts don't work with his striped raincoat, so those can't be worn together either!

### Example 1
- Given all of the items in Duo's wardrobe:
    - cowboy-hat
    - scarf
    - polka-dot-shorts
    
- And lists of incompatible items (Duo cannot wear outfits containing these combinations):
    - scarf, polka-dot-shorts
    - scarf, cowboy-hat
    
- The answer would be 4, because only the following outfits are legal:
    - cowboy-hat
    - scarf
    - polka-dot-shorts
    - cowboy-hat, polka-dot-shorts
    
### Example 2
- Clothing items:
    - black-suit
    - navy-suit 
    - fancy-bow-tie
    - plain-necktie
    - black-shoes
    - brown-shoes
    
- Incompatible combinations:
    - black-suit, navy-suit
    - fancy-bow-tie, plain-neck-tie
    - black-shoes, brown-shoes
    - black-suit, fancy-bow-tie, brown-shoes
    - navy-suit, plain-necktie, black-shoes
    
- The answer would be 24, because only the following outfits are legal:
    - any single clothing item (total: 6)
    - no suit, any bow-tie, any shoes (total: 4)
    - any suit, any bow-tie, no shoes (total: 4)
    - any suit, any shoes, no bow-tie (total: 4)
    - black-suit, plain-neck-tie, any shoes (total: 2)
    - navy-suit, fancy-bow-tie, any shoes (total: 2)
    - black-suit, fancy-bow-tie, black-shoes (total: 1)
    - navy-suit, plain-neck-tie, brown-shoes (total: 1)

### Task
- Your task is to write a function that counts how many combinations of clothes Duo can wear given input lists of clothing items and illegal combinations.

```
public static int countOutfits(List<String> clothingItems, List<List<String>> illegalCombos) {

}
```


### Test Case 1
3
cowboy-hat
scarf
polka-dot-shorts
2
0
scarf polka-dot-shorts
scarf cowboy-hat

Answer: 4


### Test Case 2

1
shirt
0
0

Answer: 1

### Test Case 3

6
black-suit
navy-suit
fancy-bow-tie
plain-necktie
black-shoes
brown-shoes
5
0
black-suit navy-suit
fancy-bow-tie plain-neck-tie
black-shoes brown-shoes
black_suit fancy-bow-tie brown-shoes
navy-suit plain-necktie black-shoes

Answer: 24

# Problem 2: Bird Languages
- Duo is busy cataloging data from different bird languages. Unfortunately not a lot of historical data is written down, Duo has to figure out certain relationships himself.
- Thankfully the language of birds is very consistent. For example, two modern owl languages have the following words:

| Language | Word |
|---|---|
|Lineowl A|hoot|
|Lineowl B|hooot|

- "hoot" and "hoot" mean the same thing in both languages. Since "hoot" has exactly one extra letter more than "hoot" we can say that "hooot" is derived from "hoot". Conveniently this rule works for all bird languages!

| Language | Word |
|---|---|
| Crewol | caw |
| Pigeon | caaw |
| Lineowl A | caww |
| Lineowl B | caaww |

- All of these words have the same meaning, but their relationships are more complicated!
  The word "caw" now has two derived words: "caaw" and "caww" and both of those can be used to derive the word "caaww"!

- The rules of bird languages are as follows:
    - Bird languages use only 26 letters (a-z). Words must contain at least 1 letter.
    - Word B is derived from word A if you can delete exactly 1 letter from word B to get word A
    - Word A and word B have the same meaning if word B is derived from word A.
    - If a word has no derivation or derived forms, then it has a unique meaning.
    
- Duo has the vocabulary of all the bird languages. Now he wants to know how many different meanings there are in all of the words! 
  Here is an example. Given the words "hoot", "hooot", "caw", "caaw", "caww", "caaww", and "chirp" there exists 3 distinct meanings.


|Meaning|Words|
|---|---|
|1|hoot, hooot|
|2|caw, cc aaw, caww, caaww|
|3|chirp|

- In this example, the answer would be "3".

### Task
- Find a solution that counts the number of distinct meanings given any vocabulary.

```
public static int countDistinctMeanings(List<String> birdLanguageVocabulary) {

}
```


### Test Case 1
7
caw
caaw
caww
caaww
hoot
hooot
chirp

Answer: 3

### Test Case 2
3
quack
quaack
qaauck

Answer: 2

### Test Case 3
1
hoot

Answer: 1
