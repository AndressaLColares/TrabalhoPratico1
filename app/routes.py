import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from typing import List
from models import Item
from utils import filtrar_classe, filtrar_especie, filtrar_familia, filtrar_filo, filtrar_genero, filtrar_ordem, filtrar_reino, ler_dados_csv, escrever_dados_csv, calcular_hash, gerar_proximo_id
from config import CSV_FILE, ZIP_FILE, LOG_FILE
import zipfile
import logging

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

router = APIRouter()

@router.get("/")
async def read_root():
    return {"msg": "Hello World"}

@router.get("/itens", response_model=List[Item])
def listar_itens():
    return ler_dados_csv(CSV_FILE)

@router.get("/itens/{item_id}", response_model=Item)
def obter_item(item_id: int):
    itens = ler_dados_csv(CSV_FILE)
    for item in itens:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado. Tente novamente")

@router.get("/total_especies")
async def obter_total_especies():
    total_especies = len(ler_dados_csv(CSV_FILE))
    return {"total_especies": total_especies}

@router.get("/download_zip")
async def download_zip():
    if not os.path.exists(CSV_FILE):
        raise HTTPException(status_code=404, detail="Arquivo CSV não encontrado")
    with zipfile.ZipFile(ZIP_FILE, "w") as zipf:
        zipf.write(CSV_FILE)
    return FileResponse(ZIP_FILE, media_type='application/zip', filename=ZIP_FILE)

@router.get("/hash")
def get_hash():
    return calcular_hash(CSV_FILE)

@router.post("/itens", response_model=Item)
def criar_item(item: Item):
    itens = ler_dados_csv(CSV_FILE)
    item.id = gerar_proximo_id(itens)  
    itens.append(item)
    escrever_dados_csv(itens, CSV_FILE)
    logging.info(f"Espécie {item.id} inserida com sucesso")
    return item

@router.put("/itens/{item_id}", response_model=Item)
def atualizar_item(item_id: int, item_atualizado: Item):
    itens = ler_dados_csv(CSV_FILE)
    for i, item in enumerate(itens):
        if item.id == item_id:
            item_atualizado.id = item_id  
            itens[i] = item_atualizado
            escrever_dados_csv(itens, CSV_FILE)
            logging.info(f"Espécie {item_id} atualizada com sucesso")
            return item_atualizado
    raise HTTPException(status_code=404, detail="Item não encontrado")

@router.delete("/itens/{item_id}", response_model=dict)
def deletar_item(item_id: int):
    itens = ler_dados_csv(CSV_FILE)
    itens_filtrados = [item for item in itens if item.id != item_id]
    if len(itens) == len(itens_filtrados):
        raise HTTPException(status_code=404, detail="Item não encontrado")
    escrever_dados_csv(itens_filtrados, CSV_FILE)
    logging.info(f"Espécie {item_id} deletada com sucesso")
    return {"mensagem": "Item deletado com sucesso"}

@router.get("/itens/{categoria}/{nome}", response_model=List[Item])
def filtrar_categoria(categoria: str, nome: str):
    match categoria:
        case "reino":
            return filtrar_reino(nome)
        case "filo":
            return filtrar_filo(nome)
        case "classe":
            return filtrar_classe(nome)
        case "ordem":
            return filtrar_ordem(nome)
        case "familia":
            return filtrar_familia(nome)
        case "genero":
            return filtrar_genero(nome)
        case "especie":
            return filtrar_especie(nome)
    raise HTTPException(status_code=404, detail="Categoria não encontrada")
