
import os

def main():
    env = os.getenv("APP_ENV", "development")
    print(f"Running application in {env} environment")

if __name__ == "__main__":
    main()
