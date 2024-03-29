import hashlib,logging, random, time, os
from datetime import datetime

os.makedirs("logs", exist_ok=True)  # verifie si le dossier logs existe sinon le creer


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/" + (datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')) + ".log","w",'utf-8')
root_logger.addHandler(handler)

def md5(string: str):
    """Enchiffrement du mot de passe en md5"""
    return hashlib.md5(bytes(string, 'utf-8')).hexdigest()


def sha256(string: str):
    """Enchiffrement du mot de passe en sha256"""
    return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()


def sha512(string: str):
    """Enchiffrement du mot de passe en sha512"""
    return hashlib.sha512(bytes(string, 'utf-8')).hexdigest()


def sha1(string: str):
    """Enchiffrement du mot de passe en sha1"""
    return hashlib.sha1(bytes(string, 'utf-8')).hexdigest()


def hasheur_random(lst: list):
    """Hash le fichier de mot de passe en clair afin de faire la démo"""
    mp_hash = []
    for i in lst:
        choix = random.randint(1, 4)
        if choix == 1:
            mp_hash.append(md5(i))
        elif choix == 2:
            mp_hash.append(sha1(i))
        elif choix == 3:
            mp_hash.append(sha256(i))
        else:
            mp_hash.append((sha512(i)))
    return mp_hash


class DictionnaireAttaque:
    """Ensemble de fonctions des attaques de dictionnaire
    """

    def __init__(self, target: str, lst_pwd: str, lst_pwd_decrypter) -> None:
        """Constructeur des variables de la classe DictionnaireAttaque

        Args:
            target (str): Mot de passe chiffre
            lst_pwd (str): Liste des mots de passe en clair
            lst_pwd_decrypter (list): Liste des mots de passe chiffrer 
        """
        self.Target = target  # mot de passe chiffre
        self.Len_Target = len(self.Target) if type(self.Target) == str else 0  # taille du mp
        self.PassWord_List = []  # liste des mots de passes possibles en clair
        self.PassWord_File = lst_pwd  # nom du fichier
        self.__DecryptedTarget = None  # statut du mot de passe
        self.lst_pwd_decrypter = lst_pwd_decrypter

        # Methode primaire
        self.open_files()
        logging.info("Started")
        logging.info(f"Fichier {self.PassWord_File} ouvert ")

    def open_files(self):
        """Ouvre et copie dans la variable Password_List les mots de passes en clairs"""
        try:
            with open(self.PassWord_File, 'r') as files:
                for i in files:
                    self.PassWord_List.append(i[:-1])
        except:
            print("Erreur, chemin de fichier incorrect ! ")

    def Dictionnaire_Md5(self):
        """Chiffre et compare un mot de passe clair en MD5, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if md5(index) == self.Target:
                self.__DecryptedTarget = (index, 'MD5', md5(index))

        return False

    def Dictionnaire_Sha1(self):
        """Chiffre et compare un mot de passe clair en SHA1, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if sha1(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-1', sha1(index))

        return False

    def Dictionnaire_Sha256(self):
        """Chiffre et compare un mot de passe clair en SHA256, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if sha256(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-256', sha256(index))

        return False

    def Dictionnaire_Sha512(self):
        """Chiffre et compare un mot de passe clair en SHA512, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if sha512(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-512', sha512(index))

        return False

    def dechiffrement(self):
        """
        Tentative de dechiffrer le mot de passe en essayant les differents encodage
        """
        logging.info(f"Dechiffrement en cours hash : {self.Target}")
        self.Dictionnaire_Md5()
        self.Dictionnaire_Sha1()
        self.Dictionnaire_Sha256()
        self.Dictionnaire_Sha512()

    def dechiffrement_liste(self):
        """ Permet le déchiffrement d'une liste de mot de passe hashé
        """
        cpt = 0
        time_1 = time.time()
        try:
            for val in self.lst_pwd_decrypter:
                self.Target = val
                self.dechiffrement()
                self.afficher()

                cpt += 1
        except TypeError:
            logging.warning("dechiffrement_liste erreur, utilisez dechiffrement()")
            print("dechiffrement_liste erreur, utilisez dechiffrement()")
        chrono = time.time() - time_1
        logging.info(f"END : {cpt} mot de passes cherché en {chrono} secondes ")
        print(f"END : {cpt} mot de passes cherché en {chrono} secondes")

    def afficher(self):
        """Affichage des résultats en direct"""
        if self.__DecryptedTarget is None:
            # print(f"Le mot de passe {self.Target} n'est soit pas dans la liste ou l'algorithme de chiffrement n'est pas supporté ! ")
            logging.info("brute_force : FAIL ")
            return f"Le mot de passe {self.Target}n'est soit pas dans la liste ou l'algorithme de chiffrement n'est pas supporté ! "
        else:
            # print(f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}")
            logging.info(
                f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}")
            return f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}"


class AttaqueBruteForce:
    def __init__(self, hash, algo_chiffrement ) :
        
        self.caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                           'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
                           '5', '6', '7', '8', '9', ',', '?', ';', '.', ':', '/', '!', '§', 'ù', '%', '*',
                           'µ', '$', '£', '^', '¨', '&', 'é', '~', '#', "'", '(', '[', '-', '|', 'è', '`', '_', '\\',
                           'ç', '^', 'à', '@', ')', ']', '°', '+', '=', '}', '"']
        self.hash = hash
        self.algo_chiffrement = algo_chiffrement
        self.caracteres_minimum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_']
        
    def Brute_Force(self, mot : str ):
        """Fonction brute force 

        Args:
            mot (str): _description_

        Returns:
            _type_: _description_
        """
        run = True
        taille = 1 
        while run:
            match self.algo_chiffrement:
                case "SHA-256":
                      for lettres in self.caracteres_minimum:
                        if sha256(mot + lettres) == self.hash  :
                            hash_dechiffre = mot + lettres 
                            run = False
                            return hash_dechiffre
                        else : 
                            mot = mot + lettres
                            taille += 1 
                            #print(mot)
                            print(sha256(mot))

                


