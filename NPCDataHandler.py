import pickle

class NPCEntry:
    def __init__(self, name, identity, level, stat, species):
        self.name = name
        self.identity = identity
        self.level = level
        self.stat = stat
        self.species = species

def addNPC(newNPC):
    db = {}
    dbfile = None
    try:
        dbfile = open("NPCData", "xb")
        db ={}
    except:
        dbfile = open("NPCData", "rb")
        db = pickle.load(dbfile)
            
    dbfile.close()

    dbfile = open("NPCData", "wb")
            
    print("Adding " + newNPC.name)
    db[newNPC.name] = newNPC
    print(db)
    print(len(db))

    pickle.dump(db, dbfile)
    dbfile.close()

    dbfile = open("NPCData", "rb")
    db = pickle.load(dbfile)
    print("Len " + str(len(db)))
    for keys in db:
        print(keys, "=>", db[keys])
    dbfile.close()