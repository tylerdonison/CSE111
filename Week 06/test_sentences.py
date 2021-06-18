from sentences import get_adverb, get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the singular nouns.
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_noun(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_noun list.
        assert word in singular_nouns

    # Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(20):
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    # Test the past verbs.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb is
        # one of the words in the past_verbs.
        assert word in past_verbs
    
    # Test the singular present verbs
    singular_present_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]    
    #This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb is
        # one of the words in the past_verbs.
        assert word in singular_present_verbs

    # Test plural present verbs
    plural_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(20):
        word = get_verb(1, "present")

        assert word in plural_present_verbs
    
    # Test future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(20):
        word = get_verb(1, "future")

def test_get_preposition():
    #Test prepositions
    prepositions = words = ["about", "above", "across", "after", "along", 
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for", 
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over", 
            "past", "to", "under", "with", "without"]
            # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_preposition()
        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in prepositions

def test_get_prepositional_phrase():
    #Test parts of the prepositional phrase.
    prepositions = ["about", "above", "across", "after", "along", 
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for", 
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over", 
            "past", "to", "under", "with", "without"]
    singular_determiners = ["the", "one"]
    plural_determiners = ["some", "many"]
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    #This loop will repeat the statements inside 20 times.
    for _ in range(20):
        phrase = get_prepositional_phrase(1)
        words = phrase.split(" ")
        #Split the prepositional phrase back into the three parts that make it up.
        assert words[0] in prepositions
        assert words[1] in singular_determiners
        assert words[2] in singular_nouns

    #This loop will repeat the statements inside 20 times.
    for _ in range(20):
        phrase = get_prepositional_phrase(2)    
        words = phrase.split(" ")
        #Split the prepositional phrase back into the three parts that make it up.
        assert words[0] in prepositions
        assert words[1] in plural_determiners
        assert words[2] in plural_nouns
   
def test_get_adverb():
    #Test adverbs
    adverbs =["quietly", "sleepily", "loudly", "excitedly", "boldly",
            "shyly", "daily", "briefly", "cruelly", "soon", "fatally"]
    for _ in range(4):
        word = get_adverb()
        # Verify that the word returned from get_adverb
        # is one of the words in the adverbs list.
        assert word in adverbs

def main():
    test_get_determiner()
    test_get_noun()
    test_get_verb()
    test_get_preposition()
    test_get_prepositional_phrase()
    test_get_adverb()

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])

