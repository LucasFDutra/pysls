from zipfile import ZipFile 
import os 
  
def get_all_file_paths(directory_to_zip): 
    file_paths = [] 
    for root, directories, files in os.walk(directory_to_zip): 
        for filename in files: 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
    return file_paths
  
def zip_files(directory_to_zip, zip_file_name): 
    file_paths = get_all_file_paths(directory_to_zip) 
    with ZipFile(zip_file_name+'.zip','w') as zip: 
        for file in file_paths: 
            zip.write(file) 