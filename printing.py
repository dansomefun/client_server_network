class Printing:
    @staticmethod
    def print_to_screen(data):
        print("Received data:")
        print(data)

    @staticmethod
    def print_to_file(data, file_path):
        with open(file_path, "w") as f:
            f.write(data)