import requests
from requests.auth import HTTPBasicAuth
import os

# Remplacez ces variables par vos informations personnelles
GITHUB_USERNAME = 'alphamouhamadou'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    raise EnvironmentError("Le token GITHUB_TOKEN n'est pas défini dans les variables d'environnement.")
REPO_NAME = 'exam_outils_versioningIA'
DESCRIPTION = 'Ceci est un dépôt créé par l\'API Rest de Github'

# URL de base pour l'API Github
BASE_URL = 'https://api.github.com'

# Fonction pour créer un dépôt
def create_github_repo(repo_name, description):
    url = f'{BASE_URL}/user/repos'
    payload = {
        'name': repo_name,
        'description': description,
        'private': False  
    }
    response = requests.post(url, json=payload, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
    
    if response.status_code == 201:
        print(f'Dépôt {repo_name} créé avec succès.')
        return response.json()
    else:
        print(f'Échec de la création du dépôt: {response.status_code}')
        print(response.json())
        return None

# Fonction pour créer un issue
def create_github_issue(repo_name, title, body):
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}/issues'
    payload = {
        'title': title,
        'body': body
    }
    response = requests.post(url, json=payload, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
    
    if response.status_code == 201:
        print(f'Issue "{title}" créé avec succès.')
        return response.json()
    else:
        print(f'Échec de la création de l\'issue: {response.status_code}')
        print(response.json())
        return None

# Créer le dépôt
repo = create_github_repo(REPO_NAME, DESCRIPTION)

# Si le dépôt a été créé avec succès, créer deux issues
if repo:
    create_github_issue(REPO_NAME, 'Issue 1', 'Description de la première issue.')
    create_github_issue(REPO_NAME, 'Issue 2', 'Description de la deuxième issue.')
    

# EXERCICE 3

# Concept des Git worktrees

# Le concept des Git worktrees permet aux utilisateurs de Git de travailler sur plusieurs branches en même temps sans avoir à changer de branche dans le même répertoire de travail. Cela est particulièrement utile lorsque vous souhaitez travailler sur différentes branches sans avoir à commettre ou à stasher vos modifications dans l'une des branches pour passer à une autre.

# Qu'est-ce qu'un Git worktree ?
# Un Git worktree est un répertoire supplémentaire associé à votre dépôt Git, permettant de vérifier différentes branches dans des répertoires distincts. Chaque worktree partage le même historique de commits et les mêmes objets Git, mais vous pouvez y travailler sur une branche différente.

# Pourquoi utiliser les worktrees ?
# Travail simultané sur plusieurs branches : Vous pouvez travailler sur une branche dans un worktree tout en travaillant sur une autre branche dans un autre worktree, sans avoir à changer de branche ou à gérer des conflits de changement.
# Facilité pour tester ou corriger des bugs : Si vous êtes en train de développer une fonctionnalité sur une branche, mais que vous devez rapidement appliquer un correctif sur une autre branche, vous pouvez créer un worktree pour la branche de correctif sans perturber votre travail en cours.

# Exemples pratiques d'utilisation des worktrees
# 1. Créer un worktree :
# Imaginons que vous travaillez sur la branche feature-a mais que vous avez besoin de basculer temporairement sur la branche bugfix-1 pour corriger un bug. Au lieu de changer de branche dans le même répertoire, vous pouvez créer un worktree.

# bash
# # Créer un nouveau worktree pour la branche bugfix-1
# git worktree add ../bugfix-1 bugfix-1
# Cette commande crée un nouveau répertoire ../bugfix-1 qui est une copie de votre dépôt, mais vérifie la branche bugfix-1.
# Vous pouvez maintenant travailler sur bugfix-1 dans le répertoire ../bugfix-1 tout en continuant à travailler sur feature-a dans le répertoire original.

# 2. Liste des worktrees existants :
# Pour voir tous les worktrees associés à votre dépôt, vous pouvez utiliser la commande suivante :

# bash
# git worktree list
# Cela affichera une liste de tous les répertoires de worktree, ainsi que la branche actuellement vérifiée dans chacun.

# 3. Supprimer un worktree :
# Une fois que vous avez terminé de travailler dans un worktree, vous pouvez le supprimer :

# bash
# git worktree remove ../bugfix-1
# Cela supprime le répertoire ../bugfix-1 tout en laissant intactes toutes les modifications que vous avez commités dans la branche bugfix-1.

# Avantages des worktrees
# Isolation des branches : Vous pouvez travailler sur plusieurs branches isolées les unes des autres, évitant ainsi les conflits et les erreurs potentielles.
# Gain de temps : Vous n'avez pas besoin de stasher ou de commettre des modifications en cours lorsque vous devez basculer temporairement sur une autre branche.

# Conclusion
# Les Git worktrees sont un outil puissant pour les développeurs qui travaillent sur des projets complexes avec plusieurs branches actives. Ils permettent une gestion efficace des branches en isolant les environnements de travail tout en partageant le même historique de dépôt. L'utilisation de worktrees est particulièrement bénéfique dans des scénarios où vous devez basculer fréquemment entre les branches ou tester des modifications sans perturber votre environnement de développement principal.
