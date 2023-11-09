"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title, story_id):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title
        self.id = story_id

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

# Here's a story to get you started
story_1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""", "Long Ago", 0
)

story_2 = Story(
    ["noun", "place", "verb"], """Have you ever heard why the {noun} crossed the {place}?  It was trying to {verb}.""", "Crossing", 1
)

story_3 = Story(
    ["superlative_adjective", "color", "noun", "ing_verb"], """The {superlative_adjective} thing I've ever seen was a {color} {noun} {ing_verb} down by the Sea!""", "Down by the Sea", 2
)

story_list = [story_1, story_2, story_3]

def get_story(story_id):
    for each in story_list:
        if each.id == int(story_id):
            return each