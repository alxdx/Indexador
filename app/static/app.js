//esto contine todas las funciones que index.html utiliza

document.addEventListener('DOMContentLoaded', ()=> {
	var options={
		data:null
	}
    options['limit']=8
	fetch(`${window.origin}/subject`)
		.then(res=>{
			if (res.status !== 200) {
          		console.log(`Error. Status code: ${res.status}`);
          		return;
        	}
			return res.json()
		})
		.then(dat=>{
			options.data=dat
			//console.log(options)
		    var elems = document.querySelectorAll('.autocomplete');
		    var instances = M.Autocomplete.init(elems, options);
		})
});




