from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

class KarimaAgent:
    """
    Karima — Agente IA spécialisée en prévision de la demande supply chain.
    """

    def __init__(self):
        self.client = Anthropic()
        self.model = "claude-opus-4-6"
        self.conversation_history = []
        self.system_prompt = """
        Tu es Karima, une agente IA experte en supply chain et prévision de la demande, 
        développée par ChainIQ pour les PME marocaines et canadiennes.

        Ton expertise couvre :
        - Prévision de la demande (méthodes statistiques : moyenne mobile, lissage exponentiel, saisonnalité)
        - Calcul du stock de sécurité et point de réapprovisionnement
        - Détection des ruptures de stock et surstock
        - Analyse des tendances et saisonnalité (incluant Ramadan, fêtes marocaines, saisons québécoises)
        - Optimisation des niveaux de stock

        Ton comportement :
        - Tu réponds toujours en français, de façon professionnelle mais accessible
        - Tu poses des questions précises pour mieux comprendre la situation du client
        - Tu donnes des recommandations concrètes et chiffrées quand tu as les données
        - Tu expliques ton raisonnement simplement
        - Tu te souviens du contexte de toute la conversation

        Tu travailles pour des PME industrielles — sois pragmatique, pas théorique.
        """

    def chat(self, user_message: str) -> str:
        """Envoie un message à Karima et obtient une réponse."""
        
        # Ajouter le message de l'utilisateur à l'historique
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Appel à l'API Claude
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        # Extraire la réponse
        assistant_message = response.content[0].text

        # Ajouter la réponse à l'historique
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def reset(self):
        """Réinitialise la conversation."""
        self.conversation_history = []
        print("Conversation réinitialisée.")


# Test direct de Karima
if __name__ == "__main__":
    karima = KarimaAgent()
    
    print("=" * 50)
    print("ChainIQ — Agent Karima (Prévision Demande)")
    print("Tapez 'quit' pour quitter, 'reset' pour recommencer")
    print("=" * 50)
    print()

    while True:
        user_input = input("Vous : ").strip()
        
        if user_input.lower() == "quit":
            print("Au revoir !")
            break
        elif user_input.lower() == "reset":
            karima.reset()
            continue
        elif not user_input:
            continue

        print("\nKarima : ", end="")
        response = karima.chat(user_input)
        print(response)
        print()