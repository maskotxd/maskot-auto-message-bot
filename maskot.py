from telethon import TelegramClient
import asyncio
import random

api_id = API_ID_BURAYA
api_hash = "API_HASH_BURAYA"

client = TelegramClient("session", api_id, api_hash)

groups = [
    GRUP_ID_1,
    GRUP_ID_2,
    GRUP_ID_3
]

message = "GONDERILECEK_MESAJ"

async def send_loop():
    while True:
        print("Tur başladı...")

        for group in groups:
            try:
                await client.send_message(group, message)
                print(f"Mesaj gönderildi: {group}")

                # 20-30 saniye random delay
                delay = random.randint(20, 30)
                print(f"{delay} saniye bekleniyor...")
                await asyncio.sleep(delay)

            except Exception as e:
                print(f"Hata ({group}): {e}")

        print("Tüm gruplara gönderildi. 10 dakika bekleniyor...\n")

        # 10 dakika bekle (600 saniye)
        await asyncio.sleep(600)

async def main():
    await client.start()
    print("Bot aktif, her şey yolunda.")
    await send_loop()

with client:
    client.loop.run_until_complete(main())