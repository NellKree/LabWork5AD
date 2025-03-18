def detect_bots(data):
    print(f"Analyzing data: {data}")
    # Здесь можно добавить
    if "bot" in data.lower():
        return {"status": "detected", "reason": "Bot-like activity"}
    return {"status": "clean"}

if __name__ == "__main__":
    sample_data = "This is a bot activity"
    result = detect_bots(sample_data)
    print(result)