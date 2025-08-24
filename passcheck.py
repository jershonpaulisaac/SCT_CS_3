import re

def check_password_strength(password: str):
    checks = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }
    score = sum(checks.values())
    percent = (score / 5) * 100
    strength_levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong",
    }

    text = strength_levels.get(score, "Very Weak")

    return {
        "checks": checks,
        "score": score,
        "percent": percent,
        "strength_text": text
    }


if __name__ == "__main__":
    while True:
        pwd = input("\nEnter a password (or 'e' to quit): ")
        if pwd.lower() == "e":
            break

        if len(pwd) < 8:
            print("Password must be at least 8 characters long.")
            continue

        result = check_password_strength(pwd)
        for key, passed in result["checks"].items():
            print(f"{key.capitalize():<10} : {'Satisfied' if passed else 'Not satisfied'}")
        print(f"Strength: {result['strength_text']} ({result['percent']}%)")
