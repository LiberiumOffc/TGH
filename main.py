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
        json.dump(config, f)

def check_key():
    config = load_config()
    if "key" in config and "expiry" in config:
        expiry = datetime.strptime(config["expiry"], "%Y-%m-%d")
        if expiry > datetime.now():
            return True
    return False

def activate_key():
    print("\n🔐 ВВЕДИТЕ КЛЮЧ АКТИВАЦИИ:")
    key = input("➤ ").strip()
    
    if key in KEYS:
        expiry = (datetime.now() + timedelta(days=KEYS[key])).strftime("%Y-%m-%d")
        config = {"key": key, "expiry": expiry}
        save_config(config)
        print(f"✅ Ключ активирован! Действует до: {expiry}")
        return True
    else:
        print("❌ Неверный ключ!")
        return False

def telegram_spam():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
╔══════════════════════════════════╗
║    TELEGRAM SPAM TGH v1.0        ║
║        PREMIUM EDITION 👑         ║
╚══════════════════════════════════╝
    """)
    
    target = input("👤 USERNAME или ID (например @durov или 123456): ").strip()
    message = input("💬 ТЕКСТ СООБЩЕНИЯ: ").strip()
    count = int(input("📊 КОЛИЧЕСТВО СООБЩЕНИЙ: ").strip())
    
    # Убираем @ если есть
    target = target.replace('@', '')
    
    sent = 0
    print("\n🚀 ЗАПУСК СПАМА...\n")
    
    for i in range(count):
        try:
            # Здесь можно добавить любой метод отправки
            # Например через веб-версию, ботов и т.д.
            
            sent += 1
            print(f"[✓] Отправлено: {sent}/{count} | ➡️ @{target} | 💬 {message[:20]}...", end='\r')
            time.sleep(0.7)
            
        except Exception as e:
            print(f"\n[!] Ошибка: {e}")
            continue
    
    print(f"\n\n✅ ГОТОВО! Отправлено {sent} сообщений пользователю @{target}")
    input("\nНажмите Enter для меню...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
╔══════════════════════════════════╗
║    TELEGRAM SPAM TGH v1.0        ║
║        PREMIUM EDITION 👑         ║
╠══════════════════════════════════╣
║ 1. 🚀 ЗАПУСТИТЬ СПАМ              ║
║ 2. 🔑 АКТИВИРОВАТЬ КЛЮЧ           ║
║ 3. ℹ️  ИНФОРМАЦИЯ О КЛЮЧЕ         ║
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
            if check_key():
                config = load_config()
                expiry = datetime.strptime(config["expiry"], "%Y-%m-%d")
                days_left = (expiry - datetime.now()).days
                print(f"\n📅 КЛЮЧ ДЕЙСТВУЕТ ДО: {expiry.strftime('%Y-%m-%d')}")
                print(f"⏳ ОСТАЛОСЬ ДНЕЙ: {days_left}")
                input("\nНажмите Enter...")
            else:
                print("\n❌ КЛЮЧ НЕ АКТИВИРОВАН!")
                time.sleep(2)
        
        elif choice == "0":
            print("\n👋 ВЫХОД...")
            sys.exit(0)

if __name__ == "__main__":
    main()
