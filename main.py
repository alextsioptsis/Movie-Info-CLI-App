import os
import requests
from dotenv import load_dotenv

# Φόρτωση μεταβλητών από το .env
load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"

def get_movie_data(title):
    """
    Τραβάει τα δεδομένα της ταινίας από το OMDb API.
    """
    if not API_KEY:
        print("❌ Σφάλμα: Δεν βρέθηκε το API Key στο .env!")
        return None

    params = {
        "apikey": API_KEY,
        "t": title
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Προσοχή: Το API επιστρέφει "Response" με κεφαλαίο R
        if data.get("Response") == "True":
            return data
        else:
            print(f"❌ Η ταινία '{title}' δεν βρέθηκε!")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Σφάλμα δικτύου: {e}")
        return None

def display_movie_info(movie):
    """
    Εμφανίζει τα στοιχεία της ταινίας όμορφα στο τερματικό.
    """
    print("\n" + "=" * 50)
    print(f"🎬 Τίτλος:     {movie.get('Title')} ({movie.get('Year')})")
    print(f"⭐ Βαθμολογία: {movie.get('imdbRating')} / 10 (IMDb)")
    print(f"🎭 Είδος:      {movie.get('Genre')}")
    print(f"🎬 Σκηνοθέτης: {movie.get('Director')}")
    print(f"👥 Ηθοποιοί:   {movie.get('Actors')}")
    print(f"⏱️ Διάρκεια:   {movie.get('Runtime')}")
    print("-" * 50)
    print(f"📖 Πλοκή:\n{movie.get('Plot')}")
    print("=" * 50 + "\n")

def main():
    """
    Η κεντρική συνάρτηση που τρέχει την εφαρμογή.
    """
    print("Welcome to the Movie Info App! 🍿")
    
    while True:
        search_query = input("Enter a movie title (or 'exit' to quit): ").strip()

        if search_query.lower() in ['exit', 'quit', 'βγες']:
            print("Exiting the Movie Info App. Goodbye! 👋")
            break
            
        if not search_query:
            print("Please enter a valid movie title.")
            continue
            
        movie_data = get_movie_data(search_query)
        if movie_data:
            display_movie_info(movie_data) 

# Εδώ ξεκινάει επίσημα το πρόγραμμα
if __name__ == "__main__":
    main()
               