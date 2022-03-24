import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
        
def main():
    access_token = 'sl.BEYUaygprQWB-SPdXsqJYAotGAw5u4RApoOs08MkhpV1rUCdB2Nj7Y663wjf4aYqsYohzmqb8WySTeZvrR2osJgmD_NK_rMzjzh8dBFJg12-urckWleX402tLcPsHxsbKm3PUUZWDcKM'
    transferData=TransferData(access_token)

    file_from = input("enter the folder to upload ")
    file_to = input("enter the full path to upload dropbox ")  
    transferData.upload_file(file_from,file_to)
    print("Folder has been moved")


main()    

   
    

