from anthropic import Anthropic
from dotenv import load_dotenv
import math

load_dotenv()

class YoussefAgent:
    """
    Youssef — Agent IA specialise en optimisation des stocks et EOQ.
    """

    def __init__(self):
        self.client = Anthropic()
        self.model = "claude-opus-4-6"
        self.conversation_history = []
        self.system_prompt = """
        Tu es Youssef, un agent IA expert en optimisation des stocks et gestion 
        des approvisionnements, developpe par ChainIQ pour les PME marocaines 
        et canadiennes.

        Ton expertise couvre :
        - Calcul EOQ (Economic Order Quantity) dynamique
        - Calcul du stock de securite optimal
        - Determination du point de reapprovisionnement (ROP)
        - Detection et resolution des situations de rupture de stock
        - Detection et resolution des situations de surstock
        - Optimisation des couts de stockage et de commande
        - Gestion multi-produits (SKUs)
        - Analyse ABC des stocks (produits A, B, C)

        Tes formules cles :
        - EOQ = sqrt((2 * D * S) / H)
          D = demande annuelle, S = cout de commande, H = cout de stockage unitaire
        - Stock de securite = Z * sigma * sqrt(L)
          Z = facteur de service, sigma = ecart-type demande, L = delai livraison
        - Point de reappro (ROP) = (demande moyenne * delai) + stock de securite

        Ton comportement :
        - Tu reponds toujours en francais, de facon professionnelle
        - Tu demandes les donnees necessaires avant de calculer
        - Tu CALCULES et donnes des chiffres precis quand tu as les donnees
        - Tu expliques chaque calcul etape par etape
        - Tu adaptes tes recommandations au contexte marocain et canadien
        - Tu te souviens de tout le contexte de la conversation

        Tu travailles pour des PME industrielles — sois concret et chiffre 
        toujours tes recommandations.
        """

    def calculer_eoq(self, demande_annuelle: float, cout_commande: float, 
                     cout_stockage: float) -> dict:
        """Calcule l'EOQ et les metriques associees."""
        eoq = math.sqrt((2 * demande_annuelle * cout_commande) / cout_stockage)
        nb_commandes = demande_annuelle / eoq
        cout_total = (demande_annuelle / eoq) * cout_commande + (eoq / 2) * cout_stockage
        
        return {
            "eoq": round(eoq, 0),
            "nb_commandes_annuelles": round(nb_commandes, 1),
            "intervalle_jours": round(365 / nb_commandes, 0),
            "cout_total_annuel": round(cout_total, 2)
        }

    def calculer_stock_securite(self, demande_moyenne: float, ecart_type: float,
                                 delai_livraison: float, niveau_service: float = 0.95) -> dict:
        """Calcule le stock de securite et le point de reapprovisionnement."""
        import scipy.stats as stats
        
        z = stats.norm.ppf(niveau_service)
        stock_securite = z * ecart_type * math.sqrt(delai_livraison)
        rop = (demande_moyenne * delai_livraison) + stock_securite
        
        return {
            "stock_securite": round(stock_securite, 0),
            "point_reappro": round(rop, 0),
            "niveau_service": f"{niveau_service * 100}%",
            "facteur_z": round(z, 2)
        }

    def chat(self, user_message: str) -> str:
        """Envoie un message a Youssef et obtient une reponse."""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        assistant_message = response.content[0].text

        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def reset(self):
        """Reinitialise la conversation."""
        self.conversation_history = []
        print("Conversation reinitialisee.")


# Test direct de Youssef
if __name__ == "__main__":
    youssef = YoussefAgent()
    
    print("=" * 50)
    print("ChainIQ — Agent Youssef (Optimisation Stocks)")
    print("Tapez 'quit' pour quitter, 'reset' pour recommencer")
    print("=" * 50)
    print()

    while True:
        user_input = input("Vous : ").strip()
        
        if user_input.lower() == "quit":
            print("Au revoir !")
            break
        elif user_input.lower() == "reset":
            youssef.reset()
            continue
        elif not user_input:
            continue

        print("\nYoussef : ", end="")
        response = youssef.chat(user_input)
        print(response)
        print()