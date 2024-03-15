class Model:
    def __init__(self):
         pass


    def search(self, query, file_path):
        results = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if query.lower() in line.lower():
                        results.append(line.strip())
        except FileNotFoundError:
            print('Faili ei leitud.')
        return results


