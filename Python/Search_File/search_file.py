import os

def find_files(filename, search_path):
    #Initialising an emtpy list
   result = [
       os.path.join(root, filename)
       for root, dir, files in os.walk(search_path) if filename in files
   ]
   return "No file found" if not result else result

if __name__ == '__main__':
    filename = input("Pleasee enter the full name of the file with extension if any: \n")
    path = input("Please enter the path in which you want to search: \n")
    print(find_files(filename, path))