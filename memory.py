import json

class Memory:
    def __init__(self, json_file: str):
        self.m_json = json_file
        self._initialize_file()

    def _initialize_file(self):
        try:
            with open(self.m_json, 'r+') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}

                if "History" not in data:
                    data["History"] = []

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except FileNotFoundError:
            with open(self.m_json, 'w') as f:
                json.dump({"History": []}, f, indent=4)

    def load(self):
        with open(self.m_json, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"History": []}

    def save(self, input_text, output_text):
        with open(self.m_json, "r+") as f:
            data = self.load()
            data["History"].append({"user": input_text, "assistant": output_text})
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()