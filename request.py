import requests
import time

def fetch(url):
    try:
        respuesta = requests.get(url, verify=False)
        return respuesta.text
    except Exception as e:
        return str(e)

def main(url, num_requests):
    print(f'Empezando las {num_requests} peticiones...')
    start_time = time.time()
    
    for i in range(num_requests):
        fetch(url)
        print(f"Petición número {i+1} completada")
    última_peticion = fetch(url)
    print(última_peticion)
    
    end_time = time.time()
    print(f"Completadas {num_requests} peticiones en {end_time - start_time} segundos")
    
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    num_requests = 1000
    main(url, num_requests)