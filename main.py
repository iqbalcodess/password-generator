import argparse
import secrets
import string


def generate_password(length: int = 16, include_symbols: bool = True) -> str:
    character_groups = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if include_symbols:
        character_groups.append(string.punctuation)

    if length < len(character_groups):
        raise ValueError(f"Length must be at least {len(character_groups)} characters.")

    password_characters = [secrets.choice(group) for group in character_groups]
    available_characters = "".join(character_groups)
    password_characters.extend(
        secrets.choice(available_characters)
        for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a strong random password.")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="password length (default: 16)",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="exclude punctuation symbols",
    )
    args = parser.parse_args()

    try:
        password = generate_password(args.length, include_symbols=not args.no_symbols)
    except ValueError as error:
        parser.error(str(error))

    print(password)


if __name__ == "__main__":
    main()