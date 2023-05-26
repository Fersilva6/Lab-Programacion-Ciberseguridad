import dns.resolver

# Obtener el contenido de la caché de DNS
resolver = dns.resolver.Resolver()
resolver.cache.flush()
cache = resolver.cache
cache_entries = cache.dump()

# Mostrar el contenido de la caché de DNS
if len(cache_entries) > 0:
    print("Contenido de la caché de DNS:")
    for entry in cache_entries:
        print(f"Nombre: {entry.name}")
        print(f"Tipo: {entry.rdtype}")
        print(f"TTL: {entry.ttl}")
        print(f"Respuesta: {entry.response}")
        print("-----------------------------")
else:
    print("La caché de DNS está vacía.")
