# Anti-Whale & Gas Oracle Logic 🍋

from dotenv import load_dotenv
import os
import json

# Зареждане на конфигурация
load_dotenv()

WHALE_LIMIT = int(os.getenv("WHALE_LIMIT", "1000"))
LOW_FEE = int(os.getenv("LOW_FEE", "20"))

def process_data(amount, gas_price):
    """
    Обработка на транзакция за закупуване на фи
    
    Args:
        amount: Размерност на транзакцията
        gas_price: Gas цена на мрежата
        
    Returns:
        str: Статус на обработката
    """
    if amount > WHALE_LIMIT:
        return "🚨 Whale Alert! Transaction exceeds limit."
    if gas_price <= LOW_FEE:
        return "✅ Low Fee - Processed!"
    return "⏳ Waiting for better gas price..."

def classify_trader(amount):
    """Класификация на трейдър по размер на транзакция"""
    if amount <= 200:
        return "Small Player"
    elif amount <= 400:
        return "Mid-Whale"
    elif amount <= WHALE_LIMIT:
        return "Large Whale"
    else:
        return "🚨 MEGA WHALE"

# Тест
if __name__ == "__main__":
    print("=== Anti-Whale Test Suite ===\n")
    
    # Тест 1: Малка транзакция
    result = process_data(500, 15)
    print(f"Test 1 (500 tokens, 15 gas): {result}")
    
    # Тест 2: Whale транзакция
    result = process_data(2000, 25)
    print(f"Test 2 (2000 tokens, 25 gas): {result}")
    
    # Тест 3: Класификация
    print("\n=== Trader Classification ===")
    for amount in [100, 250, 600, 1500]:
        classification = classify_trader(amount)
        print(f"{amount} tokens: {classification}")
