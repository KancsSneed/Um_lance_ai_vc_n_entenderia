from pathlib import Path

fileName = r"C:\Users\luisk\Documents\MeuProjetos\Um_lance_ai_vc_n_entenderia\desenvolvimento_a_parte\log\log.txt"
fileObj = Path(fileName)
print(fileObj.is_file())