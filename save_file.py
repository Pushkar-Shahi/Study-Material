import base64, os, sys

def save(path, b64_str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = base64.b64decode(b64_str).decode('utf-8')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'Successfully wrote {path}')

if __name__ == '__main__':
    path = sys.argv[1]
    b64_str = sys.argv[2]
    save(path, b64_str)
