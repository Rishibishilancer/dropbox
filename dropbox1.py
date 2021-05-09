import requests
import json
headers = {"Authorization": "Bearer ya29.a0AfH6SMBOxdco3Ekz4uQU8qmOUqP9J8rBZxYmlnEGpqB9L4SLO-cp0OhR2dRR1xoaDrFsRXPrF9O_1J265ymG6rYZVAcIn6PMqDePGqZTDLZZoznmk3Pj2tGN5p5olSyyqIW5ZcDp9wi8bl0-k19HD8YViYMy" } #put ur access token after the word 'Bearer '
para = {
    "name": "test2.txt", #file name to be uploaded
    "parents": ["1CtwUunK-H7XmyvVZ08qMOKomrGUsIomO"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('image/png',open("/Users/rishibishilancer/Downloads/IMG_1626.JPG", "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)


    