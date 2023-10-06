## API de Reconocimiento de Entidades con SpaCy

Este repositorio contiene una aplicación Flask que utiliza SpaCy para reconocer entidades a partir de oraciones en español. La API acepta una lista de oraciones y devuelve las entidades reconocidas para cada oración.

### Prerrequisitos

- Conda

### Instalación y Configuración

1. Clona el repositorio:

```bash
git clone https://github.com/uteyechea/nlp_test.git
```

2. Crea un nuevo entorno Conda y actívalo:

```bash
conda env create -f environment-multi.yml
conda activate nlp_test
```

### Ejecutar la API

Para ejecutar la API localmente:

```bash
python ner_api.py
```

Esto iniciará el servidor Flask en `http://127.0.0.1:5000/`.

### Uso de la API

Envía una solicitud POST al endpoint raíz (`/`) con un payload JSON que contenga una lista de oraciones. Por ejemplo:

```json
{
    "sentences": ["Esta es una oración de prueba.", "Madrid es la capital de España."]
}
```

La API responderá con una lista de entidades reconocidas para cada oración:

```json
[
    {"oración": "Esta es una oración de prueba.", "entidades": {}},
    {"oración": "Madrid es la capital de España.", "entidades": {"Madrid": "LOC", "España": "LOC"}}
]
```
Ejemplos de solicitudes

#### 1. Linux y macOS:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"sentences": ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.", "San Francisco considera prohibir los robots de entrega en la acera." ]}' http://127.0.0.1:5000/
```

#### 2. Windows:

```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"sentences\": [\"Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.\", \"San Francisco considera prohibir los robots de entrega en la acera.\"]}" http://127.0.0.1:5000/
```


### Manejo de Errores

Si el payload no contiene una lista válida de oraciones, la API devolverá un error 400 con un mensaje:

```json
{
    "error": "No se proporcionó una lista de oraciones"
}
```
