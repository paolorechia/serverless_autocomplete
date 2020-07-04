# import pytest

import os
from pprint import pprint
from redis import Redis 

# Refactor into unit test

r = Redis(
        host = os.getenv("REDIS_HOST"),
        port = os.getenv("REDIS_PORT"),
        password = os.getenv("REDIS_PASSWORD")
    )


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
    assert {"who", "what"} == autocomplete_trie(trie, "w")
    assert {"who", "what"} == autocomplete_trie(trie, "wh")
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
    assert {"topaz"} == autocomplete_trie(trie, "to")
    assert {"topaz"} == autocomplete_trie(trie, "top")
    assert {"topaz"} == autocomplete_trie(trie, "topa")
    assert {"topaz"} == autocomplete_trie(trie, "topaz")
    assert {} == autocomplete_trie(trie, "topazo")


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
            return {}

    words = set()
    _get_words_from_node(node, prefix=prefix, words=words)
    return words

def _get_words_from_node(node, prefix=None, words=set()):
    for key in node.keys():
        if key == 'end':
            words.add(prefix)
            continue
        if 'end' in node[key]:
            words.add(prefix + key)
        else:
            _get_words_from_node(node[key], prefix + key, words)


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


def insert_word_trie(trie, word):
    node = trie
    for w in word:
        if w in node:
            node = node[w]
        else:
            node[w] = {} 
            node = node[w]

    node['end'] = True


def build_trie(words):
    trie = {}
    for w in words:
        insert_word_trie(trie, w)
    return trie


def persist_trie(trie):
    r.set('trie', str(trie))

def retrieve_trie():
    return r.get('trie')
