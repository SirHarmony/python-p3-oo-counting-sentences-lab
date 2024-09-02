#!/usr/bin/env python3

class MyString:
  def __init__(self,value=''):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self,value):
    if isinstance(value,str):
      self._value = value
    else: 
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else: 
      return False

  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else:
      return False

  def count_sentences(self):
    new_value = self.value.replace("!",".")
    new_value_2 = new_value.replace("?",".")
    list_of_split_sentences = new_value_2.split(".")
    number_of_sentences = [sentence for sentence in list_of_split_sentences if sentence != '']
    return len(number_of_sentences)

harmony = MyString("This is a string! It has three sentences. Right?")
print(harmony.count_sentences())