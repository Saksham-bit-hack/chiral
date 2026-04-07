async function analyze() {
  const query = document.getElementById("search").value || "Ritonavir";

  const res = await fetch(
    `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${query}/property/MolecularWeight,IUPACName,CanonicalSMILES/JSON`
  );

  const data = await res.json();
  const compound = data.PropertyTable.Properties[0];

  const img = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/${compound.CanonicalSMILES}/PNG`;

  document.getElementById("result").innerHTML = `
    <div class="bg-gray-900 p-6 rounded-xl shadow-lg">
      <h2 class="text-2xl mb-2">${query}</h2>
      <p><b>IUPAC:</b> ${compound.IUPACName}</p>
      <p><b>Weight:</b> ${compound.MolecularWeight}</p>
      <img src="${img}" class="mt-4 rounded-lg"/>
    </div>
  `;
}
