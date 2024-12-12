import csv
import os
import hashlib
from typing import List
from fastapi import HTTPException
from models import Item
from config import CSV_FILE  

def ler_dados_csv(csv_file: str) -> List[Item]:
    itens = []
    if os.path.exists(csv_file):
        with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                itens.append(Item(
                    id=int(row["id"]),
                    reino=row["reino"],
                    filo=row["filo"],
                    classe=row["classe"],
                    ordem=row["ordem"],
                    familia=row["familia"],
                    genero=row["genero"],
                    especie=row["especie"]
                ))
    return itens

def escrever_dados_csv(itens: List[Item], csv_file: str):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "reino", "filo", "classe", "ordem", "familia", "genero", "especie"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in itens:
            writer.writerow(item.dict())

def calcular_hash(csv_file: str):
    if not os.path.exists(csv_file):
        raise HTTPException(status_code=404, detail="Arquivo CSV não encontrado")
    with open(csv_file, "rb") as f:
        hash_sha256 = hashlib.sha256(f.read()).hexdigest()
    return {"hash_sha256": hash_sha256}

def gerar_proximo_id(itens: List[Item]) -> int:
    if not itens:
        return 1
    return max(item.id for item in itens) + 1

def filtrar_reino(reino: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE)  
    itens_filtrados: List[Item] = [] 
    for item in itens:
        if item.reino == reino:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Reino não encontrado")

def filtrar_filo(filo: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE)  
    itens_filtrados: List[Item] = []  
    for item in itens:
        if item.filo == filo:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Filo não encontrado")

def filtrar_classe(classe: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE) 
    itens_filtrados: List[Item] = []  
    for item in itens:
        if item.classe == classe:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Classe não encontrada")

def filtrar_ordem(ordem: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE)  
    itens_filtrados: List[Item] = []  
    for item in itens:
        if item.ordem == ordem:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Ordem não encontrada")

def filtrar_familia(familia: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE)  
    itens_filtrados: List[Item] = [] 
    for item in itens:
        if item.familia == familia:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Familia não encontrada")

def filtrar_genero(genero: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE)  
    itens_filtrados: List[Item] = [] 
    for item in itens:
        if item.genero == genero:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Genero não encontrado")

def filtrar_especie(especie: str) -> List[Item]:
    itens = ler_dados_csv(CSV_FILE)  
    itens_filtrados: List[Item] = []  
    for item in itens:
        if item.especie == especie:
            itens_filtrados.append(item)
    if itens_filtrados:
        return itens_filtrados
    raise HTTPException(status_code=404, detail="Especie não encontrada")
