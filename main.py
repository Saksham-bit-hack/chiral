from fastapi import FastAPI
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.get("/analyze")
def analyze(smiles: str):
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return {"error": "Invalid SMILES"}

    # Assign stereochemistry
    Chem.AssignStereochemistry(mol, force=True, cleanIt=True)

    # Molecular properties
    formula = rdMolDescriptors.CalcMolFormula(mol)
    weight = round(Descriptors.MolWt(mol), 2)

    # Chiral centers
    chiral = Chem.FindMolChiralCenters(mol, includeUnassigned=True)

    chiral_data = []
    for idx, config in chiral:
        atom = mol.GetAtomWithIdx(idx)
        if atom.GetSymbol() == "C":
            chiral_data.append({
                "atom_index": idx,
                "configuration": config
            })

    return {
        "formula": formula,
        "molecular_weight": weight,
        "chiral_centers": chiral_data
    }
