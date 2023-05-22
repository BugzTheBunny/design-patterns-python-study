# SRP / SCP
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.entries_amount = 0

    def add_entry(self, entry: str):
        self.entries_amount += 1
        self.entries.append(f"{self.entries_amount} : {entry}")

    def remove_entry(self, index: int):
        del self.entries

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self,filename:str):
    #     pass

    # def load(self,filename:str):
    #     pass

    # def load_from_web(self,uri:str):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("blabla")
    j.add_entry("kookoo")
    print(f"Entries in Journal:\n{j}")

    PersistenceManager.save_to_file(j, "output.txt")
