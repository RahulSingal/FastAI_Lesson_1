# ------------------------------------------------------------------------------------------------------------
# | Programmer: Rahul Singal
# | File Name: functions.py
# | Date Created: 10/16/2024 
# | Date Last Modified: 10/26/2024
# | Description: This will hold all the function definitions
# ------------------------------------------------------------------------------------------------------------

import library # Importing the library.py file

#  -------------------------------------------------------------------------------------------
# | Function Name:      search_ddg
# | Description:        It will search and return a single image from the inputed search term using duck duck go
# | Input Parameters:   (str) search_term, (int) max_images
# | Returns:            Returns images from the search term for the max number of images up to 30
#  -------------------------------------------------------------------------------------------
def search_ddg(search_terms, max_images=30):
  print(f"Searching for ' {search_terms}'")
  ddgs = DDGS()
  return L(ddgs.images(search_terms, max_results=max_images)).itemgot('image')

#  -------------------------------------------------------------------------------------------
# | Function Name:      multiple_searches
# | Description:        It will take in a tuple of the search categories and then search, download, resizes, and stores them in a directory
# | Input Parameters:   (tuple) searches, (str) output_path_name, (int) max_images
# | Returns:            Returns a directory path of where the searched images are stored
#  -------------------------------------------------------------------------------------------
def multiple_searches(searches, output_path_name, max_images=30):
    path = Path(output_path_name)
    for o in searches:
        dest = (path/o)
        dest.mkdir(exist_ok=True, parents=True)
        download_images(dest, urls=search_ddg(f'{o} photo', max_images=100))
        resize_images(path/o, max_size=400, dest=path/o)
    return path

#  -------------------------------------------------------------------------------------------
# | Function Name:      delete_corrupted_images
# | Description:        It will take in a path to a directory of images and verify the validitiy of each, for the ones that failed,
# |                     it will delete using the unlink function and then finally print out the number of failed images
# | Input Parameters:   (tuple) searches, (str) output_path_name, (int) max_images
# | Returns:            Returns a directory path of where the searched images are stored
#  -------------------------------------------------------------------------------------------
def delete_corrupted_images (image_path):
  failed = verify_images(get_image_files(image_path))
  failed.map(Path.unlink)
  print(len(failed))


