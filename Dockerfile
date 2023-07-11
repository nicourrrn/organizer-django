FROM archlinux:latest 
RUN pacman -Sy python-poetry --noconfirm

WORKDIR /app
COPY . .
RUN poetry install
CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "fin_manager.asgi:application"]

