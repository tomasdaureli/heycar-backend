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
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows
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
# En caso de usar MySQL
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=your_host # localhost
MYSQL_PORT=your_port # 3306
MYSQL_DB=your_database_name # heycar
# En caso de usar PostgreSQL
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=your_host # localhost
POSTGRES_PORT=your_port # 5432
POSTGRES_DB=your_database_name # heycar

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

FCM_API_KEY=your_fcm_api_key
FCM_PROJECT_ID=your_fcm_project_id
FCM_SERVICE_ACCOUNT_FILE=path_to_your_firebase_file

EXPO_NOTIFICATION_URL=https://exp.host/--/api/v2/push/send

# OBD Simulator
API_URL=https://heycar-backend.onrender.com
INTERVAL_SECONDS=5
VEHICLE_ID=vehicle_id
```

### 6. Ejecutar el servidor de desarrollo

```bash
cd app
uvicorn main:app --reload
```

### 7. Acceder a la API

La API estará disponible en `http://127.0.0.1:8000`. Puedes usar herramientas como `curl` o Postman para probar los endpoints.

### 8. Documentación interactiva

FastAPI proporciona una documentación interactiva en tiempo de ejecución en `http://127.0.0.1:8000/docs` o `http://127.0.0.1:8000/redoc`.
