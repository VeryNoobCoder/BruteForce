import hashlib
import time

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(hashed_password, wordlist_path):
    """Brute force to find the original password from a hashed password."""
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
            for idx, word in enumerate(wordlist):
                word = word.strip()  # Remove any whitespace/newline characters
                hashed_word = hash_password(word)
                if hashed_word == hashed_password:
                    return word, idx + 1
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        return None, None

    return None, None

def main():
    print("--- Advanced Password Brute Force Tool ---")
    
    # Simulated hashed password (replace this with your own hash)
    # Original password is "password123"
    hashed_password = "ef92b778bafe771e89245b89ecbc7b6fa2a1b33a08ff2c48cdd7b94dbd4e0c75"
    
    wordlist_path = input("Enter path to the wordlist (e.g., rockyou.txt): ").strip()
    
    print("Starting brute force...")
    start_time = time.time()
    
    found_password, attempts = brute_force(hashed_password, wordlist_path)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if found_password:
        print(f"Password found: '{found_password}'")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
    else:
        print("Password not found in the wordlist.")

if __name__ == "__main__":
    main()
