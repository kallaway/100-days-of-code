import './App.css';
import AppBar from './components/AppBar/AppBar'
import AppControlsCounter from './components/AppControls/AppControlsCounter'
import AppControlsDelete from './components/AppControls/AppControlsDelete'
import AppControlsInputs from './components/AppControls/AppControlsInputs'

const App = () => {
  return (
    <div className="App">
      <AppBar/>
      <AppControlsCounter/>
      <AppControlsDelete/>
      <AppControlsInputs/>
    </div>
  );
}

export default App;
