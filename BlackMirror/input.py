def get_inputs():
    print("🎯 Welcome to BlackMirror – Enter what you know about the target (skip if not available)\n")

    email = input("📧 Enter email: ").strip()
    name = input("🧍 Enter full name: ").strip()
    username = input("👤 Enter username: ").strip()

    inputs = []
    if email:
        inputs.append({"type": "email", "value": email})
    if name:
        inputs.append({"type": "name", "value": name})
    if username:
        inputs.append({"type": "username", "value": username})

    return inputs

if __name__ == "__main__":
    user_inputs = get_inputs()
    print("\n✅ User data received:")
    for item in user_inputs:
        print(f" - {item['type'].capitalize()}: {item['value']}")
