import os

# Funtion to create an folder 

print('───── ❝ 𝐚𝐛𝐨𝐮𝐭 𝐦𝐞 ❞ ─────')

text ='''
░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█

'''

print(text)

def createfunciton(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()

# We are creating this function so that it won't remove the original extension file

files.remove('Files_in_Folder_Arrange.py')

# Calling the funtion to crate different folder

createfunciton('images')
createfunciton('zip')
createfunciton('medias')
createfunciton('documents')
createfunciton('others')
createfunciton('excel')

# Funtion for moving files of above created folder's

def move(foldername, files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")
    
'''
Here we are mentioning the different file extensions
'''

imageexts = ['.jpg','.jpeg','.avif','.GIF','.PNG','.BMP','.svg','.ai','.heif','.cr2','.PSD','.RAW']
images_ = [file for file in files if os.path.splitext(file)[1].lower() in imageexts ]

docexts = ['.docx','.txt','.doc','.pdf','.ppt','pptx','odp','.key']
documents_ = [file for file in files if os.path.splitext(file)[1].lower() in docexts]

mediaexts = ['.mp4','.vlc','.flv','.mp3','.wav']
medias_ = [file for file in files if os.path.splitext(file)[1].lower() in mediaexts]

zipexts = ['.zip','.rar']
zip_ = [file for file in files if os.path.splitext(file)[1].lower() in zipexts]

excel = ['.xlsx','.xlsm','.xlsb','.xltx']
excel_ = [file for file in files if os.path.splitext(file)[1].lower() in excel]

# other folder if for the file extension is not matched on the top 

others_ = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imageexts) and (ext not in mediaexts) and (ext not in zipexts) and os.path.isfile(file):
        others_.append(file)


# Calling function to move the respective files on these folder


move("images", images_)
move("zip", zip_)
move("medias", medias_)
move("documents", documents_)
move("images", images_)
move("others", others_)
move("excel", excel_)


print('Thank You for using this pyhton script')

temp_1 = '''
────────────────────────────────
───────────────██████████───────
──────────────████████████──────
──────────────██────────██──────
──────────────██▄▄▄▄▄▄▄▄▄█──────
──────────────██▀███─███▀█──────
█─────────────▀█────────█▀──────
██──────────────────█───────────
─█──────────────██──────────────
█▄────────────████─██──████
─▄███████████████──██──██████ ──
────█████████████──██──█████████
─────────────████──██─█████──███
──────────────███──██─█████──███
──────────────███─────█████████
──────────────██─────████████▀
────────────────██████████
────────────────██████████
─────────────────████████
──────────────────██████████▄▄
────────────────────█████████▀
─────────────────────████──███
────────────────────▄████▄──██
────────────────────██████───▀
────────────────────▀▄▄▄▄▀
'''
print(temp_1)
