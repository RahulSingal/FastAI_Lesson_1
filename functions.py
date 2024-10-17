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

  #  -------------------------------------------------------------------------------------------
# | Function Name:      create_dataloaders
# | Description:        TBD
# | Input Parameters:   TBD
# | Returns:            TBD
#  -------------------------------------------------------------------------------------------
def create_dataloaders(path, img_size=192, valid_pct=0.2, batch_size=32, seed=42):
  dblock = DataBlock(
      blocks=(ImageBlock, CategoryBlock),
      get_items=get_image_files,
      splitter=RandomSplitter(valid_pct=valid_pct, seed=seed),
      get_y=parent_label,
      item_tfms=[Resize(img_size, method='squisj')]
  )

  dls = dblock.dataloaders(path, bs=batch_size)
  dls.show_batch(max_n=6)
  return dls

#  -------------------------------------------------------------------------------------------
# | Function Name:      train_classifier
# | Description:        TBD
# | Input Parameters:   TBD
# | Returns:            TBD
#  -------------------------------------------------------------------------------------------
def train_classifier(dls, model_arch=resnet18, metrics=[error_rate], epochs=3):
  learn = vision_learner(dls, model_arch, metrics=metrics)
  learn.fine_tune(epochs)
  return learn

#  -------------------------------------------------------------------------------------------
# | Function Name:      test_classifier
# | Description:        TBD
# | Input Parameters:   TBD
# | Returns:            TBD
#  -------------------------------------------------------------------------------------------
def test_classifier(learn, search_term, max_images=1, image_size=[256, 256], show_image=True):
  image_url = search_ddg(f'{search_term} photo', max_images=max_images)[0]
  image_path = f'{search_term.replace(" ", "_")}.jpg'
  download_url(image_url, image_path, show_progress=False)
  img = Image.open(image_path).to_thumb(*image_size)
  display(img)
  is_class,_, probs = learn.predict(PILImage.create(image_path))
  print(f"This is predicted as: {is_class}.")
  print(f"Probability it's a {search_term}: {probs[1]:.4f}")





