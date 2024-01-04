from tasks import helloapi, moderation, blogger

def main():
    try:
        # helloapi.main()
        moderation.main()
        # blogger.main()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()