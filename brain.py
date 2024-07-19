import g4f
from base_control import Control
controller = Control()

class Brain:


    def __init__(self):
        self.memory = []

    def create_post(self, data, error_try=10):
        response = None
        error = error_try
        while not response:
            try:
                for text in data:
                    self.memory.append({"role": "user", "content": text})
                response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4o,
                    messages=self.memory,
                    stream=False
                )
                self.update_prompt()
            except:
                pass
            error -= 1
            if error <= 0:
                break
        return response

    def update_prompt(self):
        prompt_text = controller.get_setting("gpt_prompt")
        self.memory.clear()
        self.memory.append({"role": "user", "content": prompt_text})