from tasks import helloapi

def main():
    try:
        helloapi.main()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()