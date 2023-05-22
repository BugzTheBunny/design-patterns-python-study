# SOLID Principles

## S - `SRP` / `SOC` 
`Single Responsibility Principle` AKA `Separation Of Concerns`

A Class should have its own responsibility, and should not take other responsibilities, the only reason to change the class, is if it's related to the primary responsability.

----

## **Try to keep persistance separated**  
for example, the methods in this class are commented out, because in theory, in a big application, you would need to create the same methods for every class, and you might need to change them in all these places afterwards.

```
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.entries_amount = 0
    
    def add_entry(self,entry:str):
        self.entries_amount += 1
        self.entries.append(f"{self.entries_amount} : {entry}")
    
    def remove_entry(self,index:int):
        del self.entries

    def __str__(self):
        return '\n'.join(self.entries)
    
    // Not a good design
    # def save(self,filename:str):
    #     pass
    
    # def load(self,filename:str):
    #     pass
    
    # def load_from_web(self,uri:str):
    #     pass
```
--- 
## O - `OCP`
`Open Close Principle`