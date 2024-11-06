# FastAPI Project

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local utilizando `git`:

```bash
git clone https://github.com/tomasdaureli/heycar-backend.git
cd heycar-backend
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Crea un entorno virtual para este proyecto:

```bash
python -m venv env
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias

Instala las dependencias del proyecto utilizando `pip`:

```bash
pip install -r app/requirements.txt
```

### 4. Correr scripts para la creación de la base de datos (de ser necesario)

```bash
app/sql-schemas/*.sql
```

### 5. Cargar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=your_host # localhost
MYSQL_PORT=your_port # 3306
MYSQL_DB=your_database_name # heycar
SECRET_KEY=your_secret_key # 1234567890
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
BADGES_LEVEL_1_POINTS=level_1_min_points #0
BADGES_LEVEL_2_POINTS=level_2_min_points #230
BADGES_LEVEL_3_POINTS=level_3_min_points #550
BADGES_LEVEL_4_POINTS=level_4_min_points #820
BADGES_LEVEL_5_POINTS=level_5_min_points #1000
BADGES_LEVEL_1_NAME=level_1_name #Conductor Novato
BADGES_LEVEL_2_NAME=level_2_name #Piloto Cuidadoso
BADGES_LEVEL_3_NAME=level_3_name #Guardian del Motor
BADGES_LEVEL_4_NAME=level_4_name #Maestro del Volante
BADGES_LEVEL_5_NAME=level_5_name #Leyenda Automotor

```

### 6. Ejecutar el servidor de desarrollo

```bash
cd app
uvicorn main:app --reload
```

### 7. Acceder a la API

La API estará disponible en `http://127.0.0.1:8000`. Puedes usar herramientas como `curl` o Postman para probar los endpoints.

### 8. Documentación interactiva

FastAPI proporciona una documentación interactiva en tiempo de ejecución en `http://127.0.0.1:8000/docs`.

### 9. Crear variable de entorno para script odb_simulator

```bash
API_URL=http://127.0.0.1:8000
VEHICLE_ID=1
INTERVAL_SECONDS=5
```

