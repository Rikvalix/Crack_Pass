# Projet_NSI
Projet NSI fin d'année
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Documentation - Projet NSI</title>
    <link rel="stylesheet" type = "text/css" media="screen" href="style.css">
</head>

<body>
    <h1>Module : chiffrage / dechiffrage </h1>
    <p>Ce module contient des fonctions et des classes pour le craquage de mots de passe à l'aide d'attaques de dictionnaire, permet également le hachage cryptographique.</p>
    <h2>Module utilisé</h2>
    <ul class="decal">
        <li><code>Tkinter</code> : Interface graphique</li>
        <li><code>Logging</code> : Logs du programme</li>
        <li><code>hashlib</code> : Chiffrement des chaines de caractères</li>
    </ul>
    <div class="decal">
    <form action="https://github.com/Rikvalix/Projet_NSI" method="get" target="_blank">
        <button class="cssbuttons-io" >
            <span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"></path><path fill="currentColor" d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z"></path></svg> Code</span>
          </button>
      </form></div>
    <h2>Fonctions :</h2>
    <ul class="decal">
        <li><code>md5(string: str) -> str</code> : Enchiffre le mot de passe en MD5 et retourne le hash en tant que chaîne de caractères.</li>
        <li><code>sha256(string: str) -> str</code> : Enchiffre le mot de passe en SHA256 et retourne le hash en tant que chaîne de caractères.</li>
        <li><code>sha512(string: str) -> str</code> : Enchiffre le mot de passe en SHA512 et retourne le hash en tant que chaîne de caractères.</li>
        <li><code>sha1(string: str) -> str</code> : Enchiffre le mot de passe en SHA1 et retourne le hash en tant que chaîne de caractères.</li>
        <img src="documentation/assets/md5_exemple.PNG">
        <hr>
        <li><code>hasheur_random(lst: list) -> list</code> : Hash le fichier de mots de passe en clair en utilisant des algorithmes de hachage aléatoires et retourne une liste de hashes correspondants.</li>
        <img src="documentation/assets/hasheur_random.PNG">
    </ul>
    <hr>
    <h2>Classe :</h2>
    <div class = decal>
    <h3>DictionnaireAttaque</h3>
    <p>Cette classe représente une attaque de dictionnaire sur un mot de passe chiffré.</p>
    <h4>Attributs :</h4>
    <ul class = decal>
        <li><code>Target : str</code> : Le mot de passe chiffré cible.</li>
        <li><code>Len_Target : int</code> : La longueur du mot de passe chiffré.</li>
        <li><code>PassWord_List : list</code> : Une liste des mots de passe en clair possibles.</li>
        <li><code>PassWord_File : str</code> : Le nom du fichier contenant les mots de passe en clair.</li>
        <li><code>__DecryptedTarget : tuple</code> : Statut du mot de passe chiffré, contient le mot de passe en clair, l'algorithme de chiffrement et le hash correspondant.</li>
        <li><code>lst_pwd_decrypter : list</code> : Une liste de mots de passe chiffrés à déchiffrer.</li>
    </ul>
    <h4>Méthodes :</h4>
    <ul class = decal>
        <li><code>open_files() -> None</code> : Ouvre et copie les mots de passe en clair à partir du fichier spécifié dans <code>PassWord_File</code> dans la variable <code>Password_List</code>.</li>
        <hr>
        <li><code>Dictionnaire_Md5() -> bool</code> : Chiffre et compare un mot de passe en clair en utilisant l'algorithme MD5. Met à jour <code>__DecryptedTarget</code> si le mot de passe est déchiffré avec succès.</li>
        <li><code>Dictionnaire_Sha1() -> bool</code> : Chiffre et compare un mot de passe en clair en utilisant l'algorithme SHA1. Met à jour <code>__DecryptedTarget</code> si le mot de passe est déchiffré avec succès.</li>
        <li><code>Dictionnaire_sha256() -> bool</code> : Chiffre et compare un mot de passe en clair en utilisant l'algorithme Sha256. Met à jour <code>__DecryptedTarget</code> si le mot de passe est déchiffré avec succès.</li>
        <li><code>Dictionnaire_Sha512() -> bool</code> : Chiffre et compare un mot de passe en clair en utilisant l'algorithme Sha512. Met à jour <code>__DecryptedTarget</code> si le mot de passe est déchiffré avec succès.</li>
        <img src="documentation/assets/dictionnaire_sha1.PNG">
        <hr>
        <li><code>dechiffrement</code> : Tentative de dechiffrer le mot de passe en essayant les differents encodage</li>
        <img src="documentation/assets/dechiffrement.PNG">
        <hr>
        <li><code>dechiffrement_liste</code> : Permet le déchiffrement d'une liste de mot de passe hashé</li>
        <img src="documentation/assets/dechiffrement_liste.PNG">
        <hr>
        <li><code>afficher</code> : affichage des resultats</li>
        <img src="documentation/assets/affichage.PNG">
    </ul>
    </div>
    <hr>
    <h1> Affichage de l'interface</h1>
    <div class="decal">
    <p> Affiche les widgets et permet de chiffrer ou dechiffer un mot de passe grace a une attaque dictionnaire</p>
    <img src="documentation/assets/interface.PNG">
    <hr>
    <h2>Fonctions</h2>
    <ul class = decal>
        <li><code>exit</code> : Ferme l'application</li>
        <li><code>select</code>: Recupere la selection de l'utilisateur dans les check box </li>
        <li><code>clear</code> : supprime les champs de la zone chiffrement </li>
        <li><code>encodage</code> :encode les informations entrer dans le champ et les renvoies </li>
        <li><code>Launch_Demo_Dictionnaire</code> : Enchiffre le fichier password.lst puis le déchiffre a par partir de ce meme fichier</li>
        <li><code>Demo_Dictionaire</code> : Lance la démo de l'attaque dictionnaire</li>
        <li><code>clear_dechiffrement_dictionnaire</code> : Clear le texte des deux consoles</li>
        <li><code>Dechiffrement_dictionnaire</code> : Tente le dechiffrement du hash mis dans la zone de texte et affiche le resultat en console</li>
    </ul>
    <p>Extrait du code tkinter pour l'affichage</p>
    <img src="documentation/assets/tkinter.PNG">
    <hr>
        </div><h2>Logging</h2><div class="decal">
        <p>Consigne les actions effectués dans le programme</p>
        <img src="documentation/assets/logging.PNG">
    </div>
        <h2>Version terminal</h2>
        <img class="decal" src = "documentation/assets/cmd.PNG">       
    </body>
    </html>
