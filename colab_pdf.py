'''
This code is from https://github.com/brpy/colab-pdf/blob/master/colab_pdf.py
'''

def colab_pdf(file_name, notebookpath = '/content/drive/My Drive/Colab Notebooks/'):
  import os
  filepath = notebookpath + file_name
  if(not isinstance(file_name,str)):
    raise TypeError(f"expected a string as file_name, but got {type(file_name)} instead.")
  
  drive_mount_point = '/content/drive/'
  gdrive_home = os.path.join(drive_mount_point, 'My Drive/')
  
  if(not os.path.isdir(gdrive_home)):
    from google.colab import drive
    drive.mount(drive_mount_point)

  if(not os.path.isfile(os.path.join(notebookpath,file_name))):
    raise ValueError(f"file '{file_name}' not found in path '{notebookpath}'.")

  get_ipython().system("apt update && apt install texlive-xetex texlive-fonts-recommended texlive-generic-recommended")
  
  if(os.path.isfile(os.path.join(gdrive_home,file_name.split('.')[0] + '.pdf'))):
    os.remove(os.path.join(gdrive_home,file_name.split('.')[0] + '.pdf'))
  
  try:
    get_ipython().system("jupyter nbconvert --to PDF filepath")
  except:
    return("nbconvert error")
  
  try:
    from google.colab import files
    file_name = file_name.split('.')[0] + '.pdf'
    files.download(gdrive_home+file_name)
  except:
    return("File Download Unsuccessful. Saved in Google Drive")
  
  return("File ready to be Downloaded and Saved to Drive")
