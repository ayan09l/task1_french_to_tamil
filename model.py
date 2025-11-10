from deep_translator import GoogleTranslator

class FrenchToTamilTranslator:
    def __init__(self):
        # translators using deep-translator (Google backend)
        self.fr_to_en = GoogleTranslator(source="fr", target="en")
        self.fr_to_ta = GoogleTranslator(source="fr", target="ta")
        # submission requires strict 5-letter rule
        self.submission_mode = True

    def translate(self, word: str) -> str:
        # basic validation
        if not word:
            return "❌ Please enter a French word."

        # enforce exact 5 letters for submission
        if self.submission_mode and len(word) != 5:
            return "❌ Word must be exactly 5 letters!"

        try:
            # get English meaning (for clarity)
            english = self.fr_to_en.translate(word)
            # get Tamil translation (direct from French)
            tamil = self.fr_to_ta.translate(word)
            return f"French: {word} → English: {english} → Tamil: {tamil}"
        except Exception as e:
            # friendly error for UI
            return "⚠️ Could not translate, try again."
