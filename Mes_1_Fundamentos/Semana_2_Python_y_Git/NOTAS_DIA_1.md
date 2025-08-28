# --- DÍA 1: Introducción a Git ---

## 1. ¿Qué es el Control de Versiones?
* **Mi definición:** Es un sistema que registra los cambios en un conjunto de archivos a lo largo del tiempo. Esto nos permite volver a versiones anteriores, ver el historial de cambios, y trabajar de forma segura.
* **Analogía:** Como guardar múltiples versiones de un documento de Word con diferentes nombres ("carta_final_final.docx", "carta_version_2.docx"), pero de una manera inteligente y organizada.

## 2. ¿Qué es Git?
* **Mi definición:** Es el sistema de control de versiones distribuido más popular del mundo. Lo usamos desde la terminal para gestionar nuestro código.
* **Diferencia clave:** Git es la herramienta que usas en tu computadora. GitHub, GitLab, o Bitbucket son servicios en la nube para almacenar tus repositorios de Git y colaborar con otros.

## 3. Flujo Básico de Git
* **Directorio de trabajo:** Tus archivos actuales.
* **Staging Area (Área de Preparación):** Una especie de "sala de espera" para los archivos que quieres incluir en tu próximo commit.
* **Repositorio Local:** La base de datos de tu proyecto donde se guardan los commits.

## 4. Comandos Esenciales de Git que Aprendí Hoy
* `git --version`: Verifica si Git está instalado.
* `git init`: Inicializa un nuevo repositorio de Git en la carpeta actual.
* `git status`: Muestra el estado de los archivos (modificados, listos para commit, etc.).
* `git add [nombre_archivo]` o `git add .`: Añade archivos al área de preparación.
* `git commit -m "[mensaje]"`: Guarda los cambios en el repositorio con un mensaje descriptivo.
* `git log`: Muestra el historial de commits.