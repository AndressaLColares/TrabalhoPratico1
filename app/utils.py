import csv
import os
import hashlib
from typing import List
from fastapi import HTTPException
from models import Item

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
