from Google import Create_Service, download_file_from_google_drive
import PyPDF2
import gdown
import os

CLIENT_SECRET_FILE = "C:/Users/91885/Downloads/client_secret.json"
API_NAME='drive'
API_VERSION="v3"
SCOPES=['https://www.googleapis.com/auth/drive']


print("1")
service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

link = "https://drive.google.com/drive/u/0/folders/1mXNl5UghGKCoMcEmM_LsuLAgmhaLazbk"
folder_id = link.split('/')[-1]

print(folder_id)

# folder_id = "1mxruNd_sUF-0RbWYTsc_2_7AKvHLZ9zq"
# folder_id = "1ZScp_HrRGzcuWySZP8diS4sN5sFsU5d8"
# folder_id="1mXNl5UghGKCoMcEmM_LsuLAgmhaLazbk"

try:

    query = f"parents = '{folder_id}'"
    response = service.files().list(q=query).execute()
    files = response.get('files')
    nextPageToken = response.get('files')
    for read in files:
        print("------",read)
        output_file = read["name"]
        file_id = read["id"]
        # destination = "E:/streamlit-tut/read_pdf"
        # download_file_from_google_drive(file_id,destination)
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, fuzzy=True, quiet=False)
        
    
        with open(output_file, 'rb') as pdfs:
            text = ''
            pdfReader = PyPDF2.PdfReader(pdfs)
            for page in pdfReader.pages:
                text += page.extract_text()
        
        
            print(text)       
        os.remove(output_file)
        
except PermissionError as e:
    print(str(e))
        

    