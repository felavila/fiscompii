# Ejemplo LaTeX


### Ejemplo en Overleaf

Puedes revisar y editar el ejemplo directamente en Overleaf:

[![Open in Overleaf](https://img.shields.io/badge/Open%20in-Overleaf-47A141?logo=overleaf&logoColor=white)](https://www.overleaf.com/read/vfgcvszqsbfr#d509d2)

Para ejecutar localmente:
    Primero instalar
```bash
sudo tlmgr install latexmk
sudo tlmgr install biber
```
    Luego  descomprimir el archivo zip y dentro de la carpeta:
```bash
latexmk -pdf main.tex
```