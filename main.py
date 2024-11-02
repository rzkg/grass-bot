import asyncio
import random
import ssl
import json
import time
import uuid
from loguru import logger
from websocket import create_connection
from fake_useragent import UserAgent
from urllib.parse import urlparse
import threading

user_agent = UserAgent()
random_user_agent = user_agent.random


def parse_proxy(proxy):
    parsed = urlparse(f"http://{proxy}")
    username = parsed.username
    password = parsed.password
    host = parsed.hostname
    port = parsed.port
    if port is None:
        raise ValueError(f"Port tidak ditemukan dalam proxy: {proxy}")
    return host, port, username, password


def connect_to_wss_http_proxy(proxy, user_id):
    device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, proxy))
    logger.info(f"Device ID: {device_id}")

    host, port, username, password = parse_proxy(proxy)

    while True:
        try:
            time.sleep(random.randint(1, 10) / 10)
            custom_headers = {
                "User-Agent": random_user_agent
            }

            # SSL context setup
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            ws = create_connection(
                "wss://proxy2.wynd.network:4650/",
                http_proxy_host=host,
                http_proxy_port=int(port),
                http_proxy_auth=(username, password),
                header=[f"User-Agent: {custom_headers['User-Agent']}"],
                sslopt={"cert_reqs": ssl.CERT_NONE}
            )

            def send_ping():
                while True:
                    send_message = json.dumps(
                        {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}}
                    )
                    logger.debug(f"Sending: {send_message}")
                    ws.send(send_message)
                    time.sleep(30)

            # Jalankan send_ping dalam thread terpisah
            ping_thread = threading.Thread(target=send_ping, daemon=True)
            ping_thread.start()

            while True:
                response = ws.recv()
                message = json.loads(response)
                logger.info(f"Received: {message}")
                if message.get("action") == "AUTH":
                    auth_response = {
                        "id": message["id"],
                        "origin_action": "AUTH",
                        "result": {
                            "browser_id": device_id,
                            "user_id": user_id,
                            "user_agent": custom_headers['User-Agent'],
                            "timestamp": int(time.time()),
                            "device_type": "extension",
                            "version": "4.26.2"
                        }
                    }
                    logger.debug(f"Auth Response: {auth_response}")
                    ws.send(json.dumps(auth_response))

                elif message.get("action") == "PONG":
                    pong_response = {"id": message["id"], "origin_action": "PONG"}
                    logger.debug(f"Pong Response: {pong_response}")
                    ws.send(json.dumps(pong_response))
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(f"Proxy: {proxy}")
            time.sleep(5)  # Tunggu sebelum mencoba ulang koneksi


async def main():
    with open('users_id.txt', 'r') as file:
        user_ids = file.read().splitlines()

    with open('proxies.txt', 'r') as file:
        proxies = file.read().splitlines()

    loop = asyncio.get_running_loop()
    tasks = []
    for proxy in proxies:
        for user_id in user_ids:
            tasks.append(loop.run_in_executor(None, connect_to_wss_http_proxy, proxy, user_id))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
