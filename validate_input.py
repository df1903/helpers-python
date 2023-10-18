# Imports
from datetime import datetime, date

class ValidateInput:

  def integer(inputMessage, errorMessage):
    """
    Validates that the input is an integer.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not an integer.
    :return: The integer value entered by the user.
    """
    while True:
            try:
                value = int(input(inputMessage))
                break
            except:
                print(errorMessage)
    return value

  def integerDefaultErrorMessage(inputMessage):
    """
    Validates that the input is an integer.
    :param inputMessage: The message to display when asking for input.
    :return: The integer value entered by the user.
    """
    while True:
            try:
                value = int(input(inputMessage))
                break
            except:
                print("You must enter an integer number.")
    return value

  def integerWithinRange(inputMessage, errorMessage, minValue, maxValue):
    """
    Validates that the input is an integer within a range.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not an integer within the range.
    :param minValue: The minimum value allowed.
    :param maxValue: The maximum value allowed.
    :return: The integer value entered by the user.
    """
    while True:
      try:
          value = int(input(inputMessage))
          if value < minValue or value > maxValue:
              raise
          else:
              break
      except:
          print(errorMessage)
    return value

  def integerWithinRangeDefaultErrorMessage(inputMessage, minValue, maxValue):
    """
    Validates that the input is an integer within a range.
    :param inputMessage: The message to display when asking for input.
    :param minValue: The minimum value allowed.
    :param maxValue: The maximum value allowed.
    :return: The integer value entered by the user.
    """
    while True:
      try:
          value = int(input(inputMessage))
          if value < minValue or value > maxValue:
              raise
          else:
              break
      except:
          print(f"You must enter an integer number between {minValue} and {maxValue}.")
    return value

  def decimal(inputMessage, errorMessage):
    """
    Validates that the input is a decimal number.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not a decimal number.
    :return: The decimal value entered by the user.
    """
    while True:
      try:
          value = float(input(inputMessage))
          break
      except:
          print(errorMessage)
    return value

  def decimalDefaultErrorMessage(inputMessage):
    """
    Validates that the input is a decimal number.
    :param inputMessage: The message to display when asking for input.
    :return: The decimal value entered by the user.
    """
    while True:
      try:
          value = float(input(inputMessage))
          break
      except:
          print("You must enter a number.")
    return value

  def decimalWithinRange(inputMessage, errorMessage, minValue, maxValue):
    """
    Validates that the input is a decimal number within a range.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not a decimal number within the range.
    :param minValue: The minimum value allowed.
    :param maxValue: The maximum value allowed.
    :return: The decimal value entered by the user.
    """
    while True:
      try:
          value = float(input(inputMessage))
          if value < minValue or value > maxValue:
              raise
          else:
              break
      except:
          print(errorMessage)
    return value

  def decimalWithinRangeDefaultErrorMessage(inputMessage, minValue, maxValue):
    """
    Validates that the input is a decimal number within a range.
    :param inputMessage: The message to display when asking for input.
    :param minValue: The minimum value allowed.
    :param maxValue: The maximum value allowed.
    :return: The decimal value entered by the user.
    """
    while True:
      try:
          value = float(input(inputMessage))
          if value < minValue or value > maxValue:
              raise
          else:
              break
      except:
          print(f"You must enter a number between {minValue} and {maxValue}.")
    return value

  def string(inputMessage, errorMessage):
    """
    Validates that the input is a string.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not a string.
    :return: The string value entered by the user.
    """
    while True:
      try:
          value = str(input(inputMessage))
          break
      except:
          print(errorMessage)
    return value

  def stringDefaultErrorMessage(inputMessage):
    """
    Validates that the input is a string.
    :param inputMessage: The message to display when asking for input.
    :return: The string value entered by the user.
    """
    while True:
      try:
          value = str(input(inputMessage))
          break
      except:
          print("You must enter a string.")
    return value

  def stringWithinRange(inputMessage, errorMessage, minLength, maxLength):
    """
    Validates that the input is a string within a range.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not a string within the range.
    :param minLength: The minimum length allowed.
    :param maxLength: The maximum length allowed.
    :return: The string value entered by the user.
    """
    while True:
      try:
          value = str(input(inputMessage))
          if len(value) < minLength or len(value) > maxLength:
              raise
          else:
              break
      except:
          print(errorMessage)
    return value

  def stringWithinRangeDefaultErrorMessage(inputMessage, minLength, maxLength):
    """
    Validates that the input is a string within a range.
    :param inputMessage: The message to display when asking for input.
    :param minLength: The minimum length allowed.
    :param maxLength: The maximum length allowed.
    :return: The string value entered by the user.
    """
    while True:
      try:
          value = str(input(inputMessage))
          if len(value) < minLength or len(value) > maxLength:
              raise
          else:
              break
      except:
          print(f"You must enter a string between {minLength} and {maxLength} characters long.")
    return value

  def boolean(inputMessage, errorMessage):
    """
    Validates that the input is a boolean.
    :param inputMessage: The message to display when asking for input.
    :param errorMessage: The message to display when input is not a boolean.
    :return: The boolean value entered by the user.
    """
    while True:
      try:
          value = str(input(inputMessage)).lower()
          if value.startswith("s") or value.startswith("y"):
              value = True
              break
          elif value.startswith("n"):
              value = False
              break
          else:
              raise
      except:
          print(errorMessage)
    return value

  def booleanDefaultErrorMessage(inputMessage):
    """
    Validates that the input is a boolean.
    :param inputMessage: The message to display when asking for input.
    :return: The boolean value entered by the user.
    """
    while True:
      try:
          value = str(input(inputMessage)).lower()
          if value.startswith("s") or value.startswith("y"):
              value = True
              break
          elif value.startswith("n"):
              value = False
              break
          else:
              raise
      except:
          print("You must enter 'yes' or 'no'.")
    return value

