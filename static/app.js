//esto contine todas las funciones que index.html utiliza

document.addEventListener('DOMContentLoaded', ()=> {
    var options={}
    var elems = document.querySelectorAll('.autocomplete');
    var instances = M.Autocomplete.init(elems, options);

    elemInput=document.getElementById('autocomplete-input')
    var instance = M.Autocomplete.getInstance(elemInput);

    elemInput.addEventListener('input',()=>{
		dataInput=elemInput.value

		var search={"term":dataInput}
		console.log(JSON.stringify(search))

		fetch(`${window.origin}/subject`,{
			method:"POST",
			body:JSON.stringify(search) 
		})
		.then(res=>{
			if (res.status !== 200) {
          		console.log(`Error. Status code: ${res.status}`);
          		return;
        	}
			return res.json()
		})
		.then(data=>{
			instance.updateData(data)
		})
	})
});




