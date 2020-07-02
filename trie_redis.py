import pytest

from pprint import pprint
from redis import Redis 

r = Redis(
    host = '',
    port = '30562',
    password = ''
)

# Refactor into unit test


sample_trie = {
            't': {
                'r': {
                    'e': {
                        'e': {'end': True},
                        },
                    'i': {
                        'e': {'end': True},
                        }
                    }
                
                }
    }

random_words = [
    'sand',
    'salt',
    'salad',
    'topaz',
    'love',
    'tree',
    'trie',
    'who',
    'what'
]

def test_insert():
    trie = sample_trie
    new_trie = {}
    insert_word_trie(new_trie, 'tree')
    insert_word_trie(new_trie, 'trie')
    assert trie == new_trie


def test_search():
    trie = sample_trie
    assert search_word_trie(trie, "tree")
    assert search_word_trie(trie, "trie")
    assert not search_word_trie(trie, "abcde")
    assert not search_word_trie(trie, "treee")
    assert not search_word_trie(trie, "tre")
    assert not search_word_trie(trie, "trei")

    for w in random_words:
        insert_word_trie(trie, w)
    

def test_autocomplete():
    trie = {}
    for w in random_words:
        insert_word_trie(trie, w)
    assert {} == autocomplete_trie(trie, "")
    assert {} == autocomplete_trie(trie, "a")
    assert {"who", "what", ""} == autocomplete_trie(trie, "w")
    assert {"who"} == autocomplete_trie(trie, "wh")
    assert {"who"} == autocomplete_trie(trie, "who")
    assert {} == autocomplete_trie(trie, "whoo")
    assert {"tree", "trie", "topaz"} == autocomplete_trie(trie, "t")
    assert {"tree", "trie"} == autocomplete_trie(trie, "tr")
    assert {"salt", "salad", "sand"} == autocomplete_trie(trie, "sa")
    assert {"salt", "salad"} == autocomplete_trie(trie, "sal")
    assert {"salad"} == autocomplete_trie(trie, "sala")
    assert {"salad"} == autocomplete_trie(trie, "salad")
    assert {} == autocomplete_trie(trie, "salada")
    assert {"love"} == autocomplete_trie(trie, "lo")
    assert {"topaz"} == autocomplete_trie(trie, "t")
    assert {"topaz"} == autocomplete_trie(trie, "to")
    assert {"topaz"} == autocomplete_trie(trie, "top")
    assert {"topaz"} == autocomplete_trie(trie, "topa")
    assert {"topaz"} == autocomplete_trie(trie, "topaz")
    assert {""} == autocomplete_trie(trie, "topazo")


def autocomplete_trie(trie, word):
    if not word:
        return {}

    node = trie
    found = has_more = True
    prefix = ""
    for w in word:
        if w in node:
            node = node[w]
            prefix += w
        else:
            print("Returning empty")
            return {}

    
    print("node: {}".format(node))
    return node 


def search_word_trie(trie, word):
    node = trie
    for w in word:
        # print(w)
        try:
            node = node[w]
        except:
            return False
    # print(node)
    try:
        node['end']
        return True
    except:
        return False

def autocomplete(trie, word):
    print("autocomplete")

def insert_word_trie(trie, word):
    node = trie
    for w in word:
        if w in node:
            node = node[w]
        else:
            node[w] = {} 
            node = node[w]

    node['end'] = True


#r.set('foo', str(trie))
# print(r.get('foo'))
