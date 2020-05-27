import React from 'react';
import Button from '@material-ui/core/Button'
import ComboBox from './ComboBox.js'
import SearchBarMaterias from './SearchBarMaterias.js'
const Carreras=[
  {"title":"COM semestral"},
  {"title":"COM cuatrimestral"},
  {"title":"ITI semestral"},
  {"title":"ITI cuatrimestral"},
  {"title":"ICC semestral"},
  {"title":"ICC cuatrimestral"}
]

const onPlanChanged=(event, newInputValue) => {
        if (newInputValue!=null) {
          console.log(newInputValue.title)          
        }
      }

function App() {
  return (
    <div>
      <ComboBox id="carreras" params={Carreras} label="Selecciona tu carrera" getSelected={onPlanChanged} ></ComboBox>
      <SearchBarMaterias/>
    </div>
  );
}

export default App;
