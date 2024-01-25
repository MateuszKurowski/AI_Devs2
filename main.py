from tasks import helloapi, moderation, blogger, liar, inprompt, embedding

def main():
    try:
        # helloapi.main()
        # moderation.main()
        # blogger.main()
        # liar.main()
        # inprompt.main()
        embedding.main()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()