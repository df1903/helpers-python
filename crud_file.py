# Imports
import os
import json

class CrudFile:

  def createJson(folderPath, fileName, content):
    """
    Creates a JSON file with the specified content.
    :param folderPath: The folder path where the file is located.
    :param fileName: The name of the file to create.
    :param content: The content to write to the file.
    """
    try:
      if not folderPath or not fileName:
        raise ValueError("Folder path or file name cannot be empty.")
      fullPath = os.path.join(folderPath,fileName) + ".json"
      if os.path.exists(fullPath):
        raise ValueError(f"File '{fullPath}' already exists.")
      else:
        with open(fullPath, 'w') as jsonFile:
          json.dump(content, jsonFile, indent=4)
    except Exception as e:
        print("Error:", str(e))

  def readJson(folderPath, fileName):
    """
    Reads a JSON file and returns its content as a dictionary.
    :param folderPath: The folder path where the file is located.
    :param fileName: The name of the file to read.
    :return: The content of the file as a dictionary.
    """
    try:
      if not folderPath or not fileName:
        raise ValueError("Folder path or file name cannot be empty.")
      fullPath = os.path.join(folderPath,fileName) + ".json"
      if os.path.exists(fullPath):
        with open(fullPath, 'r') as jsonFile:
          content = json.load(jsonFile)
          return content
      else:
        raise ValueError(f"File '{fullPath}' not found.")

    except Exception as e:
        print("Error:", str(e))
        return None

  def updateJson(folderPath, fileName, content):
    """
    Writes a dictionary as a JSON file.
    :param folderPath: The folder path where the file is located.
    :param fileName: The name of the file to write.
    :param content: The content to write to the file.
    """
    try:
      if not folderPath or not fileName:
        raise ValueError("Folder path or file name cannot be empty.")
      fullPath = os.path.join(folderPath,fileName) + ".json"
      with open(fullPath, 'w') as jsonFile:
        json.dump(content, jsonFile, indent=4)
    except Exception as e:
        print("Error:", str(e))

  def deleteJson(folderPath, fileName):
    """
    Deletes a JSON file.
    :param folderPath: The folder path where the file is located.
    :param fileName: The name of the file to delete.
    """
    try:
      if not folderPath or not fileName:
        raise ValueError("Folder path or file name cannot be empty.")
      fullPath = os.path.join(folderPath,fileName) + ".json"
      if os.path.exists(fullPath):
        os.remove(fullPath)
      else:
        raise ValueError(f"File '{fullPath}' not found.")
    except Exception as e:
        print("Error:", str(e))