# Con el script sin paralelismo se ha tardado unos 165 segundos en hacer las 1000 peticiones. Vamos a implementar ahora el paralelismo.
# Con 100 hilos (max_workers = 100), se reduce el tiempo a ~ 20 segundos.

import requests
import time
import concurrent.futures as cf

def fetch(url):
    try:
        respuesta = requests.get(url, verify=False)
        return respuesta.text
    except Exception as e:
        return str(e)

def main(url, num_requests):
    print(f'Empezando las {num_requests} peticiones...')
    start_time = time.time()

    # con ThreadPoolExecutor podemos hacer peticiones en paralelo en vez de esperar a la anterior
    with cf.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(fetch, url) for _ in range(num_requests)] # Si los 100 hilos están ocupados, se programa una nueva tarea para que se ejecute cuando esté disponible un hilo
        for i, _ in enumerate(cf.as_completed(futures)):
            print(f"Petición número {i+1} completada")

    última_peticion = fetch(url)
    print(última_peticion)
    
    end_time = time.time()
    print(f"Completadas {num_requests} peticiones en {end_time - start_time} segundos")
    
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    num_requests = 1000
    main(url, num_requests)