import json

class Memory:
    def __init__(self, json_file: str):
        self.m_json = json_file
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

        with open(self.m_json, "r+") as f:
            try:
                t = json.load(f)
            except json.JSONDecodeError:
                f.seek(0)
                json.dump({"History": []}, f)
                f.truncate()
                t = {"History": []}
            
            if "History" not in t:
                t["History"] = []
                f.seek(0)
                json.dump(t, f, indent=4)
                f.truncate()

    def load(self):
        with open(self.m_json, "r") as f:
            return json.load(f)

    def save(self, input_text, output_text):
        with open(self.m_json, "r+") as f:
            data = json.load(f)
            data["History"].append({"user": input_text, "assistant": output_text})
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
