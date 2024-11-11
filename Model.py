

import requests
from textblob import TextBlob
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_tool = language_tool_python.LanguageTool('en-US')  # Specify language

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)



    def correct_grammar(self, text):
        matches = self.grammar_tool.check(text)
        foundmistakes = []
    
        for match in matches:
        # Create a structured output for each mistake
            mistake_detail = {
                'rule_id': match.ruleId,
                'message': match.message,
                'context': match.context,  # You can include the context if needed
                'replacements': match.replacements  # Possible corrections
            }
            foundmistakes.append(mistake_detail)
    
        foundmistakes_count = len(foundmistakes)
        return foundmistakes, foundmistakes_count


    def get_spelling_mistakes(self, text):
        words = text.split()
        spelling_mistakes = []
    
        for word in words:
            corrected_word = str(TextBlob(word).correct())
        if corrected_word != word:
            spelling_mistakes.append((word, corrected_word))  # Return original and corrected words
    
        return spelling_mistakes