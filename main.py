import os
import sys
import time
import json
import requests
from datetime import datetime, timedelta

CONFIG_FILE = "config.json"
KEYS = {
    "GOLIHFVDBDFJJXDHB": 7,
    "HDDHDHHCH-HFHDDHBFF": 30,
    "FSJFBXHZVDB-6474867546": 365
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def check_key():
    config = load_config()
    if "key" in config and "expiry" in config:
        expiry = datetime.strptime(config["expiry"], "%Y-%m-%d")
        if expiry > datetime.now():
            return True
    return False

def check_api_credentials():
    config = load_config()
    return "api_id" in config and "api_hash" in config

def save_api_credentials(api_id, api_hash):
    config = load_config()
    config["api_id"] = api_id
    config["api_hash"] = api_hash
    save_config(config)

def activate_key():
    print("\n🔐 ВВЕДИТЕ КЛЮЧ АКТИВАЦИИ:")
    key = input("➤ ").strip()
    
    if key in KEYS:
        expiry = (datetime.now() + timedelta(days=KEYS[key])).strftime("%Y-%m-%d")
        config = load_config()
        config["key"] = key
        config["expiry"] = expiry
        save_config(config)
        print(f"✅ Ключ активирован! Действует до: {expiry}")
        return True
    else:
        print("❌ Неверный ключ!")
        return False

def setup_api_credentials():
    print("\n🔧 ПЕРВОНАЧАЛЬНАЯ НАСТРОЙКА")
    print("Получите API ID и API HASH на my.telegram.org\n")
    
    api_id = input("📱 API ID: ").strip()
    api_hash = input("🔑 API HASH: ").strip()
    
    if api_id and api_hash:
        save_api_credentials(api_id, api_hash)
        print("✅ Данные сохранены!")
        return True
    else:
        print("❌ Ошибка: данные не могут быть пустыми")
        return False

def telegram_spam():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
╔══════════════════════════════════╗
║    TELEGRAM SPAM TGH v1.0        ║
║        PREMIUM EDITION 👑         ║
╚══════════════════════════════════╝
    """)
    
    config = load_config()
    api_id = config["api_id"]
    api_hash = config["api_hash"]
    
    target = input("👤 USERNAME или ID (без @): ").strip()
    message = input("💬 ТЕКСТ СООБЩЕНИЯ: ").strip()
    count = int(input("📊 КОЛИЧЕСТВО СООБЩЕНИЙ: ").strip())
    
    print("\n📝 ГЕНЕРАЦИЯ СКРИПТА...")
    
    spam_code = f'''
import asyncio
import time
from telethon import TelegramClient
from telethon.errors import FloodWaitError

async def spam():
    client = TelegramClient('spam_session', {api_id}, '{api_hash}')
    await client.start()
    
    print("✅ Бот запущен! Отправка начата...")
    
    try:
        entity = await client.get_input_entity('{target}')
    except:
        print("❌ Ошибка: пользователь не найден")
        return
    
    sent = 0
    for i in range({count}):
        try:
            await client.send_message(entity, '{message}')
            sent += 1
            print(f"✓ Отправлено: {{sent}}/{{count}}", end='\\r')
            await asyncio.sleep(0.5)
        except FloodWaitError as e:
            print(f"\\n⚠️ Флуд контроль: ждем {{e.seconds}} сек")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"\\n❌ Ошибка: {{e}}")
    
    print(f"\\n\\n✅ Готово! Отправлено {{sent}} сообщений")
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(spam())
'''
    
    script_path = os.path.join(os.path.dirname(__file__), f"spam_{int(time.time())}.py")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(spam_code)
    
    print(f"\n✅ СКРИПТ СОЗДАН: {script_path}")
    print("\n📦 Установите Telethon:")
    print("pip install telethon")
    print(f"\n🚀 Запустите: python {os.path.basename(script_path)}")
    
    input("\nНажмите Enter для меню...")

def main():
    # Проверяем наличие API данных при первом запуске
    if not check_api_credentials():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
╔══════════════════════════════════╗
║    TELEGRAM SPAM TGH v1.0        ║
║        PREMIUM EDITION 👑         ║
╚══════════════════════════════════╝
        """)
        print("\n⚠️ API данные не найдены!")
        if not setup_api_credentials():
            print("\n❌ Настройка не завершена. Выход...")
            sys.exit(1)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
╔══════════════════════════════════╗
║    TELEGRAM SPAM TGH v1.0        ║
║        PREMIUM EDITION 👑         ║
╠══════════════════════════════════╣
║ 1. 🚀 СОЗДАТЬ СКРИПТ СПАМА        ║
║ 2. 🔑 АКТИВИРОВАТЬ КЛЮЧ           ║
║ 3. 🔧 СМЕНИТЬ API ДАННЫЕ          ║
║ 4. ℹ️  ИНФОРМАЦИЯ                 ║
║ 0. ❌ ВЫХОД                        ║
╚══════════════════════════════════╝
        """)
        
        if check_key():
            config = load_config()
            expiry = datetime.strptime(config["expiry"], "%Y-%m-%d")
            days_left = (expiry - datetime.now()).days
            print(f"✅ КЛЮЧ АКТИВЕН! Осталось дней: {days_left}\n")
        else:
            print("❌ КЛЮЧ НЕ АКТИВИРОВАН!\n")
        
        choice = input("➤ ВЫБЕРИТЕ: ")
        
        if choice == "1":
            if check_key():
                telegram_spam()
            else:
                print("\n❌ СНАЧАЛА АКТИВИРУЙТЕ КЛЮЧ!")
                time.sleep(2)
        
        elif choice == "2":
            if activate_key():
                time.sleep(2)
        
        elif choice == "3":
            setup_api_credentials()
            time.sleep(2)
        
        elif choice == "4":
            config = load_config()
            print("\n📋 ИНФОРМАЦИЯ:")
            if "api_id" in config:
                print(f"📱 API ID: {config['api_id']}")
                print(f"🔑 API HASH: {config['api_hash'][:5]}...{config['api_hash'][-5:]}")
            if "key" in config:
                print(f"🔐 КЛЮЧ: {config['key']}")
                print(f"📅 ДЕЙСТВУЕТ ДО: {config['expiry']}")
            input("\nНажмите Enter...")
        
        elif choice == "0":
            print("\n👋 ВЫХОД...")
            sys.exit(0)

if __name__ == "__main__":
    main()
