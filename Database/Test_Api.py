from gradio_client import Client
from Starting_File import Starting_File


class API:
    def __init__(self,data=None):
        self.data = data

    
    def talk(self):
        result = self.get_data(self.data)
        temp = result.split(";")
        temp = [x for x in temp if len(x) >= 3]
        return_value = []
        ss = Starting_File()
        for item in temp:
            item = item.lstrip()
            return_value.append(ss.get_input(item))
        return return_value[len(return_value)-1]


    def get_data(self,data):
        client = Client("http://localhost:8001/")
        result = client.predict(
            self.data,  # str  in 'Message' Textbox component
            'LLM Chat',  # Literal[Query Docs, Search in Docs, LLM Chat]  in 'Mode' Radio component
            ["https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf"],
            # List[filepath]  in 'Upload File(s)' Uploadbutton component
            "Hello!!",  # str  in 'System Prompt' Textbox component
            api_name="/chat"
        )
        return result

if __name__ == "__main__":
    a = API()
    a.talk()