import json
import requests
from typing import Any, List, Optional, Union
import base64
class APIClient:
    def __init__(self, server_addr: str):
        self.completions_v1_url = f'{server_addr}/v1/chat/completions'
        self._models_v1_url = f'{server_addr}/v1/models'
        self.model_name = self.get_model_list(self._models_v1_url)[0]

    @staticmethod
    def get_model_list(api_url: str):
        """Get model list from api server."""
        print(api_url)
        response = requests.get(api_url)
        if hasattr(response, 'text'):
            model_list = json.loads(response.text)
            model_list = model_list.pop('data', [])
            print(model_list)
            return [item['id'] for item in model_list]
        return None

    def v1_chat_completions(
            self,
            prompt: Union[str, List[Any]],
            temperature: Optional[float] = 0.0,
            max_tokens: Optional[int] = 2048,
            stream: Optional[bool] = False,
            top_p: Optional[float] = 0.95,
            top_k: Optional[int] = 10,
            repetition_penalty: Optional[float] = 1.15,
            **kwargs):
        pload = {
            'model': self.model_name,
            'messages': prompt,
            'stream': stream,
            'max_tokens': max_tokens,
            'top_k': 1,
            'top_p': top_p,
            'n': 1,
            'temperature': temperature,
            'do_sample': False,
            'temperature': 0.0,
            'repetition_penalty': repetition_penalty,
        }
        headers = {'content-type': 'application/json'}

        response = requests.post(self.completions_v1_url,
                                headers=headers,
                                json=pload,
                                stream=stream)
        for chunk in response.iter_lines(chunk_size=8192,
                                        decode_unicode=False,
                                        delimiter=b'\n'):
            if chunk:
                if stream:
                    decoded = chunk.decode('utf-8')
                    if decoded == 'data: [DONE]':
                        continue
                    if decoded[:6] == 'data: ':
                        decoded = decoded[6:]
                    output = json.loads(decoded)
                    yield output
                else:
                    decoded = chunk.decode('utf-8')
                    output = json.loads(decoded)
                    yield output

if __name__ == "__main__":
    server_addr = "https://shopee.sg/api/v1/compassllvm"
    api_client = APIClient(server_addr)
    prompts=[{
        'role':
        'user',
        'content': [{
            'type': 'text',
            'text': "What is unusual about this image?",
        }, {
            'type': 'image_url',
            'image_url': {
                'url': f"data:image/jpeg;base64,{base64.b64encode(open('images/extreme_ironing.jpg', 'rb').read()).decode('utf-8')}"
            },
        }
        ],
    }]
    stream = False
    if stream:
        for result in api_client.v1_chat_completions(
            prompt=prompts,
            stream=stream):
            print(result)
            text = result['choices'][0].get('delta').get('content')
            if text:
                print(text, end='', flush=True)
        print("\n")
    else:
        for output in api_client.v1_chat_completions(
            prompt=prompts,
            stream=stream):
            print(output['choices'][0]['message']['content'])
