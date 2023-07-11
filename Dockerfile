FROM archlinux:latest 
RUN pacman -Sy python-poetry --noconfirm

WORKDIR /app
COPY . .
RUN poetry install
CMD ["poetry", "run", "uvicorn", "fin_manager.asgi:application"]

