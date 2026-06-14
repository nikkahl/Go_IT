from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - target_date).days
    except ValueError:
        return None

if __name__ == "__main__":
    print("різниця у днях:", get_days_from_today("2025-12-09"))
