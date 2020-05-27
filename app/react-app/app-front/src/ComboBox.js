import React from 'react';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';

export default function ComboBox(props) {
  //const [value,setValue] = React.useState(props.params[0]);

  return (
    <Autocomplete
      id={props.id}
      onChange={props.getSelected.bind()}
      options={props.params}
      getOptionLabel={(option) => option.title}
      style={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label={props.label} variant="outlined" />}
    />
  );
}
