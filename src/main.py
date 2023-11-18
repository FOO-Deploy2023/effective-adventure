import sys
import os


def get_env(name: str) -> str:
    ENV = os.getenv(name)
    return ENV


def main() -> int:
    print(get_env("DISCORD_TOKEN"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
