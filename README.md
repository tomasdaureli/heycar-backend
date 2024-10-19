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
pip install -r builder/requirements.txt
```

### 4. Correr scripts para la creación de la base de datos (de ser necesario)

```bash
builder/sql-schemas/*.sql
```

### 5. Cargar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=your_host # localhost
MYSQL_PORT=your_port # 3306
MYSQL_DB=your_database_name # heycar
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





