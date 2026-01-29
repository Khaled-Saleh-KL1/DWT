class QAStore:
    def __init__(self):
        self._context_data = ""

    def save_context(self, text: str):
        self._context_data = text

    def get_context(self) -> str:
        return self._context_data

    def clear(self):
        self._context_data = ""
