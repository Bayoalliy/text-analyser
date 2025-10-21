from hashlib import sha256

class String():
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        reversed_str = self.value[::-1].lower()
        if reversed_str == self.value.lower():
            return True
        return False

    def length(self):
        return len(self.value)


    def unique_characters(self):
        return len(set(self.value))

    def word_count(self):
        return len(self.value.split())

    def hashed_value(self):
        return sha256(self.value.encode()).hexdigest()

    def character_frequency_map(self):
        dic = {}
        for char in self.value:
            if char not in dic.keys():
                dic[char] = 1
            else:
                dic[char] += 1
        return dic


