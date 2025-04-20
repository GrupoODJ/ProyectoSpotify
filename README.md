# Proyecto Final - Análisis Musical con Machine Learning 🎧

**Universidad:** Universidad de los Andes  
**Curso:** [Nombre del curso o programa, ej. MIAD]  
**Semestre:** 2025-1  
**Organización GitHub:** [GrupoODJ](https://github.com/GrupoODJ)  
**Repositorio:** [ProyectoSpotify](https://github.com/GrupoODJ/ProyectoSpotify)

---

## 🎯 Descripción

Este proyecto consiste en el desarrollo de un modelo de análisis o recomendación musical utilizando aprendizaje automático, con base en un conjunto de datos musicales (por ejemplo, datos de Spotify).

El trabajo se desarrolla colaborativamente en el archivo principal `S3P1_proyectoSpotify.ipynb`, dentro de un entorno compartido de GitHub y controlado mediante ramas por integrante.

---

## 📁 Estructura del Repositorio

```
ProyectoSpotify/
│
├── S3P1_proyectoSpotify.ipynb # Notebook principal del proyecto
├── data/                      # Archivos de entrada
├── images/                    # Visualizaciones generadas
├── README.md                  # Este archivo
└── .gitignore                 # Exclusión de archivos innecesarios
```
---

## 🤝 Guía de colaboración para el equipo

### 1. Clonar el repositorio

```bash
git clone https://github.com/GrupoODJ/ProyectoSpotify.git
cd ProyectoSpotify
```

### 2. Crear una rama con tu nombre

```bash
git checkout -b tu-nombre
git push origin tu-nombre
```

Ejemplo:
```bash
git checkout -b camilo-desarrollo
```

### 3. Hacer cambios y subir

```bash
git add .
git commit -m "Descripción clara de los cambios"
git push origin tu-nombre
```

### 4. Crear un Pull Request en GitHub

- Ve a la pestaña **"Pull Requests"**.
- Haz clic en **"New Pull Request"**.
- Asegúrate que diga: `base: main ← compare: tu-rama`
- Agrega título y descripción, luego haz clic en **"Create Pull Request"**.

### 5. Revisión y merge

- El equipo puede comentar y aprobar.
- Al aprobar, haz clic en **"Merge pull request"**.
- Luego, elimina la rama si ya no se necesita.

### 🧠 Buenas prácticas

- Trabajar solo en tu rama.
- Sincroniza tu rama con `main` antes de subir:
  ```bash
  git pull origin main
  ```
- Mantén mensajes de commit claros.
- No trabajes sobre `main` directamente.