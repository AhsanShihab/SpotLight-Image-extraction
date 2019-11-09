# SpotLight-Image-extraction
This is a fun project to automate the extraction of windows spotlight images into jpeg format at a desired directory using python.


You can clone or download the whole repository in your local machine (must be a windows 10 machine) and run the SpotLight_Image_Extractor.py file.

## Create .exe file

Have pyinstaller installed on your machine. Then, in the directory of SpotLight_Image_Extractor.py file, run 'cmd' or 'powershell' and write this following code,

>pyinstaller --onefile -w SpotLight_Image_Extractor.py

In the created 'dist' folder, copy the 'background.png' and 'button_start-extracting.png' files for the GUI to work properly.
