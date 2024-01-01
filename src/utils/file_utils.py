import os

class FileUtils:
  
  @staticmethod
  def save_file(file_path: str, content: bytes) -> str:
    filename = os.path.basename(file_path)
    local_path = os.path.join(os.getcwd(), filename)

    with open(local_path, 'wb') as file: # guarda la imagen
      file.write(content)

    return local_path
  
  @staticmethod
  def read_file(file_path: str) -> bytes:
    with open(file_path, 'rb') as file:
      data = file.read()
    return data
  
  @staticmethod
  def remove_file(file_path: str) -> None:
    os.remove(file_path)