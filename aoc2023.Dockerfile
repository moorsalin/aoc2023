FROM python:3.12-alpine
RUN mkdir -p /workspace/aoc2023
WORKDIR /workspace/aoc2023
COPY . .
RUN apk add git nodejs neovim ripgrep build-base wget bash just pipx libffi-dev --update --no-cache
# RUN apk add bash wget just pipx
RUN git clone https://github.com/NvChad/NvChad ~/.config/nvim
RUN pip install poetry
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
CMD [ "bash" ]