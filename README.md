# 👤 Microservicio de Clientes

Servicio de **usuarios/clientes** con API **GraphQL** (más DRF) y su frontend de administración.

![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-Graphene-E10098?logo=graphql&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white)

## Componentes

| Carpeta | Qué es | Puerto |
|---|---|---|
| `users_services/` | Django + Graphene + DRF + PostgreSQL | 3001 (`/api/graphql/`) |
| `users-frontend/` | React 19 + Apollo Client + Bootstrap | 5173 |

## Variables de entorno

Copia `.env.example` a `.env`: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` (**obligatoria**), `DB_HOST`, `DB_PORT`.

## Cómo correrlo

### Con Docker

```bash
git clone https://github.com/JSRT23/microservicio-clientes.git
cd microservicio-clientes
cp .env.example .env
docker compose up --build      # db + users_service (3001) + frontend (5173)
```

### Sin Docker

```bash
# Backend (Python 3.12, PostgreSQL local)
cd users_services
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DB_PASSWORD=... DB_HOST=127.0.0.1
python manage.py migrate && python manage.py runserver 3001

# Frontend
cd ../users-frontend && npm ci && npm run dev
```

> El frontend apunta a `http://127.0.0.1:3001/api/graphql/` (fijo en el código).

## Notas

- Se quitó del código la contraseña de la base de datos; **cámbiala** donde se haya usado.
- `requirements.txt` quedó en UTF-8 (estaba en UTF-16).
