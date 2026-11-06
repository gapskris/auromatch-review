# -*- coding: utf-8 -*-
"""
AuroMatch: The Triple Garden of Significances — Vocabulary & Tile Content Classifier
This script processes raw excerpts from the collected works of Sri Aurobindo and the Mother
to build a thematic tile quote database for the teachings repository.

To scale:
1. Place text files of digitized works in a local folder 'corpus/'.
2. Run this script to extract matching qualities, flowers, Sanskrit seeds, and symbol meanings.
"""

import os
import re
import json

# 1. Sample text corpus containing direct excerpts
SAMPLE_CORPUS = [
    {
        "text": "Sincerity is the key of the divine doors; it is the condition of all progress. To be sincere is to have no other dynamic motive than the desire to find the Divine and serve Him.",
        "source": "The Mother",
        "book": "Words of The Mother - Vol 14"
    },
    {
        "text": "True humility consists in knowing that without the Divine Grace we are nothing, and that our only strength is the strength of the Divine working through us.",
        "source": "The Mother",
        "book": "Words of The Mother - Vol 14"
    },
    {
        "text": "Gratitude is a loving vibration of the soul turned toward the Divine. It is the sweetest of all vibrations that can rise from the heart.",
        "source": "The Mother",
        "book": "Words of The Mother - Vol 14"
    },
    {
        "text": "To feel the Divine presence constantly in all things and all movements. The lotus is the flower of quiet, ascending aspiration.",
        "source": "The Mother",
        "book": "Flowers and Their Messages"
    },
    {
        "text": "Simple, sweet, and direct; it opens to the Light without demands or calculations. Purity is the shield that keeps out all vital disturbance.",
        "source": "The Mother",
        "book": "Flowers and Their Messages"
    },
    {
        "text": "Pure, constant, and complete; the offering of the heart at the feet of the Mother. A rose blooms in silent devotion, seeking only to give its fragrance.",
        "source": "The Mother",
        "book": "Flowers and Their Messages"
    },
    {
        "text": "Om is the signature of the Infinite. It is the unmanifest sound from which all manifestation rises, bringing peace and cosmic expansion to the mind.",
        "source": "Sri Aurobindo",
        "book": "Letters on Yoga - Vol 29"
    },
    {
        "text": "In the silence of the mind, the divine force acts and transforms the nature. Speak only when necessary and let your words arise from that deep peace.",
        "source": "Sri Aurobindo",
        "book": "Letters on Yoga - Vol 29"
    },
    {
        "text": "The overlapping triangles represent the ascent of human aspiration and the descent of the Divine Grace. The square in the center represents manifestation, and the lotus represents realization.",
        "source": "Sri Aurobindo",
        "book": "Collected Letters"
    }
]

# 2. Stop words to filter out grammatical connector words
STOP_WORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", 
    "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", 
    "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", 
    "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", 
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
    "for", "with", "about", "against", "between", "into", "through", "during", "before", 
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", 
    "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", 
    "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", 
    "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", 
    "will", "just", "don", "should", "now", "let", "always", "would", "never", "only"
}

# 3. Seed keywords for thematic classification
THEMES_SEEDS = {
    "qualities": ["sincerity", "humility", "gratitude", "perseverance", "aspiration", "receptivity", "progress", "courage", "goodness", "generosity", "equality", "peace"],
    "flowers": ["lotus", "jasmine", "rose", "hibiscus", "marigold", "periwinkle", "zinnia", "tulsi"],
    "sanskrit": ["om", "shanti", "jyoti", "satya", "ananda", "prem"],
    "symbols": ["triangles", "symbol", "crystal", "service", "leaf", "conch", "diya", "matrimandir", "petal"]
}

def clean_and_tokenize(text):
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned.split()
    return [w for w in words if w not in STOP_WORDS and len(w) > 2]

def classify_word(word):
    for theme, seeds in THEMES_SEEDS.items():
        if word in seeds:
            return theme
    for theme, seeds in THEMES_SEEDS.items():
        for seed in seeds:
            if seed in word or word in seed:
                return theme
    return None

def build_repository(corpus):
    themes_db = {theme: {"words": set(), "quotes": []} for theme in THEMES_SEEDS}
    quote_id_counter = 1
    
    for entry in corpus:
        text = entry["text"]
        source = entry["source"]
        book = entry["book"]
        
        tokens = clean_and_tokenize(text)
        
        for token in tokens:
            theme = classify_word(token)
            if theme:
                word_upper = token.upper()
                themes_db[theme]["words"].add(word_upper)
                
                # Append the quote object for this specific word
                quote_object = {
                    "id": f"Q_{theme.upper()[:4]}_{quote_id_counter:03d}",
                    "name": token.capitalize(),
                    "quality": token.capitalize(),
                    "text": text,
                    "source": source,
                    "book": book
                }
                # Check for duplicates
                if quote_object not in themes_db[theme]["quotes"]:
                    themes_db[theme]["quotes"].append(quote_object)
                    quote_id_counter += 1
            
    # Convert sets to sorted lists for final JSON serialization
    final_db = {}
    for theme, data in themes_db.items():
        final_db[theme] = {
            "words": sorted(list(data["words"])),
            "quotes": data["quotes"]
        }
        
    return final_db

if __name__ == "__main__":
    print("Initializing AuroMatch Vocabulary Pipeline...")
    repository = build_repository(SAMPLE_CORPUS)
    
    # Save the output to teachings_repository.json
    output_path = "c:\\DataScience\\AuroProject_Annalysis\\AuroMatch\\doc\\teachings_repository.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(repository, f, indent=2, ensure_ascii=False)
        
    clean_path = output_path.replace('\\', '/')
    print(f"\nSuccess! Categorized tile sets and quotes written to:\n[teachings_repository.json](file:///{clean_path})")
