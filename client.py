import httpx
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--host", default="localhost", type=str)
parser.add_argument("--port", default=8000, type=int)
parser.add_argument("message")

args = parser.parse_args()

resp = httpx.post(f"http://{args.host}:{args.port}/", json={
    "message": args.message,
})

print(resp.json())

