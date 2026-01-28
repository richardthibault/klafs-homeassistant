"""Test script for the REAL Klafs API endpoints."""
import asyncio
import aiohttp
import json
from getpass import getpass

API_BASE_URL = "https://sauna-app.klafs.com"
API_LOGIN_ENDPOINT = "/Account/Login"
SAUNA_ID = "YOUR_SAUNA_ID_HERE"  # Replace with your actual sauna ID


async def login(session, username, password):
    """Login to Klafs API."""
    print("\n" + "="*60)
    print("LOGIN")
    print("="*60)
    
    data = {
        "UserName": username,
        "Password": password,
    }
    
    print(f"→ Login avec {username}...")
    async with session.post(
        f"{API_BASE_URL}{API_LOGIN_ENDPOINT}",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        allow_redirects=True,
    ) as response:
        if response.status == 200:
            print("✓ Login réussi!")
            return response.cookies
        else:
            print(f"✗ Login échoué: {response.status}")
            return None


async def get_sauna_status(session, cookies, sauna_id):
    """Get sauna status."""
    print("\n" + "="*60)
    print("GET STATUS")
    print("="*60)
    
    url = f"{API_BASE_URL}/SaunaApp/GetData?id={sauna_id}"
    print(f"→ GET {url}")
    
    async with session.get(url, cookies=cookies) as response:
        print(f"→ Status: {response.status}")
        if response.status == 200:
            data = await response.json()
            print("✓ Statut récupéré!")
            print(f"→ Données: {json.dumps(data, indent=2)}")
            return data
        else:
            text = await response.text()
            print(f"✗ Erreur: {text[:500]}")
            return None


async def start_sauna(session, cookies, sauna_id, pin):
    """Start the sauna."""
    print("\n" + "="*60)
    print("START SAUNA")
    print("="*60)
    
    url = f"{API_BASE_URL}/SaunaApp/StartCabin"
    data = {
        "id": sauna_id,
        "pin": pin,
        "time_selected": False,
        "sel_hour": 0,
        "sel_min": 0
    }
    
    print(f"→ POST {url}")
    print(f"→ Data: {json.dumps(data, indent=2)}")
    
    async with session.post(
        url,
        json=data,
        cookies=cookies,
        headers={"Content-Type": "application/json"},
    ) as response:
        print(f"→ Status: {response.status}")
        if response.status == 200:
            result = await response.json()
            print("✓ Commande envoyée!")
            print(f"→ Résultat: {json.dumps(result, indent=2)}")
            return result
        else:
            text = await response.text()
            print(f"✗ Erreur: {text[:500]}")
            return None


async def stop_sauna(session, cookies, sauna_id):
    """Stop the sauna."""
    print("\n" + "="*60)
    print("STOP SAUNA")
    print("="*60)
    
    url = f"{API_BASE_URL}/SaunaApp/StopCabin"
    data = {
        "id": sauna_id
    }
    
    print(f"→ POST {url}")
    print(f"→ Data: {json.dumps(data, indent=2)}")
    
    async with session.post(
        url,
        json=data,
        cookies=cookies,
        headers={"Content-Type": "application/json"},
    ) as response:
        print(f"→ Status: {response.status}")
        if response.status == 200:
            result = await response.json()
            print("✓ Commande envoyée!")
            print(f"→ Résultat: {json.dumps(result, indent=2)}")
            return result
        else:
            text = await response.text()
            print(f"✗ Erreur: {text[:500]}")
            return None


async def change_temperature(session, cookies, sauna_id, temperature):
    """Change sauna temperature."""
    print("\n" + "="*60)
    print("CHANGE TEMPERATURE")
    print("="*60)
    
    url = f"{API_BASE_URL}/SaunaApp/ChangeTemperature"
    data = {
        "id": sauna_id,
        "temp": temperature
    }
    
    print(f"→ POST {url}")
    print(f"→ Data: {json.dumps(data, indent=2)}")
    
    async with session.post(
        url,
        json=data,
        cookies=cookies,
        headers={"Content-Type": "application/json"},
    ) as response:
        print(f"→ Status: {response.status}")
        if response.status == 200:
            result = await response.json()
            print("✓ Commande envoyée!")
            print(f"→ Résultat: {json.dumps(result, indent=2)}")
            return result
        else:
            text = await response.text()
            print(f"✗ Erreur: {text[:500]}")
            return None


async def main():
    """Main test function."""
    print("="*60)
    print("TEST DE L'API KLAFS RÉELLE")
    print("="*60)
    
    # Get credentials
    print("\nEntrez vos identifiants Klafs:")
    username = input("Username (email): ")
    password = getpass("Password: ")
    
    async with aiohttp.ClientSession() as session:
        # Login
        cookies = await login(session, username, password)
        if not cookies:
            print("\n✗ Impossible de continuer sans authentification")
            return
        
        # Get status
        status = await get_sauna_status(session, cookies, SAUNA_ID)
        
        # Ask user what to test
        print("\n" + "="*60)
        print("QUE VOULEZ-VOUS TESTER ?")
        print("="*60)
        print("1. Récupérer le statut uniquement (déjà fait)")
        print("2. Tester START (nécessite le PIN)")
        print("3. Tester STOP")
        print("4. Tester changement de température")
        print("5. Quitter")
        
        choice = input("\nVotre choix (1-5): ").strip()
        
        if choice == "2":
            pin = getpass("Entrez le PIN du sauna: ")
            await start_sauna(session, cookies, SAUNA_ID, pin)
            # Get status again
            await asyncio.sleep(2)
            await get_sauna_status(session, cookies, SAUNA_ID)
        elif choice == "3":
            await stop_sauna(session, cookies, SAUNA_ID)
            # Get status again
            await asyncio.sleep(2)
            await get_sauna_status(session, cookies, SAUNA_ID)
        elif choice == "4":
            temp = input("Température souhaitée (°C): ")
            await change_temperature(session, cookies, SAUNA_ID, int(temp))
            # Get status again
            await asyncio.sleep(2)
            await get_sauna_status(session, cookies, SAUNA_ID)
        
        print("\n" + "="*60)
        print("TESTS TERMINÉS")
        print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
