# Imports
import os
import json

class CrudFile:

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