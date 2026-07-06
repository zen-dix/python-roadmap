class FileParser:
    def parse(self, data: str):
        raise NotImplementedError()


class JSONParser(FileParser):
    def parse(self, data: str):
        print("[JSON Parser] Extracting keys from document...")


class CSVParser(FileParser):
    def parse(self, data: str):
        print("[CSV Parser] Splitting rows by commas...")


def analyze_data(parser, raw_data):
    parser.parse(raw_data)


analyze_data(JSONParser(), {"user": "gleb", "role": "admin"})
analyze_data(CSVParser(), "id,name,status\n1,gleb,active")
